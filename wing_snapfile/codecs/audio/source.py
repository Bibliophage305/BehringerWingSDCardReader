from wing_snapfile.models.audio.source import (
    AudioSource,
    AudioPhaseInvertibleSource,
    AudioPreampAccessibleSource,
    AudioOscillatorSettings,
    AudioOscillatorSource,
    AudioUserSignalSettings,
    AudioUserSignalFullSettings,
    AudioUserSignalSource,
    AudioUserSignalPatchSource,
    AudioSourceBank,
)
from wing_snapfile.helpers.indexed import encode_indexed, parse_indexed


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _decode_source_base(data: dict) -> dict:
    return {
        "mode": data["mode"],
        "mute": data["mute"],
        "color": data["col"],
        "name": data["name"],
        "icon": data["icon"],
        "tags": data["tags"].split(","),
    }


def _encode_source_base(obj: AudioSource) -> dict:
    return {
        "mode": obj.mode,
        "mute": obj.mute,
        "col": obj.color,
        "name": obj.name,
        "icon": obj.icon,
        "tags": ",".join(obj.tags),
    }


def _decode_phase_invertible(data: dict) -> dict:
    return {
        **_decode_source_base(data),
        "phase_invert": data["pol"],
    }


def _encode_phase_invertible(obj: AudioPhaseInvertibleSource) -> dict:
    return {
        **_encode_source_base(obj),
        "pol": obj.phase_invert,
    }


# ---------------------------------------------------------------------------
# Leaf codecs
# ---------------------------------------------------------------------------

class AudioPreampAccessibleSourceCodec:
    @staticmethod
    def decode(data: dict) -> AudioPreampAccessibleSource:
        return AudioPreampAccessibleSource(
            **_decode_phase_invertible(data),
            gain=float(data["g"]),
            phantom_power=data["vph"],
            remote_control=data["rmt"],
            link_customization_to_source=data["rcvc"],
        )

    @staticmethod
    def encode(obj: AudioPreampAccessibleSource) -> dict:
        return {
            **_encode_phase_invertible(obj),
            "g": obj.gain,
            "vph": obj.phantom_power,
            "rmt": obj.remote_control,
            "rcvc": obj.link_customization_to_source,
        }


class AudioPhaseInvertibleSourceCodec:
    @staticmethod
    def decode(data: dict) -> AudioPhaseInvertibleSource:
        return AudioPhaseInvertibleSource(**_decode_phase_invertible(data))

    @staticmethod
    def encode(obj: AudioPhaseInvertibleSource) -> dict:
        return _encode_phase_invertible(obj)


class AudioOscillatorSettingsCodec:
    @staticmethod
    def decode(data: dict) -> AudioOscillatorSettings:
        return AudioOscillatorSettings(
            level=float(data["lvl"]),
            mode=data["mode"],
            frequency=float(data["f"]),
        )

    @staticmethod
    def encode(obj: AudioOscillatorSettings) -> dict:
        return {
            "lvl": obj.level,
            "mode": obj.mode,
            "f": obj.frequency,
        }


class AudioOscillatorSourceCodec:
    @staticmethod
    def decode(data: dict) -> AudioOscillatorSource:
        return AudioOscillatorSource(
            **_decode_source_base(data),
            oscillator_settings=AudioOscillatorSettingsCodec.decode(data["osc"]),
        )

    @staticmethod
    def encode(obj: AudioOscillatorSource) -> dict:
        return {
            **_encode_source_base(obj),
            "osc": AudioOscillatorSettingsCodec.encode(obj.oscillator_settings),
        }


class AudioUserSignalSettingsCodec:
    @staticmethod
    def decode(data: dict) -> AudioUserSignalSettings:
        return AudioUserSignalSettings(
            group=data["grp"],
            input=data["in"],
        )

    @staticmethod
    def encode(obj: AudioUserSignalSettings) -> dict:
        return {
            "grp": obj.group,
            "in": obj.input,
        }


class AudioUserSignalFullSettingsCodec:
    @staticmethod
    def decode(data: dict) -> AudioUserSignalFullSettings:
        return AudioUserSignalFullSettings(
            group=data["grp"],
            input=data["in"],
            tap_point=data["tap"],
            lr_mode=data["lr"],
        )

    @staticmethod
    def encode(obj: AudioUserSignalFullSettings) -> dict:
        return {
            "grp": obj.group,
            "in": obj.input,
            "tap": obj.tap_point,
            "lr": obj.lr_mode,
        }


class AudioUserSignalSourceCodec:
    @staticmethod
    def decode(data: dict) -> AudioUserSignalSource:
        return AudioUserSignalSource(
            **_decode_phase_invertible(data),
            user_signal_settings=AudioUserSignalFullSettingsCodec.decode(data["user"]),
        )

    @staticmethod
    def encode(obj: AudioUserSignalSource) -> dict:
        return {
            **_encode_phase_invertible(obj),
            "user": AudioUserSignalFullSettingsCodec.encode(obj.user_signal_settings),
        }


