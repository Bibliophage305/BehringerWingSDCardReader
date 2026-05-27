import wave

import json

import psutil
import questionary
import tqdm

import msgspec

from collections import defaultdict
from pathlib import Path

from wing_snapfile.api.snapfile import load_snapfile, dump_snapfile


def get_input_path() -> Path:
    x_live_paths = []

    for partition in psutil.disk_partitions():
        p = Path(partition.device) / "X_LIVE"
        if p.exists():
            for subdir in p.iterdir():
                x_live_paths.append(subdir)

    if x_live_paths:
        path = questionary.select(
            "Which directory to use as input?",
            choices=[questionary.Choice(str(p), value=p) for p in x_live_paths]
            + ["Other"],
        ).ask()

        if path != "Other":
            return path

    return Path(questionary.path("Enter the path to the input directory").ask())


def validate_input_path(input_path: Path):
    if not input_path.exists():
        raise FileNotFoundError(f"{input_path} does not exist")

    if not input_path.is_dir():
        raise FileNotFoundError(f"{input_path} is not a directory")


def get_output_path(input_path: Path) -> Path:
    output_path = Path(questionary.path("Enter the path to the output directory").ask())
    output_path_subdirectory = questionary.select(
        "Export to:",
        choices=[
            questionary.Choice(str(p), value=p)
            for p in [output_path / input_path.name, output_path]
        ],
    ).ask()
    if not output_path_subdirectory.exists():
        print(f"Creating output directory {output_path_subdirectory}...")
        output_path_subdirectory.mkdir(parents=True)
    return output_path_subdirectory


def get_wav_paths(input_path: Path) -> list[Path]:
    wav_paths = []
    for file_path in input_path.iterdir():
        if not file_path.is_file():
            continue
        if file_path.suffix.lower() == ".wav":
            wav_paths.append(file_path)
    wav_paths.sort()
    return wav_paths


def validate_wav_paths(wav_paths: list[Path]):
    if not wav_paths:
        raise FileNotFoundError("No .wav files found in input directory")

    formats = defaultdict(list)
    for path in wav_paths:
        with wave.open(str(path), "rb") as wf:
            fmt = (wf.getnchannels(), wf.getsampwidth(), wf.getframerate())
            formats[fmt].append(path)

    if len(formats) > 1:
        error_message_lines = ["", "Multiple audio formats found in input files:"]
        for i, ((nchannels, sampwidth, framerate), paths) in enumerate(formats.items()):
            error_message_lines.append("")
            error_message_lines.append(f"Format {i+1}:")
            error_message_lines.append(f"    Channels: {nchannels}")
            error_message_lines.append(f"    Sample Width: {sampwidth}")
            error_message_lines.append(f"    Frame Rate: {framerate}")
            error_message_lines.append("Files:")
            for path in paths:
                error_message_lines.append(f"    {path}")
        raise ValueError("\n".join(error_message_lines))


def verify_channel_list(channel_list: list[str], output_path: Path):
    if len(channel_list) != len(set(channel_list)):
        raise ValueError("Channel list has duplicate names, abandoning")
    if any(name.strip() == "" for name in channel_list):
        raise ValueError("Channel list has empty names, abandoning")
    overwrite_candidates = [
        output_file_path
        for output_file_path in channel_list
        if (output_path / output_file_path).exists()
    ]
    if overwrite_candidates:
        error_message_lines = [
            "",
            "The following channel names would overwrite existing files in the output directory:",
        ]
        for name in overwrite_candidates:
            error_message_lines.append(f"    {name}")
        raise ValueError("\n".join(error_message_lines))


def choose_channels_to_extract(channel_list: list[str]) -> list[int]:
    return questionary.checkbox(
        "Select channels to extract",
        choices=[
            questionary.Choice(name, value=i, checked=True)
            for i, name in enumerate(channel_list)
        ],
        validate=lambda selected: (
            True if selected else "You must select at least one channel"
        ),
    ).ask()


def verify_output_files(
    channel_list: list[str],
    output_path: Path,
    total_frames: int,
    sampwidth: int,
    channels_to_extract: list[int],
):
    print("\n--- Verification ---")

    expected_data_bytes = total_frames * sampwidth

    all_ok = True

    for channel_index, channel_name in enumerate(channel_list):
        if channel_index not in channels_to_extract:
            continue

        out_path = output_path / channel_name

        with wave.open(str(out_path), "rb") as wf:
            actual_frames = wf.getnframes()
            actual_bytes = actual_frames * wf.getsampwidth()

        file_size = out_path.stat().st_size
        header_size = file_size - actual_bytes

        print(f"{out_path}:")
        print(f"  Expected frames: {total_frames}")
        print(f"  Actual frames:   {actual_frames}")
        print(f"  Expected bytes:  {expected_data_bytes}")
        print(f"  Actual bytes:    {actual_bytes}")
        print(f"  Header size:     {header_size}")

        if actual_frames != total_frames or actual_bytes != expected_data_bytes:
            print("  ❌ MISMATCH")
            all_ok = False
        else:
            print("  ✅ OK")

    if not all_ok:
        print("\nWARNING: One or more output files failed verification.")
    else:
        print("\nAll output files verified successfully.")


