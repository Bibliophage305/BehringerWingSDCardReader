from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

from wing_snapfile.types.one_indexed_list import OneIndexedList
from wing_snapfile.models.audio.monitor import Monitor


@dataclass_validate
@dataclass(kw_only=True)
class SoloConfig:
    mode: str
    monitor_outputs: str
    mute: bool

    channel_tap: str
    bus_tap: str
    main_tap: str
    matrix_tap: str

    source_solo: str


@dataclass_validate
@dataclass(kw_only=True)
class RTAConfig:
    rta_range: int
    rta_gain: int
    rta_autogain: bool

    eq_decay: str
    eq_detector: str
    eq_range: int
    eq_gain: int
    eq_autogain: bool


@dataclass_validate
@dataclass(kw_only=True)
class MeterTapPoints:
    channel_tap: str
    bus_tap: str
    main_tap: str
    matrix_tap: str
    dca_tap: str


@dataclass_validate
@dataclass(kw_only=True)
class MeterConfig:
    scope_source: int
    scope_tap_point: str

    surface_meter_tap_points: MeterTapPoints
    meter_page_tap_points: MeterTapPoints

    main_meter_source: str
    main_meter_position: str


@dataclass_validate
@dataclass(kw_only=True)
class TalkbackAssignments:
    mode: str

    monitor_dim: int
    bus_dim: int

    individual_send_levels: bool

    bus_assignments: OneIndexedList[bool]
    matrix_assignments: OneIndexedList[bool]
    main_assignments: OneIndexedList[bool]


@dataclass_validate
@dataclass(kw_only=True)
class TalkbackConfig:
    assign: str
    fader_level: float

    talkback_a: TalkbackAssignments
    talkback_b: TalkbackAssignments


@dataclass_validate
@dataclass(kw_only=True)
class AutomixConfig:
    x_enable: bool
    y_enable: bool


@dataclass_validate
@dataclass(kw_only=True)
class AudioConfig:
    mainlink: str
    dcamgrp: bool

    mon: OneIndexedList[Monitor]

    solo: SoloConfig
    rta: RTAConfig
    mtr: MeterConfig
    talk: TalkbackConfig
    amix: AutomixConfig