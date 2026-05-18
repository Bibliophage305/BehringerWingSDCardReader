from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

from wing_snapfile.types import OneIndexedList


@dataclass_validate
@dataclass
class AudioSource:
    mode: str
    mute: bool
    color: int
    name: str
    icon: int
    tags: list[str]

    @classmethod
    def from_dict(cls, data):
        return cls(**cls._from_dict_kwargs(data))

    @classmethod
    def _from_dict_kwargs(cls, data: dict[str, object]) -> dict[str, object]:
        return {
            "mode": data["mode"],
            "mute": data["mute"],
            "color": data["col"],
            "name": data["name"],
            "icon": data["icon"],
            "tags": data["tags"],
        }


@dataclass_validate
@dataclass
class AudioPhaseInvertibleSource(AudioSource):
    phase_invert: bool

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioSource._from_dict_kwargs(data),
            "phase_invert": data["pol"],
        }


@dataclass_validate
@dataclass
class AudioPreampAccessibleSource(AudioPhaseInvertibleSource):
    gain: float
    phantom_power: bool
    remote_control: str
    link_customization_to_source: bool

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioPhaseInvertibleSource._from_dict_kwargs(data),
            "gain": float(data["g"]),
            "phantom_power": data["vph"],
            "remote_control": data["rmt"],
            "link_customization_to_source": data["rcvc"],
        }


@dataclass_validate
@dataclass
class AudioOscillatorSettings:
    level: float
    mode: str
    frequency: float

    @classmethod
    def from_dict(cls, data):
        return cls(
            level=float(data["lvl"]),
            mode=data["mode"],
            frequency=float(data["f"]),
        )


@dataclass_validate
@dataclass
class AudioOscillatorSource(AudioSource):
    oscillator_settings: AudioOscillatorSettings

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioSource._from_dict_kwargs(data),
            "oscillator_settings": AudioOscillatorSettings.from_dict(data["osc"]),
        }


@dataclass_validate
@dataclass
class AudioUserSignalSettings:
    group: str
    input: int

    @classmethod
    def from_dict(cls, data):
        return cls(**cls._from_dict_kwargs(data))

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            "group": data["grp"],
            "input": data["in"],
        }


@dataclass_validate
@dataclass
class AudioUserSignalFullSettings(AudioUserSignalSettings):
    tap_point: str
    lr_mode: str

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioUserSignalSettings._from_dict_kwargs(data),
            "tap_point": data["tap"],
            "lr_mode": data["lr"],
        }


@dataclass_validate
@dataclass
class AudioUserSignalSource(AudioPhaseInvertibleSource):
    user_signal_settings: AudioUserSignalFullSettings

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioPhaseInvertibleSource._from_dict_kwargs(data),
            "user_signal_settings": AudioUserSignalFullSettings.from_dict(
                data["user"]
            ),
        }


@dataclass_validate
@dataclass
class AudioUserSignalPatchSource(AudioPhaseInvertibleSource):
    user_signal_settings: AudioUserSignalSettings

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioPhaseInvertibleSource._from_dict_kwargs(data),
            "user_signal_settings": AudioUserSignalSettings.from_dict(
                data["user"]
            ),
        }


@dataclass_validate
@dataclass
class AudioSourceBank:
    local_sources: OneIndexedList[AudioPreampAccessibleSource]
    aux_sources: OneIndexedList[AudioPhaseInvertibleSource]
    aes50_a_sources: OneIndexedList[AudioPreampAccessibleSource]
    aes50_b_sources: OneIndexedList[AudioPreampAccessibleSource]
    aes50_c_sources: OneIndexedList[AudioPreampAccessibleSource]
    stageconnect_sources: OneIndexedList[AudioPhaseInvertibleSource]
    usb_sources: OneIndexedList[AudioPhaseInvertibleSource]
    expansion_card_sources: OneIndexedList[AudioPhaseInvertibleSource]
    module_sources: OneIndexedList[AudioPhaseInvertibleSource]
    usb_playback_sources: OneIndexedList[AudioPhaseInvertibleSource]
    aes3_sources: OneIndexedList[AudioPhaseInvertibleSource]
    user_signal_sources: OneIndexedList[AudioUserSignalSource]
    user_signal_patch_sources: OneIndexedList[AudioUserSignalPatchSource]
    oscillator_sources: OneIndexedList[AudioOscillatorSource]

    @classmethod
    def from_dict(cls, data):
        return cls(
            local_sources=OneIndexedList.from_indexed_dict(
                data["LCL"], AudioPreampAccessibleSource.from_dict
            ),
            aux_sources=OneIndexedList.from_indexed_dict(
                data["AUX"], AudioPhaseInvertibleSource.from_dict
            ),
            aes50_a_sources=OneIndexedList.from_indexed_dict(
                data["A"], AudioPreampAccessibleSource.from_dict
            ),
            aes50_b_sources=OneIndexedList.from_indexed_dict(
                data["B"], AudioPreampAccessibleSource.from_dict
            ),
            aes50_c_sources=OneIndexedList.from_indexed_dict(
                data["C"], AudioPreampAccessibleSource.from_dict
            ),
            stageconnect_sources=OneIndexedList.from_indexed_dict(
                data["SC"], AudioPhaseInvertibleSource.from_dict
            ),
            usb_sources=OneIndexedList.from_indexed_dict(
                data["USB"], AudioPhaseInvertibleSource.from_dict
            ),
            expansion_card_sources=OneIndexedList.from_indexed_dict(
                data["CRD"], AudioPhaseInvertibleSource.from_dict
            ),
            module_sources=OneIndexedList.from_indexed_dict(
                data["MOD"], AudioPhaseInvertibleSource.from_dict
            ),
            usb_playback_sources=OneIndexedList.from_indexed_dict(
                data["PLAY"], AudioPhaseInvertibleSource.from_dict
            ),
            aes3_sources=OneIndexedList.from_indexed_dict(
                data["AES"], AudioPhaseInvertibleSource.from_dict
            ),
            user_signal_sources=OneIndexedList.from_indexed_dict(
                {k: v for k, v in data["USR"].items() if int(k) <= 24},
                AudioUserSignalSource.from_dict,
            ),
            user_signal_patch_sources=OneIndexedList.from_indexed_dict(
                {str(int(k) - 24): v for k, v in data["USR"].items() if int(k) > 24},
                AudioUserSignalPatchSource.from_dict,
            ),
            oscillator_sources=OneIndexedList.from_indexed_dict(
                data["OSC"], AudioOscillatorSource.from_dict
            ),
        )
