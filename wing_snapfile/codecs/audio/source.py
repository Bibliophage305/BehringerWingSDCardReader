from wing_snapfile.models.audio.source import (
    Source,
    PhaseInvertibleSource,
    PreampAccessibleSource,
    OscillatorSettings,
    OscillatorSource,
    UserSignalSettings,
    UserSignalFullSettings,
    UserSignalSource,
    UserSignalPatchSource,
    SourceBank,
)
from wing_snapfile.helpers.indexed import encode_one_indexed_list, decode_one_indexed_list


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


def _encode_source_base(obj: Source) -> dict:
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


def _encode_phase_invertible(obj: PhaseInvertibleSource) -> dict:
    return {
        **_encode_source_base(obj),
        "pol": obj.phase_invert,
    }


# ---------------------------------------------------------------------------
# Leaf codecs
# ---------------------------------------------------------------------------

class PreampAccessibleSourceCodec:
    @staticmethod
    def decode(data: dict) -> PreampAccessibleSource:
        return PreampAccessibleSource(
            **_decode_phase_invertible(data),
            gain=float(data["g"]),
            phantom_power=data["vph"],
            remote_control=data["rmt"],
            link_customization_to_source=data["rcvc"],
        )

    @staticmethod
    def encode(obj: PreampAccessibleSource) -> dict:
        return {
            **_encode_phase_invertible(obj),
            "g": obj.gain,
            "vph": obj.phantom_power,
            "rmt": obj.remote_control,
            "rcvc": obj.link_customization_to_source,
        }


class PhaseInvertibleSourceCodec:
    @staticmethod
    def decode(data: dict) -> PhaseInvertibleSource:
        return PhaseInvertibleSource(**_decode_phase_invertible(data))

    @staticmethod
    def encode(obj: PhaseInvertibleSource) -> dict:
        return _encode_phase_invertible(obj)


class OscillatorSettingsCodec:
    @staticmethod
    def decode(data: dict) -> OscillatorSettings:
        return OscillatorSettings(
            level=float(data["lvl"]),
            mode=data["mode"],
            frequency=float(data["f"]),
        )

    @staticmethod
    def encode(obj: OscillatorSettings) -> dict:
        return {
            "lvl": obj.level,
            "mode": obj.mode,
            "f": obj.frequency,
        }


class OscillatorSourceCodec:
    @staticmethod
    def decode(data: dict) -> OscillatorSource:
        return OscillatorSource(
            **_decode_source_base(data),
            oscillator_settings=OscillatorSettingsCodec.decode(data["osc"]),
        )

    @staticmethod
    def encode(obj: OscillatorSource) -> dict:
        return {
            **_encode_source_base(obj),
            "osc": OscillatorSettingsCodec.encode(obj.oscillator_settings),
        }


class UserSignalSettingsCodec:
    @staticmethod
    def decode(data: dict) -> UserSignalSettings:
        return UserSignalSettings(
            group=data["grp"],
            input=data["in"],
        )

    @staticmethod
    def encode(obj: UserSignalSettings) -> dict:
        return {
            "grp": obj.group,
            "in": obj.input,
        }


class UserSignalFullSettingsCodec:
    @staticmethod
    def decode(data: dict) -> UserSignalFullSettings:
        return UserSignalFullSettings(
            group=data["grp"],
            input=data["in"],
            tap_point=data["tap"],
            lr_mode=data["lr"],
        )

    @staticmethod
    def encode(obj: UserSignalFullSettings) -> dict:
        return {
            "grp": obj.group,
            "in": obj.input,
            "tap": obj.tap_point,
            "lr": obj.lr_mode,
        }


class UserSignalSourceCodec:
    @staticmethod
    def decode(data: dict) -> UserSignalSource:
        return UserSignalSource(
            **_decode_phase_invertible(data),
            user_signal_settings=UserSignalFullSettingsCodec.decode(data["user"]),
        )

    @staticmethod
    def encode(obj: UserSignalSource) -> dict:
        return {
            **_encode_phase_invertible(obj),
            "user": UserSignalFullSettingsCodec.encode(obj.user_signal_settings),
        }


class UserSignalPatchSourceCodec:
    @staticmethod
    def decode(data: dict) -> UserSignalPatchSource:
        return UserSignalPatchSource(
            **_decode_phase_invertible(data),
            user_signal_settings=UserSignalSettingsCodec.decode(data["user"]),
        )

    @staticmethod
    def encode(obj: UserSignalPatchSource) -> dict:
        return {
            **_encode_phase_invertible(obj),
            "user": UserSignalSettingsCodec.encode(obj.user_signal_settings),
        }


