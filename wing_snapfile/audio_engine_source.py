from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

from .types import OneIndexedList


@dataclass_validate
@dataclass
class AudioEngineSource:
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
class AudioEnginePhaseInvertibleSource(AudioEngineSource):
    phase_invert: bool

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioEngineSource._from_dict_kwargs(data),
            "phase_invert": data["pol"],
        }


@dataclass_validate
@dataclass
class AudioEnginePreampAccessibleSource(AudioEnginePhaseInvertibleSource):
    gain: float
    phantom_power: bool
    remote_control: str
    link_customization_to_source: bool

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioEnginePhaseInvertibleSource._from_dict_kwargs(data),
            "gain": float(data["g"]),
            "phantom_power": data["vph"],
            "remote_control": data["rmt"],
            "link_customization_to_source": data["rcvc"],
        }


@dataclass_validate
@dataclass
class AudioEngineOscillatorSettings:
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
class AudioEngineOscillatorSource(AudioEngineSource):
    oscillator_settings: AudioEngineOscillatorSettings

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioEngineSource._from_dict_kwargs(data),
            "oscillator_settings": AudioEngineOscillatorSettings.from_dict(data["osc"]),
        }


@dataclass_validate
@dataclass
class AudioEngineUserSignalSettings:
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
class AudioEngineUserSignalFullSettings(AudioEngineUserSignalSettings):
    tap_point: str
    lr_mode: str

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioEngineUserSignalSettings._from_dict_kwargs(data),
            "tap_point": data["tap"],
            "lr_mode": data["lr"],
        }


@dataclass_validate
@dataclass
class AudioEngineUserSignalSource(AudioEnginePhaseInvertibleSource):
    user_signal_settings: AudioEngineUserSignalFullSettings

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioEnginePhaseInvertibleSource._from_dict_kwargs(data),
            "user_signal_settings": AudioEngineUserSignalFullSettings.from_dict(
                data["user"]
            ),
        }


@dataclass_validate
@dataclass
class AudioEngineUserSignalPatchSource(AudioEnginePhaseInvertibleSource):
    user_signal_settings: AudioEngineUserSignalSettings

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioEnginePhaseInvertibleSource._from_dict_kwargs(data),
            "user_signal_settings": AudioEngineUserSignalSettings.from_dict(
                data["user"]
            ),
        }


@dataclass_validate
@dataclass
class AudioEngineSourceBank:
    local_sources: OneIndexedList[AudioEnginePreampAccessibleSource]
    aux_sources: OneIndexedList[AudioEnginePhaseInvertibleSource]
    aes50_a_sources: OneIndexedList[AudioEnginePreampAccessibleSource]
    aes50_b_sources: OneIndexedList[AudioEnginePreampAccessibleSource]
    aes50_c_sources: OneIndexedList[AudioEnginePreampAccessibleSource]
    stageconnect_sources: OneIndexedList[AudioEnginePhaseInvertibleSource]
    usb_sources: OneIndexedList[AudioEnginePhaseInvertibleSource]
    expansion_card_sources: OneIndexedList[AudioEnginePhaseInvertibleSource]
    module_sources: OneIndexedList[AudioEnginePhaseInvertibleSource]
    usb_playback_sources: OneIndexedList[AudioEnginePhaseInvertibleSource]
    aes3_sources: OneIndexedList[AudioEnginePhaseInvertibleSource]
    user_signal_sources: OneIndexedList[AudioEngineUserSignalSource]
    user_signal_patch_sources: OneIndexedList[AudioEngineUserSignalPatchSource]
    oscillator_sources: OneIndexedList[AudioEngineOscillatorSource]

    @classmethod
    def from_dict(cls, data):
        return cls(
            local_sources=OneIndexedList.from_indexed_dict(
                data["LCL"], AudioEnginePreampAccessibleSource.from_dict
            ),
            aux_sources=OneIndexedList.from_indexed_dict(
                data["AUX"], AudioEnginePhaseInvertibleSource.from_dict
            ),
            aes50_a_sources=OneIndexedList.from_indexed_dict(
                data["A"], AudioEnginePreampAccessibleSource.from_dict
            ),
            aes50_b_sources=OneIndexedList.from_indexed_dict(
                data["B"], AudioEnginePreampAccessibleSource.from_dict
            ),
            aes50_c_sources=OneIndexedList.from_indexed_dict(
                data["C"], AudioEnginePreampAccessibleSource.from_dict
            ),
            stageconnect_sources=OneIndexedList.from_indexed_dict(
                data["SC"], AudioEnginePhaseInvertibleSource.from_dict
            ),
            usb_sources=OneIndexedList.from_indexed_dict(
                data["USB"], AudioEnginePhaseInvertibleSource.from_dict
            ),
            expansion_card_sources=OneIndexedList.from_indexed_dict(
                data["CRD"], AudioEnginePhaseInvertibleSource.from_dict
            ),
            module_sources=OneIndexedList.from_indexed_dict(
                data["MOD"], AudioEnginePhaseInvertibleSource.from_dict
            ),
            usb_playback_sources=OneIndexedList.from_indexed_dict(
                data["PLAY"], AudioEnginePhaseInvertibleSource.from_dict
            ),
            aes3_sources=OneIndexedList.from_indexed_dict(
                data["AES"], AudioEnginePhaseInvertibleSource.from_dict
            ),
            user_signal_sources=OneIndexedList.from_indexed_dict(
                {k: v for k, v in data["USR"].items() if int(k) <= 24},
                AudioEngineUserSignalSource.from_dict,
            ),
            user_signal_patch_sources=OneIndexedList.from_indexed_dict(
                {str(int(k) - 24): v for k, v in data["USR"].items() if int(k) > 24},
                AudioEngineUserSignalPatchSource.from_dict,
            ),
            oscillator_sources=OneIndexedList.from_indexed_dict(
                data["OSC"], AudioEngineOscillatorSource.from_dict
            ),
        )
