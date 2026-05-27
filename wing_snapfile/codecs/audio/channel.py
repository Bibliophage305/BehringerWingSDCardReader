from wing_snapfile.models.audio.channel import (
    DelaySettings,
    DirectInput,
    Channel,
    BusChannel,
    MatrixChannel,
    MainChannel,
    AuxChannel,
    FullChannel,
)
from wing_snapfile.helpers.indexed import encode_one_indexed_list, decode_one_indexed_list

from wing_snapfile.codecs.audio.dynamics_crossover import DynamicsCrossoverCodec
from wing_snapfile.codecs.audio.dynamics_sidechain import DynamicsSidechainCodec
from wing_snapfile.codecs.audio.eq_block import EQBlockCodec
from wing_snapfile.codecs.audio.input import (
    InputCodec,
    FullInputCodec,
)
from wing_snapfile.codecs.audio.filter import FilterCodec
from wing_snapfile.codecs.audio.tap_eq import TapEQCodec
from wing_snapfile.codecs.audio.gate_sidechain import GateSidechainCodec
from wing_snapfile.codecs.audio.dynamics_block import DynamicsBlockCodec
from wing_snapfile.codecs.audio.pre_insert_block import PreInsertPluginCodec
from wing_snapfile.codecs.audio.post_insert_block import (
    PostInsertBlockCodec,
    PostInsertBlockWithAutomixCodec,
)
from wing_snapfile.codecs.audio.send import FullSendCodec, SendCodec


# ---------------------------------------------------------------------------
# Sub-struct codecs
# ---------------------------------------------------------------------------

class DelaySettingsCodec:
    @staticmethod
    def decode(data: dict) -> DelaySettings:
        return DelaySettings(
            on=data["on"],
            delay_mode=data["mode"],
            delay_amount=float(data["dly"]),
        )

    @staticmethod
    def encode(obj: DelaySettings) -> dict:
        return {
            "on": obj.on,
            "mode": obj.delay_mode,
            "dly": obj.delay_amount,
        }


class DirectInputCodec:
    @staticmethod
    def decode(data: dict) -> DirectInput:
        return DirectInput(
            direct_input=data["on"],
            fader_level=float(data["lvl"]),
            phase_invert=data["inv"],
            input_selector=data["in"],
        )

    @staticmethod
    def encode(obj: DirectInput) -> dict:
        return {
            "on": obj.direct_input,
            "lvl": obj.fader_level,
            "inv": obj.phase_invert,
            "in": obj.input_selector,
        }


# ---------------------------------------------------------------------------
# Shared decode/encode fragments
# ---------------------------------------------------------------------------

def _decode_channel_base(data: dict) -> dict:
    return {
        "color": data["col"],
        "name": data["name"],
        "icon": data["icon"],
        "led_on": data["led"],
        "mute_on": data["mute"],
        "fader_level": float(data["fdr"]),
        "pan": data["pan"],
        "width": data["wid"],
        "monitor_mode": data["mon"],
        "eq_block": EQBlockCodec.decode(data["eq"]),
        "dynamics_block": DynamicsBlockCodec.decode(data["dyn"]),
        "pre_insert_block": PreInsertPluginCodec.decode(data["preins"]),
        "tags": data["tags"].split(","),
    }


def _encode_channel_base(obj: Channel) -> dict:
    return {
        "col": obj.color,
        "name": obj.name,
        "icon": obj.icon,
        "led": obj.led_on,
        "mute": obj.mute_on,
        "fdr": obj.fader_level,
        "pan": obj.pan,
        "wid": obj.width,
        "mon": obj.monitor_mode,
        "eq": EQBlockCodec.encode(obj.eq_block),
        "dyn": DynamicsBlockCodec.encode(obj.dynamics_block),
        "preins": PreInsertPluginCodec.encode(obj.pre_insert_block),
        "tags": ",".join(obj.tags),
    }