# ---------------------------------------------------------------------------
# AudioSourceBank
# ---------------------------------------------------------------------------

_USR_SPLIT = 24  # indices 1-24 → UserSignal, 25+ → UserSignalPatch


class SourceBankCodec:
    @staticmethod
    def decode(data: dict) -> SourceBank:
        usr = data["USR"]
        return SourceBank(
            local_sources=decode_one_indexed_list(
                data["LCL"], PreampAccessibleSourceCodec.decode
            ),
            aux_sources=decode_one_indexed_list(
                data["AUX"], PhaseInvertibleSourceCodec.decode
            ),
            aes50_a_sources=decode_one_indexed_list(
                data["A"], PreampAccessibleSourceCodec.decode
            ),
            aes50_b_sources=decode_one_indexed_list(
                data["B"], PreampAccessibleSourceCodec.decode
            ),
            aes50_c_sources=decode_one_indexed_list(
                data["C"], PreampAccessibleSourceCodec.decode
            ),
            stageconnect_sources=decode_one_indexed_list(
                data["SC"], PhaseInvertibleSourceCodec.decode
            ),
            usb_sources=decode_one_indexed_list(
                data["USB"], PhaseInvertibleSourceCodec.decode
            ),
            expansion_card_sources=decode_one_indexed_list(
                data["CRD"], PhaseInvertibleSourceCodec.decode
            ),
            module_sources=decode_one_indexed_list(
                data["MOD"], PhaseInvertibleSourceCodec.decode
            ),
            usb_playback_sources=decode_one_indexed_list(
                data["PLAY"], PhaseInvertibleSourceCodec.decode
            ),
            aes3_sources=decode_one_indexed_list(
                data["AES"], PhaseInvertibleSourceCodec.decode
            ),
            user_signal_sources=decode_one_indexed_list(
                {k: v for k, v in usr.items() if int(k) <= _USR_SPLIT},
                UserSignalSourceCodec.decode,
            ),
            user_signal_patch_sources=decode_one_indexed_list(
                {str(int(k) - _USR_SPLIT): v
                 for k, v in usr.items() if int(k) > _USR_SPLIT},
                UserSignalPatchSourceCodec.decode,
            ),
            oscillator_sources=decode_one_indexed_list(
                data["OSC"], OscillatorSourceCodec.decode
            ),
        )

    @staticmethod
    def encode(obj: SourceBank) -> dict:
        return {
            "LCL": encode_one_indexed_list(
                obj.local_sources, PreampAccessibleSourceCodec.encode
            ),
            "AUX": encode_one_indexed_list(
                obj.aux_sources, PhaseInvertibleSourceCodec.encode
            ),
            "A": encode_one_indexed_list(
                obj.aes50_a_sources, PreampAccessibleSourceCodec.encode
            ),
            "B": encode_one_indexed_list(
                obj.aes50_b_sources, PreampAccessibleSourceCodec.encode
            ),
            "C": encode_one_indexed_list(
                obj.aes50_c_sources, PreampAccessibleSourceCodec.encode
            ),
            "SC": encode_one_indexed_list(
                obj.stageconnect_sources, PhaseInvertibleSourceCodec.encode
            ),
            "USB": encode_one_indexed_list(
                obj.usb_sources, PhaseInvertibleSourceCodec.encode
            ),
            "CRD": encode_one_indexed_list(
                obj.expansion_card_sources, PhaseInvertibleSourceCodec.encode
            ),
            "MOD": encode_one_indexed_list(
                obj.module_sources, PhaseInvertibleSourceCodec.encode
            ),
            "PLAY": encode_one_indexed_list(
                obj.usb_playback_sources, PhaseInvertibleSourceCodec.encode
            ),
            "AES": encode_one_indexed_list(
                obj.aes3_sources, PhaseInvertibleSourceCodec.encode
            ),
            "USR": {
                **encode_one_indexed_list(
                    obj.user_signal_sources, UserSignalSourceCodec.encode
                ),
                **encode_one_indexed_list(
                    obj.user_signal_patch_sources,
                    UserSignalPatchSourceCodec.encode,
                    offset=_USR_SPLIT,
                ),
            },
            "OSC": encode_one_indexed_list(
                obj.oscillator_sources, OscillatorSourceCodec.encode
            ),
        }