def main():

    input_path = get_input_path()
    validate_input_path(input_path)

    output_path = get_output_path(input_path)

    wav_paths = get_wav_paths(input_path)
    validate_wav_paths(wav_paths)

    channel_list = [
        "EMPTY Kick In",
        "Kick Out",
        "Snare Top",
        "EMPTY Snare Bottom",
        "Rack Tom",
        "Floor Tom",
        "EMPTY Hats",
        "EMPTY Ride",
        "Overhead L",
        "Overhead R",
        "Bass Guitar",
        "Acoustic Guitar",
        "Electric Guitar L",
        "Electric Guitar R",
        "Keyboards L",
        "Keyboards R",
        "Georgie Vocal",
        "Electric Guitar Vocal",
        "Bass Vocal",
        "Keys Vocal",
        "Zak Vocal",
        "Zak Guitar",
        "Crowd",
        "Talkback",
        "Tracks L",
        "Tracks R",
        "Tracks Sub",
        "Click",
        "Cues",
        "Main L",
        "Main R",
    ]

    channel_list = [f"{i+1:02} {name}.wav" for i, name in enumerate(channel_list)]

    with wave.open(str(wav_paths[0]), "rb") as wf:
        channel_count = wf.getnchannels()

        if channel_count < len(channel_list):
            print(
                f"{len(channel_list)} channel names provided, but source only has {channel_count} channels"
            )
            print(f"Truncating channel list to {channel_count} channels")
            channel_list = channel_list[:channel_count]
        elif channel_count > len(channel_list):
            print(
                f"Source has {channel_count} channels, but only {len(channel_list)} channel names provided"
            )
            print(f"Extending channel names to {channel_count}")
            while len(channel_list) < channel_count:
                channel_list.append(f"{len(channel_list)+1:02} EMPTY.wav")

        sampwidth = wf.getsampwidth()
        framerate = wf.getframerate()

    verify_channel_list(channel_list, output_path)

    channels_to_extract = choose_channels_to_extract(channel_list)

    writers = []

    for channel_index, channel_name in enumerate(channel_list):
        if channel_index not in channels_to_extract:
            writers.append(None)
            continue
        writer = wave.open(str(output_path / channel_name), "wb")
        writer.setnchannels(1)
        writer.setsampwidth(sampwidth)
        writer.setframerate(framerate)
        writers.append(writer)

    total_frames = 0

    for wav_path in wav_paths:
        with wave.open(str(wav_path), "rb") as wf:
            total_frames += wf.getnframes()

    frames_written = 0

    with tqdm.tqdm(total=total_frames, unit="frames") as pbar:
        for wav_path in wav_paths:
            pbar.set_description(f"Processing {wav_path.name}")

            with wave.open(str(wav_path), "rb") as wf:

                frame_size = channel_count * sampwidth

                while True:
                    pbar.update(frames_written - pbar.n)
                    frames = wf.readframes(
                        2**20
                    )  # tune for performance/memory tradeoff
                    if not frames:
                        break

                    n_frames = len(frames) // frame_size

                    frames_written += n_frames

                    channel_buffers = [bytearray() for _ in range(channel_count)]

                    for i in range(n_frames):
                        base = i * frame_size
                        for channel_index in range(channel_count):
                            start = base + channel_index * sampwidth
                            end = start + sampwidth
                            channel_buffers[channel_index].extend(frames[start:end])

                    for writer, channel_buffer in zip(writers, channel_buffers):
                        if writer is not None:
                            writer.writeframes(channel_buffer)

    for writer in writers:
        if writer is not None:
            writer.close()

    verify_output_files(
        channel_list, output_path, total_frames, sampwidth, channels_to_extract
    )

def compare_dicts(d1: dict, d2: dict, path=""):
    are_equal = True
    for key in sorted(d1.keys() | d2.keys()):
        if key not in d1:
            print(f"Key {path + key} only in second dict")
        elif key not in d2:
            print(f"Key {path + key} only in first dict")
        else:
            v1 = d1[key]
            v2 = d2[key]
            if isinstance(v1, dict) and isinstance(v2, dict):
                compare_dicts(v1, v2, path + key + ".")
            elif v1 != v2:
                print(f"Value mismatch at {path + key}: {v1} != {v2}")
                are_equal = False
    return are_equal


if __name__ == "__main__":
    # main()
    with open(Path("TestRouting.snap"), "r") as f:
        snapfile_json = json.load(f)
    
    snapfile = load_snapfile(snapfile_json)

    # print(snapfile.audio_engine_data.channels[1].tags)
    # print(snapfile.audio_engine_data.dcas)

    roundtrip_json = dump_snapfile(snapfile)

    if compare_dicts(snapfile_json, roundtrip_json):
        if snapfile_json == roundtrip_json:
            print("Success: snapfile JSON matches exactly after parsing and serialization")
        else:
            print("How strange! JSON dicts are equal but not identical after parsing and serialization")
