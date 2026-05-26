from wing_snapfile.models.audio.config import (
    AudioConfig,
    AudioSoloConfig,
    AudioRTAConfig,
    AudioMeterConfig,
    AudioMeterTapPoints,
    AudioTalkbackConfig,
    AudioTalkbackAssignments,
    AudioAutomixConfig,
)

from wing_snapfile.helpers.indexed import parse_indexed, encode_indexed

from wing_snapfile.codecs.audio.monitor import AudioMonitorCodec


class AudioSoloConfigCodec:
    @staticmethod
    def decode(data: dict) -> AudioSoloConfig:
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

    @staticmethod
    def encode(obj: AudioSoloConfig) -> dict:
        return {
            "mode": obj.mode,
            "mon": obj.monitor_outputs,
            "mute": obj.mute,
            "chtap": obj.channel_tap,
            "bustap": obj.bus_tap,
            "maintap": obj.main_tap,
            "mtxtap": obj.matrix_tap,
            "srcsolo": obj.source_solo,
        }


class AudioRTAConfigCodec:
    @staticmethod
    def decode(data: dict) -> AudioRTAConfig:
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

    @staticmethod
    def encode(obj: AudioRTAConfig) -> dict:
        return {
            "rtarange": obj.rta_range,
            "rtagain": obj.rta_gain,
            "rtaauto": obj.rta_autogain,
            "eqdecay": obj.eq_decay,
            "eqdet": obj.eq_detector,
            "eqrange": obj.eq_range,
            "eqgain": obj.eq_gain,
            "eqauto": obj.eq_autogain,
        }


class AudioMeterTapPointsCodec:
    @staticmethod
    def decode(data: dict) -> AudioMeterTapPoints:
        return AudioMeterTapPoints(
            channel_tap=data["in"],
            bus_tap=data["bus"],
            main_tap=data["main"],
            matrix_tap=data["mtx"],
            dca_tap=data["dca"],
        )

    @staticmethod
    def encode(obj: AudioMeterTapPoints) -> dict:
        return {
            "in": obj.channel_tap,
            "bus": obj.bus_tap,
            "main": obj.main_tap,
            "mtx": obj.matrix_tap,
            "dca": obj.dca_tap,
        }


class AudioMeterConfigCodec:
    @staticmethod
    def decode(data: dict) -> AudioMeterConfig:
        return AudioMeterConfig(
            scope_source=data["scopesrc"],
            scope_tap_point=data["scopetap"],
            surface_meter_tap_points=AudioMeterTapPointsCodec.decode(data["mtrsfc"]),
            meter_page_tap_points=AudioMeterTapPointsCodec.decode(data["mtrpage"]),
            main_meter_source=data["mainmtr"],
            main_meter_position=data["mainpos"],
        )

    @staticmethod
    def encode(obj: AudioMeterConfig) -> dict:
        return {
            "scopesrc": obj.scope_source,
            "scopetap": obj.scope_tap_point,
            "mtrsfc": AudioMeterTapPointsCodec.encode(obj.surface_meter_tap_points),
            "mtrpage": AudioMeterTapPointsCodec.encode(obj.meter_page_tap_points),
            "mainmtr": obj.main_meter_source,
            "mainpos": obj.main_meter_position,
        }


class AudioTalkbackAssignmentsCodec:
    @staticmethod
    def decode(data: dict) -> AudioTalkbackAssignments:
        return AudioTalkbackAssignments(
            mode=data["mode"],
            monitor_dim=data["mondim"],
            bus_dim=data["busdim"],
            individual_send_levels=data["indiv"],

            bus_assignments=parse_indexed(
                {k[1:]: v for k, v in data.items()
                 if k.startswith("B") and k[1:].isdigit()},
                lambda x: x,
            ),

            matrix_assignments=parse_indexed(
                {k[2:]: v for k, v in data.items()
                 if k.startswith("MX") and k[2:].isdigit()},
                lambda x: x,
            ),

            main_assignments=parse_indexed(
                {k[1:]: v for k, v in data.items()
                 if k.startswith("M") and k[1:].isdigit()},
                lambda x: x,
            ),
        )

    @staticmethod
    def encode(obj: AudioTalkbackAssignments) -> dict:
        return {
            "mode": obj.mode,
            "mondim": obj.monitor_dim,
            "busdim": obj.bus_dim,
            "indiv": obj.individual_send_levels,

            **obj.bus_assignments.to_dict(prefix="B"),
            **obj.matrix_assignments.to_dict(prefix="MX"),
            **obj.main_assignments.to_dict(prefix="M"),
        }


class AudioTalkbackConfigCodec:
    @staticmethod
    def decode(data: dict) -> AudioTalkbackConfig:
        return AudioTalkbackConfig(
            assign=data["assign"],
            fader_level=float(data["lvl"]),
            talkback_a=AudioTalkbackAssignmentsCodec.decode(data["A"]),
            talkback_b=AudioTalkbackAssignmentsCodec.decode(data["B"]),
        )

    @staticmethod
    def encode(obj: AudioTalkbackConfig) -> dict:
        return {
            "assign": obj.assign,
            "lvl": obj.fader_level,
            "A": AudioTalkbackAssignmentsCodec.encode(obj.talkback_a),
            "B": AudioTalkbackAssignmentsCodec.encode(obj.talkback_b),
        }


class AudioAutomixConfigCodec:
    @staticmethod
    def decode(data: dict) -> AudioAutomixConfig:
        return AudioAutomixConfig(
            x_enable=data["x"],
            y_enable=data["y"],
        )

    @staticmethod
    def encode(obj: AudioAutomixConfig) -> dict:
        return {
            "x": obj.x_enable,
            "y": obj.y_enable,
        }


class AudioConfigCodec:
    @staticmethod
    def decode(data: dict) -> AudioConfig:
        return AudioConfig(
            mainlink=data["mainlink"],
            dcamgrp=data["dcamgrp"],
            mon=parse_indexed(data["mon"], AudioMonitorCodec.decode),

            solo=AudioSoloConfigCodec.decode(data["solo"]),
            rta=AudioRTAConfigCodec.decode(data["rta"]),
            mtr=AudioMeterConfigCodec.decode(data["mtr"]),
            talk=AudioTalkbackConfigCodec.decode(data["talk"]),
            amix=AudioAutomixConfigCodec.decode(data["amix"]),
        )

    @staticmethod
    def encode(obj: AudioConfig) -> dict:
        return {
            "mainlink": obj.mainlink,
            "dcamgrp": obj.dcamgrp,
            "mon": encode_indexed(obj.mon, encoder=AudioMonitorCodec.encode),
            "solo": AudioSoloConfigCodec.encode(obj.solo),
            "rta": AudioRTAConfigCodec.encode(obj.rta),
            "mtr": AudioMeterConfigCodec.encode(obj.mtr),
            "talk": AudioTalkbackConfigCodec.encode(obj.talk),
            "amix": AudioAutomixConfigCodec.encode(obj.amix),
        }