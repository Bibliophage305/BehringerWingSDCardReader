from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

from wing_snapfile.types.one_indexed_list import OneIndexedList


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

    def to_dict(self):
        return {
            "mode": self.mode,
            "mute": self.mute,
            "col": self.color,
            "name": self.name,
            "icon": self.icon,
            "tags": self.tags,
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

    def to_dict(self):
        return {
            **super().to_dict(),
            "pol": self.phase_invert,
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

    def to_dict(self):
        return {
            **super().to_dict(),
            "g": self.gain,
            "vph": self.phantom_power,
            "rmt": self.remote_control,
            "rcvc": self.link_customization_to_source,
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

    def to_dict(self):
        return {
            "lvl": self.level,
            "mode": self.mode,
            "f": self.frequency,
        }


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

    def to_dict(self):
        return {
            **super().to_dict(),
            "osc": self.oscillator_settings.to_dict(),
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

    def to_dict(self):
        return {
            "grp": self.group,
            "in": self.input,
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

    def to_dict(self):
        return {
            **super().to_dict(),
            "tap": self.tap_point,
            "lr": self.lr_mode,
        }


@dataclass_validate
@dataclass
class AudioUserSignalSource(AudioPhaseInvertibleSource):
    user_signal_settings: AudioUserSignalFullSettings

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioPhaseInvertibleSource._from_dict_kwargs(data),
            "user_signal_settings": AudioUserSignalFullSettings.from_dict(data["user"]),
        }

    def to_dict(self):
        return {
            **super().to_dict(),
            "user": self.user_signal_settings.to_dict(),
        }


@dataclass_validate
@dataclass
class AudioUserSignalPatchSource(AudioPhaseInvertibleSource):
    user_signal_settings: AudioUserSignalSettings

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioPhaseInvertibleSource._from_dict_kwargs(data),
            "user_signal_settings": AudioUserSignalSettings.from_dict(data["user"]),
        }

    def to_dict(self):
        return {
            **super().to_dict(),
            "user": self.user_signal_settings.to_dict(),
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

    def to_dict(self):
        return {
            "LCL": self.local_sources.to_dict(),
            "AUX": self.aux_sources.to_dict(),
            "A": self.aes50_a_sources.to_dict(),
            "B": self.aes50_b_sources.to_dict(),
            "C": self.aes50_c_sources.to_dict(),
            "SC": self.stageconnect_sources.to_dict(),
            "USB": self.usb_sources.to_dict(),
            "CRD": self.expansion_card_sources.to_dict(),
            "MOD": self.module_sources.to_dict(),
            "PLAY": self.usb_playback_sources.to_dict(),
            "AES": self.aes3_sources.to_dict(),
            "USR": {
                **self.user_signal_sources.to_dict(),
                **self.user_signal_patch_sources.to_dict(offset=24),
            },
            "OSC": self.oscillator_sources.to_dict(),
        }
