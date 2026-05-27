from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

from wing_snapfile.types.one_indexed_list import OneIndexedList


@dataclass_validate
@dataclass(kw_only=True)
class Source:
    mode: str
    mute: bool
    color: int
    name: str
    icon: int
    tags: list[str]


@dataclass_validate
@dataclass(kw_only=True)
class PhaseInvertibleSource(Source):
    phase_invert: bool


@dataclass_validate
@dataclass(kw_only=True)
class PreampAccessibleSource(PhaseInvertibleSource):
    gain: float
    phantom_power: bool
    remote_control: str
    link_customization_to_source: bool


@dataclass_validate
@dataclass(kw_only=True)
class OscillatorSettings:
    level: float
    mode: str
    frequency: float


@dataclass_validate
@dataclass(kw_only=True)
class OscillatorSource(Source):
    oscillator_settings: OscillatorSettings


@dataclass_validate
@dataclass(kw_only=True)
class UserSignalSettings:
    group: str
    input: int


@dataclass_validate
@dataclass(kw_only=True)
class UserSignalFullSettings(UserSignalSettings):
    tap_point: str
    lr_mode: str


@dataclass_validate
@dataclass(kw_only=True)
class UserSignalSource(PhaseInvertibleSource):
    user_signal_settings: UserSignalFullSettings


@dataclass_validate
@dataclass(kw_only=True)
class UserSignalPatchSource(PhaseInvertibleSource):
    user_signal_settings: UserSignalSettings


@dataclass_validate
@dataclass(kw_only=True)
class SourceBank:
    local_sources: OneIndexedList[PreampAccessibleSource]
    aux_sources: OneIndexedList[PhaseInvertibleSource]
    aes50_a_sources: OneIndexedList[PreampAccessibleSource]
    aes50_b_sources: OneIndexedList[PreampAccessibleSource]
    aes50_c_sources: OneIndexedList[PreampAccessibleSource]
    stageconnect_sources: OneIndexedList[PhaseInvertibleSource]
    usb_sources: OneIndexedList[PhaseInvertibleSource]
    expansion_card_sources: OneIndexedList[PhaseInvertibleSource]
    module_sources: OneIndexedList[PhaseInvertibleSource]
    usb_playback_sources: OneIndexedList[PhaseInvertibleSource]
    aes3_sources: OneIndexedList[PhaseInvertibleSource]
    user_signal_sources: OneIndexedList[UserSignalSource]
    user_signal_patch_sources: OneIndexedList[UserSignalPatchSource]
    oscillator_sources: OneIndexedList[OscillatorSource]