def _decode_dynamics_fully_processable(data: dict) -> dict:
    return {
        "dynamics_sidechain": DynamicsSidechainCodec.decode(data["dynsc"]),
        "dynamics_crossover": DynamicsCrossoverCodec.decode(data["dynxo"]),
    }


def _encode_dynamics_fully_processable(obj) -> dict:
    return {
        "dynsc": DynamicsSidechainCodec.encode(obj.dynamics_sidechain),
        "dynxo": DynamicsCrossoverCodec.encode(obj.dynamics_crossover),
    }


def _decode_limited_sends(data: dict) -> dict:
    send = data["send"]
    return {
        "bus_sends": decode_one_indexed_list(
            {k: v for k, v in send.items() if not k.startswith("MX")},
            SendCodec.decode,
        ),
        "matrix_sends": decode_one_indexed_list(
            {k[2:]: v for k, v in send.items() if k.startswith("MX")},
            SendCodec.decode,
        ),
    }


def _encode_limited_sends(obj) -> dict:
    return {
        **encode_one_indexed_list(obj.bus_sends, SendCodec.encode),
        **encode_one_indexed_list(
            obj.matrix_sends, SendCodec.encode, prefix="MX"
        ),
    }


def _decode_full_sends(data: dict) -> dict:
    send = data["send"]
    return {
        "bus_sends": decode_one_indexed_list(
            {k: v for k, v in send.items() if not k.startswith("MX")},
            FullSendCodec.decode,
        ),
        "matrix_sends": decode_one_indexed_list(
            {k[2:]: v for k, v in send.items() if k.startswith("MX")},
            FullSendCodec.decode,
        ),
    }


def _encode_full_sends(obj) -> dict:
    return {
        **encode_one_indexed_list(obj.bus_sends, FullSendCodec.encode),
        **encode_one_indexed_list(obj.matrix_sends, FullSendCodec.encode, prefix="MX"),
    }


def _decode_main_sends(data: dict) -> dict:
    return {
        "main_sends": decode_one_indexed_list(data["main"], SendCodec.decode),
    }


def _encode_main_sends(obj) -> dict:
    return encode_one_indexed_list(obj.main_sends, SendCodec.encode)


# ---------------------------------------------------------------------------
# Concrete channel codecs
# ---------------------------------------------------------------------------

class BusChannelCodec:
    @staticmethod
    def decode(data: dict) -> BusChannel:
        return BusChannel(
            **_decode_channel_base(data),
            **_decode_limited_sends(data),
            **_decode_main_sends(data),
            **_decode_dynamics_fully_processable(data),
            input=InputCodec.decode(data["in"]),
            post_insert_block=PostInsertBlockCodec.decode(data["postins"]),
            delay_settings=DelaySettingsCodec.decode(data["dly"]),
            mono_bus=data["busmono"],
        )

    @staticmethod
    def encode(obj: BusChannel) -> dict:
        return {
            **_encode_channel_base(obj),
            **_encode_dynamics_fully_processable(obj),
            "in": InputCodec.encode(obj.input),
            "postins": PostInsertBlockCodec.encode(obj.post_insert_block),
            "dly": DelaySettingsCodec.encode(obj.delay_settings),
            "send": _encode_limited_sends(obj),
            "main": _encode_main_sends(obj),
            "busmono": obj.mono_bus,
        }


class MatrixChannelCodec:
    @staticmethod
    def decode(data: dict) -> MatrixChannel:
        return MatrixChannel(
            **_decode_channel_base(data),
            **_decode_dynamics_fully_processable(data),
            input=InputCodec.decode(data["in"]),
            post_insert_block=PostInsertBlockCodec.decode(data["postins"]),
            delay_settings=DelaySettingsCodec.decode(data["dly"]),
            direct_input_settings=DirectInputCodec.decode(data["dir"]),
            mono_bus=data["busmono"],
        )

    @staticmethod
    def encode(obj: MatrixChannel) -> dict:
        return {
            **_encode_channel_base(obj),
            **_encode_dynamics_fully_processable(obj),
            "in": InputCodec.encode(obj.input),
            "postins": PostInsertBlockCodec.encode(obj.post_insert_block),
            "dly": DelaySettingsCodec.encode(obj.delay_settings),
            "dir": DirectInputCodec.encode(obj.direct_input_settings),
            "busmono": obj.mono_bus,
        }


