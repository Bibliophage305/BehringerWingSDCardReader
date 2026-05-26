import msgspec

from wing_snapfile.types.one_indexed_list import OneIndexedList
from wing_snapfile.models.audio.dynamics_crossover import AudioDynamicsCrossover
from wing_snapfile.models.audio.dynamics_sidechain import AudioDynamicsSidechain
from wing_snapfile.models.audio.eq import AudioEQ
from wing_snapfile.models.audio.input import (
    AudioInput,
    AudioRoutableInput,
    AudioSourceSwitchableDelayableInput,
)
from wing_snapfile.models.audio.filter import AudioFilter
from wing_snapfile.models.audio.tap_eq import AudioTapEQ
from wing_snapfile.models.audio.gate_sidechain import AudioGateSidechain
from wing_snapfile.models.audio.dynamics import AudioDynamics
from wing_snapfile.models.audio.pre_insert_plugin import AudioPreInsertPlugin
from wing_snapfile.models.audio.post_insert_plugin import (
    AudioPostInsertPlugin,
    AudioPostInsertPluginWithAutomix,
)
from wing_snapfile.models.audio.send import AudioFullSend, AudioLimitedSend


class DelaySettings(msgspec.Struct, kw_only=True):
    on: bool
    delay_mode: str
    delay_amount: float


class AudioDirectInput(msgspec.Struct, kw_only=True):
    direct_input: bool
    fader_level: float
    phase_invert: bool
    input_selector: str


class AudioChannel(msgspec.Struct, kw_only=True):
    """Fields common to all channel types. Does not declare `input` —
    each concrete subclass declares it with the appropriate type."""
    color: int
    name: str
    icon: int
    led_on: bool
    mute_on: bool
    fader_level: float
    pan: int
    width: int
    monitor_mode: str
    eq_plugin: AudioEQ
    dynamics_plugin: AudioDynamics
    pre_insert_plugin: AudioPreInsertPlugin
    tags: list[str]


class AudioBusChannel(AudioChannel, kw_only=True):
    input: AudioInput
    bus_sends: OneIndexedList[AudioLimitedSend]
    matrix_sends: OneIndexedList[AudioLimitedSend]
    main_sends: OneIndexedList[AudioLimitedSend]
    dynamics_sidechain: AudioDynamicsSidechain
    dynamics_crossover: AudioDynamicsCrossover
    post_insert_plugin: AudioPostInsertPlugin
    delay_settings: DelaySettings
    mono_bus: bool


class AudioMatrixChannel(AudioChannel, kw_only=True):
    input: AudioInput
    dynamics_sidechain: AudioDynamicsSidechain
    dynamics_crossover: AudioDynamicsCrossover
    post_insert_plugin: AudioPostInsertPlugin
    delay_settings: DelaySettings
    direct_input_settings: AudioDirectInput
    mono_bus: bool


class AudioMainChannel(AudioChannel, kw_only=True):
    input: AudioInput
    bus_sends: OneIndexedList[AudioLimitedSend]
    matrix_sends: OneIndexedList[AudioLimitedSend]
    dynamics_sidechain: AudioDynamicsSidechain
    dynamics_crossover: AudioDynamicsCrossover
    post_insert_plugin: AudioPostInsertPlugin
    delay_settings: DelaySettings
    mono_bus: bool


class AudioAuxChannel(AudioChannel, kw_only=True):
    input: AudioSourceSwitchableDelayableInput
    link_customization_to_source: bool
    solo_safe: bool
    bus_sends: OneIndexedList[AudioFullSend]
    matrix_sends: OneIndexedList[AudioFullSend]
    main_sends: OneIndexedList[AudioLimitedSend]
    dynamics_sidechain: AudioDynamicsSidechain


class AudioFullChannel(AudioChannel, kw_only=True):
    input: AudioSourceSwitchableDelayableInput
    link_customization_to_source: bool
    solo_safe: bool
    dynamics_sidechain: AudioDynamicsSidechain
    dynamics_crossover: AudioDynamicsCrossover
    post_insert_plugin: AudioPostInsertPluginWithAutomix
    bus_sends: OneIndexedList[AudioFullSend]
    matrix_sends: OneIndexedList[AudioFullSend]
    main_sends: OneIndexedList[AudioLimitedSend]
    filter: AudioFilter
    processing_order: str
    processing_tap_point: str
    tap_eq: AudioTapEQ
    gate_plugin: AudioDynamics
    gate_sidechain: AudioGateSidechain
    tap_width: int