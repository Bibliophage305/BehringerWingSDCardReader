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

    def to_dict(self):
        return {
            "mode": self.mode,
            "mon": self.monitor_outputs,
            "mute": self.mute,
            "chtap": self.channel_tap,
            "bustap": self.bus_tap,
            "maintap": self.main_tap,
            "mtxtap": self.matrix_tap,
            "srcsolo": self.source_solo,
        }

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

    def to_dict(self):
        return {
            "rtarange": self.rta_range,
            "rtagain": self.rta_gain,
            "rtaauto": self.rta_autogain,
            "eqdecay": self.eq_decay,
            "eqdet": self.eq_detector,
            "eqrange": self.eq_range,
            "eqgain": self.eq_gain,
            "eqauto": self.eq_autogain,
        }

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
    
    def to_dict(self):
        return {
            "in": self.channel_tap,
            "bus": self.bus_tap,
            "main": self.main_tap,
            "mtx": self.matrix_tap,
            "dca": self.dca_tap,
        }


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

    def to_dict(self):
        return {
            "scopesrc": self.scope_source,
            "scopetap": self.scope_tap_point,
            "mtrsfc": self.surface_meter_tap_points.to_dict(),
            "mtrpage": self.meter_page_tap_points.to_dict(),
            "mainmtr": self.main_meter_source,
            "mainpos": self.main_meter_position,
        }

@dataclass_validate
@dataclass
class AudioTalkbackAssignments:
    mode: str
    monitor_dim: int
    bus_dim: int
    individual_send_levels: bool
    bus_assignments: OneIndexedList[bool]
    matrix_assignments: OneIndexedList[bool]
    main_assignments: OneIndexedList[bool]

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioTalkbackAssignments":
        return AudioTalkbackAssignments(
            mode=data["mode"],
            monitor_dim=data["mondim"],
            bus_dim=data["busdim"],
            individual_send_levels=data["indiv"],
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
    
    def to_dict(self):
        return {
            "mode": self.mode,
            "mondim": self.monitor_dim,
            "busdim": self.bus_dim,
            "indiv": self.individual_send_levels,
            **self.bus_assignments.to_dict(prefix="B"),
            **self.matrix_assignments.to_dict(prefix="MX"),
            **self.main_assignments.to_dict(prefix="M"),
        }

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
    
    def to_dict(self):
        return {
            "assign": self.assign,
            "lvl": self.fader_level,
            "A": self.talkback_a.to_dict(),
            "B": self.talkback_b.to_dict(),
        }

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

    def to_dict(self):
        return {
            "x": self.x_enable,
            "y": self.y_enable,
        }

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
    
    def to_dict(self):
        return {
            "mainlink": self.mainlink,
            "dcamgrp": self.dcamgrp,
            "mon": self.mon.to_dict(),
            "solo": self.solo.to_dict(),
            "rta": self.rta.to_dict(),
            "mtr": self.mtr.to_dict(),
            "talk": self.talk.to_dict(),
            "amix": self.amix.to_dict(),
        }