class MainChannelCodec:
    @staticmethod
    def decode(data: dict) -> MainChannel:
        return MainChannel(
            **_decode_channel_base(data),
            **_decode_limited_sends(data),
            **_decode_dynamics_fully_processable(data),
            input=InputCodec.decode(data["in"]),
            post_insert_block=PostInsertBlockCodec.decode(data["postins"]),
            delay_settings=DelaySettingsCodec.decode(data["dly"]),
            mono_bus=data["busmono"],
        )

    @staticmethod
    def encode(obj: MainChannel) -> dict:
        return {
            **_encode_channel_base(obj),
            "in": InputCodec.encode(obj.input),
            "send": _encode_limited_sends(obj),
            **_encode_dynamics_fully_processable(obj),
            "postins": PostInsertBlockCodec.encode(obj.post_insert_block),
            "dly": DelaySettingsCodec.encode(obj.delay_settings),
            "busmono": obj.mono_bus,
        }


class AuxChannelCodec:
    @staticmethod
    def decode(data: dict) -> AuxChannel:
        return AuxChannel(
            **_decode_channel_base(data),
            **_decode_full_sends(data),
            **_decode_main_sends(data),
            input=FullInputCodec.decode(data["in"]),
            link_customization_to_source=data["clink"],
            solo_safe=data["solosafe"],
            dynamics_sidechain=DynamicsSidechainCodec.decode(data["dynsc"]),
        )

    @staticmethod
    def encode(obj: AuxChannel) -> dict:
        return {
            **_encode_channel_base(obj),
            "in": FullInputCodec.encode(obj.input),
            "clink": obj.link_customization_to_source,
            "solosafe": obj.solo_safe,
            "send": _encode_full_sends(obj),
            "main": _encode_main_sends(obj),
            "dynsc": DynamicsSidechainCodec.encode(obj.dynamics_sidechain),
        }


class FullChannelCodec:
    @staticmethod
    def decode(data: dict) -> FullChannel:
        return FullChannel(
            **_decode_channel_base(data),
            **_decode_dynamics_fully_processable(data),
            **_decode_full_sends(data),
            **_decode_main_sends(data),
            input=FullInputCodec.decode(data["in"]),
            link_customization_to_source=data["clink"],
            solo_safe=data["solosafe"],
            post_insert_block=PostInsertBlockWithAutomixCodec.decode(
                data["postins"]
            ),
            filter=FilterCodec.decode(data["flt"]),
            processing_order=data["proc"],
            processing_tap_point=data["ptap"],
            tap_eq=TapEQCodec.decode(data["peq"]),
            gate_block=DynamicsBlockCodec.decode(data["gate"]),
            gate_sidechain=GateSidechainCodec.decode(data["gatesc"]),
            tap_width=data["tapwid"],
        )

    @staticmethod
    def encode(obj: FullChannel) -> dict:
        return {
            **_encode_channel_base(obj),
            **_encode_dynamics_fully_processable(obj),
            "in": FullInputCodec.encode(obj.input),
            "clink": obj.link_customization_to_source,
            "solosafe": obj.solo_safe,
            "postins": PostInsertBlockWithAutomixCodec.encode(
                obj.post_insert_block
            ),
            "send": _encode_full_sends(obj),
            "main": _encode_main_sends(obj),
            "flt": FilterCodec.encode(obj.filter),
            "proc": obj.processing_order,
            "ptap": obj.processing_tap_point,
            "peq": TapEQCodec.encode(obj.tap_eq),
            "gate": DynamicsBlockCodec.encode(obj.gate_block),
            "gatesc": GateSidechainCodec.encode(obj.gate_sidechain),
            "tapwid": obj.tap_width,
        }