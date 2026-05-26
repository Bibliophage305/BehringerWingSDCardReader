from wing_snapfile.models.audio.record_settings import AudioRecordSettings


class AudioRecordSettingsCodec:
    @staticmethod
    def decode(data: dict) -> AudioRecordSettings:
        return AudioRecordSettings(
            path=data["path"],
            resolution=data["resolution"],
            channels=data["channels"],
        )

    @staticmethod
    def encode(obj: AudioRecordSettings) -> dict:
        return {
            "path": obj.path,
            "resolution": obj.resolution,
            "channels": obj.channels,
        }