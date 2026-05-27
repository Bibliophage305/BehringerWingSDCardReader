from wing_snapfile.models.audio.config import (
    AudioConfig,
    SoloConfig,
    RTAConfig,
    MeterConfig,
    MeterTapPoints,
    TalkbackConfig,
    TalkbackAssignments,
    AutomixConfig,
)

from wing_snapfile.helpers.indexed import decode_one_indexed_list, encode_one_indexed_list

from wing_snapfile.codecs.audio.monitor import MonitorCodec


class SoloConfigCodec:
    @staticmethod
    def decode(data: dict) -> SoloConfig:
        return SoloConfig(
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
    def encode(obj: SoloConfig) -> dict:
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


class RTAConfigCodec:
    @staticmethod
    def decode(data: dict) -> RTAConfig:
        return RTAConfig(
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
    def encode(obj: RTAConfig) -> dict:
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


class MeterTapPointsCodec:
    @staticmethod
    def decode(data: dict) -> MeterTapPoints:
        return MeterTapPoints(
            channel_tap=data["in"],
            bus_tap=data["bus"],
            main_tap=data["main"],
            matrix_tap=data["mtx"],
            dca_tap=data["dca"],
        )

    @staticmethod
    def encode(obj: MeterTapPoints) -> dict:
        return {
            "in": obj.channel_tap,
            "bus": obj.bus_tap,
            "main": obj.main_tap,
            "mtx": obj.matrix_tap,
            "dca": obj.dca_tap,
        }


class MeterConfigCodec:
    @staticmethod
    def decode(data: dict) -> MeterConfig:
        return MeterConfig(
            scope_source=data["scopesrc"],
            scope_tap_point=data["scopetap"],
            surface_meter_tap_points=MeterTapPointsCodec.decode(data["mtrsfc"]),
            meter_page_tap_points=MeterTapPointsCodec.decode(data["mtrpage"]),
            main_meter_source=data["mainmtr"],
            main_meter_position=data["mainpos"],
        )

    @staticmethod
    def encode(obj: MeterConfig) -> dict:
        return {
            "scopesrc": obj.scope_source,
            "scopetap": obj.scope_tap_point,
            "mtrsfc": MeterTapPointsCodec.encode(obj.surface_meter_tap_points),
            "mtrpage": MeterTapPointsCodec.encode(obj.meter_page_tap_points),
            "mainmtr": obj.main_meter_source,
            "mainpos": obj.main_meter_position,
        }


class TalkbackAssignmentsCodec:
    @staticmethod
    def decode(data: dict) -> TalkbackAssignments:
        return TalkbackAssignments(
            mode=data["mode"],
            monitor_dim=data["mondim"],
            bus_dim=data["busdim"],
            individual_send_levels=data["indiv"],

            bus_assignments=decode_one_indexed_list(
                {k[1:]: v for k, v in data.items()
                 if k.startswith("B") and k[1:].isdigit()},
                lambda x: x,
            ),

            matrix_assignments=decode_one_indexed_list(
                {k[2:]: v for k, v in data.items()
                 if k.startswith("MX") and k[2:].isdigit()},
                lambda x: x,
            ),

            main_assignments=decode_one_indexed_list(
                {k[1:]: v for k, v in data.items()
                 if k.startswith("M") and k[1:].isdigit()},
                lambda x: x,
            ),
        )

    @staticmethod
    def encode(obj: TalkbackAssignments) -> dict:
        return {
            "mode": obj.mode,
            "mondim": obj.monitor_dim,
            "busdim": obj.bus_dim,
            "indiv": obj.individual_send_levels,

            **obj.bus_assignments.to_dict(prefix="B"),
            **obj.matrix_assignments.to_dict(prefix="MX"),
            **obj.main_assignments.to_dict(prefix="M"),
        }


class TalkbackConfigCodec:
    @staticmethod
    def decode(data: dict) -> TalkbackConfig:
        return TalkbackConfig(
            assign=data["assign"],
            fader_level=float(data["lvl"]),
            talkback_a=TalkbackAssignmentsCodec.decode(data["A"]),
            talkback_b=TalkbackAssignmentsCodec.decode(data["B"]),
        )

    @staticmethod
    def encode(obj: TalkbackConfig) -> dict:
        return {
            "assign": obj.assign,
            "lvl": obj.fader_level,
            "A": TalkbackAssignmentsCodec.encode(obj.talkback_a),
            "B": TalkbackAssignmentsCodec.encode(obj.talkback_b),
        }


class AutomixConfigCodec:
    @staticmethod
    def decode(data: dict) -> AutomixConfig:
        return AutomixConfig(
            x_enable=data["x"],
            y_enable=data["y"],
        )

    @staticmethod
    def encode(obj: AutomixConfig) -> dict:
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
            mon=decode_one_indexed_list(data["mon"], MonitorCodec.decode),

            solo=SoloConfigCodec.decode(data["solo"]),
            rta=RTAConfigCodec.decode(data["rta"]),
            mtr=MeterConfigCodec.decode(data["mtr"]),
            talk=TalkbackConfigCodec.decode(data["talk"]),
            amix=AutomixConfigCodec.decode(data["amix"]),
        )

    @staticmethod
    def encode(obj: AudioConfig) -> dict:
        return {
            "mainlink": obj.mainlink,
            "dcamgrp": obj.dcamgrp,
            "mon": encode_one_indexed_list(obj.mon, encoder=MonitorCodec.encode),
            "solo": SoloConfigCodec.encode(obj.solo),
            "rta": RTAConfigCodec.encode(obj.rta),
            "mtr": MeterConfigCodec.encode(obj.mtr),
            "talk": TalkbackConfigCodec.encode(obj.talk),
            "amix": AutomixConfigCodec.encode(obj.amix),
        }