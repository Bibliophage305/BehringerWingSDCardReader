import msgspec

from wing_snapfile.types.one_indexed_list import OneIndexedList
from wing_snapfile.models.audio.monitor import AudioMonitor


class AudioSoloConfig(msgspec.Struct, kw_only=True):
    mode: str
    monitor_outputs: str
    mute: bool

    channel_tap: str
    bus_tap: str
    main_tap: str
    matrix_tap: str

    source_solo: str


class AudioRTAConfig(msgspec.Struct, kw_only=True):
    rta_range: int
    rta_gain: int
    rta_autogain: bool

    eq_decay: str
    eq_detector: str
    eq_range: int
    eq_gain: int
    eq_autogain: bool


class AudioMeterTapPoints(msgspec.Struct, kw_only=True):
    channel_tap: str
    bus_tap: str
    main_tap: str
    matrix_tap: str
    dca_tap: str


class AudioMeterConfig(msgspec.Struct, kw_only=True):
    scope_source: int
    scope_tap_point: str

    surface_meter_tap_points: AudioMeterTapPoints
    meter_page_tap_points: AudioMeterTapPoints

    main_meter_source: str
    main_meter_position: str


class AudioTalkbackAssignments(msgspec.Struct, kw_only=True):
    mode: str

    monitor_dim: int
    bus_dim: int

    individual_send_levels: bool

    bus_assignments: OneIndexedList[bool]
    matrix_assignments: OneIndexedList[bool]
    main_assignments: OneIndexedList[bool]


class AudioTalkbackConfig(msgspec.Struct, kw_only=True):
    assign: str
    fader_level: float

    talkback_a: AudioTalkbackAssignments
    talkback_b: AudioTalkbackAssignments


class AudioAutomixConfig(msgspec.Struct, kw_only=True):
    x_enable: bool
    y_enable: bool


class AudioConfig(msgspec.Struct, kw_only=True):
    mainlink: str
    dcamgrp: bool

    mon: OneIndexedList[AudioMonitor]

    solo: AudioSoloConfig
    rta: AudioRTAConfig
    mtr: AudioMeterConfig
    talk: AudioTalkbackConfig
    amix: AudioAutomixConfig