from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate
from wing_snapfile.types import OneIndexedList
from wing_snapfile.audio.monitor import AudioMonitor

@dataclass_validate
@dataclass
class AudioSoloConfig:
    mode: str
    monitor_outputs: str
    mute: bool
    channel_tap: str
    bus_tap: str
    main_tap: str
    matrix_tap: str
    source_solo: str
    
    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioSoloConfig":
        return AudioSoloConfig(
            mode=data["mode"],
            monitor_outputs=data["mon"],
            mute=data["mute"],
            channel_tap=data["chtap"],
            bus_tap=data["bustap"],
            main_tap=data["maintap"],
            matrix_tap=data["mtxtap"],
            source_solo=data["srcsolo"],
        )

@dataclass_validate
@dataclass
class AudioRTAConfig:
    rta_range: int
    rta_gain: int
    rta_autogain: bool
    eq_decay: str
    eq_detector: str
    eq_range: int
    eq_gain: int
    eq_autogain: bool

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioRTAConfig":
        return AudioRTAConfig(
            rta_range=data["rtarange"],
            rta_gain=data["rtagain"],
            rta_autogain=data["rtaauto"],
            eq_decay=data["eqdecay"],
            eq_detector=data["eqdet"],
            eq_range=data["eqrange"],
            eq_gain=data["eqgain"],
            eq_autogain=data["eqauto"],
        )

@dataclass_validate
@dataclass
class AudioMeterTapPoints:
    channel_tap: str
    bus_tap: str
    main_tap: str
    matrix_tap: str
    dca_tap: str

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioMeterTapPoints":
        return AudioMeterTapPoints(
            channel_tap=data["in"],
            bus_tap=data["bus"],
            main_tap=data["main"],
            matrix_tap=data["mtx"],
            dca_tap=data["dca"],
        )


@dataclass_validate
@dataclass
class AudioMeterConfig:
    scope_source: int
    scope_tap_point: str
    surface_meter_tap_points: AudioMeterTapPoints
    meter_page_tap_points: AudioMeterTapPoints
    main_meter_source: str
    main_meter_position: str

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioMeterConfig":
        return AudioMeterConfig(
            scope_source=data["scopesrc"],
            scope_tap_point=data["scopetap"],
            surface_meter_tap_points=AudioMeterTapPoints.from_dict(data["mtrsfc"]),
            meter_page_tap_points=AudioMeterTapPoints.from_dict(data["mtrpage"]),
            main_meter_source=data["mainmtr"],
            main_meter_position=data["mainpos"],
        )

@dataclass_validate
@dataclass
class AudioTalkbackAssignments:
    mode: str
    monitor_dim: int
    bus_dim: int
    bus_assignments: OneIndexedList[bool]
    matrix_assignments: OneIndexedList[bool]
    main_assignments: OneIndexedList[bool]

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioTalkbackAssignments":
        return AudioTalkbackAssignments(
            mode=data["mode"],
            monitor_dim=data["mondim"],
            bus_dim=data["busdim"],
            bus_assignments=OneIndexedList.from_indexed_dict(
                {k[1:]: v for k, v in data.items() if k.startswith("B") and k[1:].isdigit()}
            ),
            matrix_assignments=OneIndexedList.from_indexed_dict(
                {k[2:]: v for k, v in data.items() if k.startswith("MX") and k[2:].isdigit()}
            ),
            main_assignments=OneIndexedList.from_indexed_dict(
                {k[1:]: v for k, v in data.items() if k.startswith("M") and k[1:].isdigit()}
            ),
        )

@dataclass_validate
@dataclass
class AudioTalkbackConfig:
    assign: str
    fader_level: float
    talkback_a: AudioTalkbackAssignments
    talkback_b: AudioTalkbackAssignments

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioTalkbackConfig":
        return AudioTalkbackConfig(
            assign=data["assign"],
            fader_level=float(data["lvl"]),
            talkback_a=AudioTalkbackAssignments.from_dict(data["A"]),
            talkback_b=AudioTalkbackAssignments.from_dict(data["B"]),
        )

@dataclass_validate
@dataclass
class AudioAutomixConfig:
    x_enable: bool
    y_enable: bool

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioAutomixConfig":
        return AudioAutomixConfig(
            x_enable=data["x"],
            y_enable=data["y"],
        )


@dataclass_validate
@dataclass
class AudioConfig:
    mainlink: str
    dcamgrp: bool
    mon: OneIndexedList[AudioMonitor]
    solo: AudioSoloConfig
    rta: AudioRTAConfig
    mtr: AudioMeterConfig
    talk: AudioTalkbackConfig
    amix: AudioAutomixConfig

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioConfig":
        return AudioConfig(
            mainlink=data["mainlink"],
            dcamgrp=data["dcamgrp"],
            mon=OneIndexedList.from_indexed_dict(data["mon"], AudioMonitor.from_dict),
            solo=AudioSoloConfig.from_dict(data["solo"]),
            rta=AudioRTAConfig.from_dict(data["rta"]),
            mtr=AudioMeterConfig.from_dict(data["mtr"]),
            talk=AudioTalkbackConfig.from_dict(data["talk"]),
            amix=AudioAutomixConfig.from_dict(data["amix"]),
        )

