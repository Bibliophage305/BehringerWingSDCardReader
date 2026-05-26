import msgspec

from wing_snapfile.types.one_indexed_list import OneIndexedList


class AudioSource(msgspec.Struct, kw_only=True):
    mode: str
    mute: bool
    color: int
    name: str
    icon: int
    tags: list[str]


class AudioPhaseInvertibleSource(AudioSource, kw_only=True):
    phase_invert: bool


class AudioPreampAccessibleSource(AudioPhaseInvertibleSource, kw_only=True):
    gain: float
    phantom_power: bool
    remote_control: str
    link_customization_to_source: bool


class AudioOscillatorSettings(msgspec.Struct, kw_only=True):
    level: float
    mode: str
    frequency: float


class AudioOscillatorSource(AudioSource, kw_only=True):
    oscillator_settings: AudioOscillatorSettings


class AudioUserSignalSettings(msgspec.Struct, kw_only=True):
    group: str
    input: int


class AudioUserSignalFullSettings(AudioUserSignalSettings, kw_only=True):
    tap_point: str
    lr_mode: str


class AudioUserSignalSource(AudioPhaseInvertibleSource, kw_only=True):
    user_signal_settings: AudioUserSignalFullSettings


class AudioUserSignalPatchSource(AudioPhaseInvertibleSource, kw_only=True):
    user_signal_settings: AudioUserSignalSettings


class AudioSourceBank(msgspec.Struct, kw_only=True):
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