class AudioUserSignalPatchSourceCodec:
    @staticmethod
    def decode(data: dict) -> AudioUserSignalPatchSource:
        return AudioUserSignalPatchSource(
            **_decode_phase_invertible(data),
            user_signal_settings=AudioUserSignalSettingsCodec.decode(data["user"]),
        )

    @staticmethod
    def encode(obj: AudioUserSignalPatchSource) -> dict:
        return {
            **_encode_phase_invertible(obj),
            "user": AudioUserSignalSettingsCodec.encode(obj.user_signal_settings),
        }


# ---------------------------------------------------------------------------
# AudioSourceBank
# ---------------------------------------------------------------------------

_USR_SPLIT = 24  # indices 1-24 → UserSignal, 25+ → UserSignalPatch


class AudioSourceBankCodec:
    @staticmethod
    def decode(data: dict) -> AudioSourceBank:
        usr = data["USR"]
        return AudioSourceBank(
            local_sources=parse_indexed(
                data["LCL"], AudioPreampAccessibleSourceCodec.decode
            ),
            aux_sources=parse_indexed(
                data["AUX"], AudioPhaseInvertibleSourceCodec.decode
            ),
            aes50_a_sources=parse_indexed(
                data["A"], AudioPreampAccessibleSourceCodec.decode
            ),
            aes50_b_sources=parse_indexed(
                data["B"], AudioPreampAccessibleSourceCodec.decode
            ),
            aes50_c_sources=parse_indexed(
                data["C"], AudioPreampAccessibleSourceCodec.decode
            ),
            stageconnect_sources=parse_indexed(
                data["SC"], AudioPhaseInvertibleSourceCodec.decode
            ),
            usb_sources=parse_indexed(
                data["USB"], AudioPhaseInvertibleSourceCodec.decode
            ),
            expansion_card_sources=parse_indexed(
                data["CRD"], AudioPhaseInvertibleSourceCodec.decode
            ),
            module_sources=parse_indexed(
                data["MOD"], AudioPhaseInvertibleSourceCodec.decode
            ),
            usb_playback_sources=parse_indexed(
                data["PLAY"], AudioPhaseInvertibleSourceCodec.decode
            ),
            aes3_sources=parse_indexed(
                data["AES"], AudioPhaseInvertibleSourceCodec.decode
            ),
            user_signal_sources=parse_indexed(
                {k: v for k, v in usr.items() if int(k) <= _USR_SPLIT},
                AudioUserSignalSourceCodec.decode,
            ),
            user_signal_patch_sources=parse_indexed(
                {str(int(k) - _USR_SPLIT): v
                 for k, v in usr.items() if int(k) > _USR_SPLIT},
                AudioUserSignalPatchSourceCodec.decode,
            ),
            oscillator_sources=parse_indexed(
                data["OSC"], AudioOscillatorSourceCodec.decode
            ),
        )

    @staticmethod
    def encode(obj: AudioSourceBank) -> dict:
        return {
            "LCL": encode_indexed(
                obj.local_sources, AudioPreampAccessibleSourceCodec.encode
            ),
            "AUX": encode_indexed(
                obj.aux_sources, AudioPhaseInvertibleSourceCodec.encode
            ),
            "A": encode_indexed(
                obj.aes50_a_sources, AudioPreampAccessibleSourceCodec.encode
            ),
            "B": encode_indexed(
                obj.aes50_b_sources, AudioPreampAccessibleSourceCodec.encode
            ),
            "C": encode_indexed(
                obj.aes50_c_sources, AudioPreampAccessibleSourceCodec.encode
            ),
            "SC": encode_indexed(
                obj.stageconnect_sources, AudioPhaseInvertibleSourceCodec.encode
            ),
            "USB": encode_indexed(
                obj.usb_sources, AudioPhaseInvertibleSourceCodec.encode
            ),
            "CRD": encode_indexed(
                obj.expansion_card_sources, AudioPhaseInvertibleSourceCodec.encode
            ),
            "MOD": encode_indexed(
                obj.module_sources, AudioPhaseInvertibleSourceCodec.encode
            ),
            "PLAY": encode_indexed(
                obj.usb_playback_sources, AudioPhaseInvertibleSourceCodec.encode
            ),
            "AES": encode_indexed(
                obj.aes3_sources, AudioPhaseInvertibleSourceCodec.encode
            ),
            "USR": {
                **encode_indexed(
                    obj.user_signal_sources, AudioUserSignalSourceCodec.encode
                ),
                **encode_indexed(
                    obj.user_signal_patch_sources,
                    AudioUserSignalPatchSourceCodec.encode,
                    offset=_USR_SPLIT,
                ),
            },
            "OSC": encode_indexed(
                obj.oscillator_sources, AudioOscillatorSourceCodec.encode
            ),
        }
