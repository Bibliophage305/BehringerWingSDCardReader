from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

from wing_snapfile.types.one_indexed_list import OneIndexedList
from wing_snapfile.models.audio.dynamics_crossover import DynamicsCrossover
from wing_snapfile.models.audio.dynamics_sidechain import DynamicsSidechain
from wing_snapfile.models.audio.eq_block import EQBlock
from wing_snapfile.models.audio.input import (
    Input,
    FullInput,
)
from wing_snapfile.models.audio.filter import Filter
from wing_snapfile.models.audio.tap_eq import TapEQ
from wing_snapfile.models.audio.gate_sidechain import GateSidechain
from wing_snapfile.models.audio.dynamics_block import DynamicsBlock
from wing_snapfile.models.audio.pre_insert_block import PreInsertBlock
from wing_snapfile.models.audio.post_insert_block import (
    PostInsertBlock,
    PostInsertBlockWithAutomix,
)
from wing_snapfile.models.audio.send import FullSend, Send


@dataclass_validate
@dataclass(kw_only=True)
class DelaySettings:
    on: bool
    delay_mode: str
    delay_amount: float


@dataclass_validate
@dataclass(kw_only=True)
class DirectInput:
    direct_input: bool
    fader_level: float
    phase_invert: bool
    input_selector: str


@dataclass_validate
@dataclass(kw_only=True)
class Channel:
    color: int
    name: str
    icon: int
    led_on: bool
    mute_on: bool
    fader_level: float
    pan: int
    width: int
    monitor_mode: str
    eq_block: EQBlock
    dynamics_block: DynamicsBlock
    pre_insert_block: PreInsertBlock
    tags: list[str]


@dataclass_validate
@dataclass(kw_only=True)
class BusChannel(Channel):
    input: Input
    bus_sends: OneIndexedList[Send]
    matrix_sends: OneIndexedList[Send]
    main_sends: OneIndexedList[Send]
    dynamics_sidechain: DynamicsSidechain
    dynamics_crossover: DynamicsCrossover
    post_insert_block: PostInsertBlock
    delay_settings: DelaySettings
    mono_bus: bool


@dataclass_validate
@dataclass(kw_only=True)
class MatrixChannel(Channel):
    input: Input
    dynamics_sidechain: DynamicsSidechain
    dynamics_crossover: DynamicsCrossover
    post_insert_block: PostInsertBlock
    delay_settings: DelaySettings
    direct_input_settings: DirectInput
    mono_bus: bool


@dataclass_validate
@dataclass(kw_only=True)
class MainChannel(Channel):
    input: Input
    bus_sends: OneIndexedList[Send]
    matrix_sends: OneIndexedList[Send]
    dynamics_sidechain: DynamicsSidechain
    dynamics_crossover: DynamicsCrossover
    post_insert_block: PostInsertBlock
    delay_settings: DelaySettings
    mono_bus: bool


@dataclass_validate
@dataclass(kw_only=True)
class AuxChannel(Channel):
    input: FullInput
    link_customization_to_source: bool
    solo_safe: bool
    bus_sends: OneIndexedList[FullSend]
    matrix_sends: OneIndexedList[FullSend]
    main_sends: OneIndexedList[Send]
    dynamics_sidechain: DynamicsSidechain


@dataclass_validate
@dataclass(kw_only=True)
class FullChannel(Channel):
    input: FullInput
    link_customization_to_source: bool
    solo_safe: bool
    dynamics_sidechain: DynamicsSidechain
    dynamics_crossover: DynamicsCrossover
    post_insert_block: PostInsertBlockWithAutomix
    bus_sends: OneIndexedList[FullSend]
    matrix_sends: OneIndexedList[FullSend]
    main_sends: OneIndexedList[Send]
    filter: Filter
    processing_order: str
    processing_tap_point: str
    tap_eq: TapEQ
    gate_block: DynamicsBlock
    gate_sidechain: GateSidechain
    tap_width: int