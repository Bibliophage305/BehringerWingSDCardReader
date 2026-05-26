from wing_snapfile.models.audio.channel import (
    DelaySettings,
    AudioDirectInput,
    AudioChannel,
    AudioBusChannel,
    AudioMatrixChannel,
    AudioMainChannel,
    AudioAuxChannel,
    AudioFullChannel,
)
from wing_snapfile.helpers.indexed import encode_indexed, parse_indexed

from wing_snapfile.codecs.audio.dynamics_crossover import AudioDynamicsCrossoverCodec
from wing_snapfile.codecs.audio.dynamics_sidechain import AudioDynamicsSidechainCodec
from wing_snapfile.codecs.audio.eq import AudioEQCodec
from wing_snapfile.codecs.audio.input import (
    AudioInputCodec,
    AudioSourceSwitchableDelayableInputCodec,
)
from wing_snapfile.codecs.audio.filter import AudioFilterCodec
from wing_snapfile.codecs.audio.tap_eq import AudioTapEQCodec
from wing_snapfile.codecs.audio.gate_sidechain import AudioGateSidechainCodec
from wing_snapfile.codecs.audio.dynamics import AudioDynamicsCodec
from wing_snapfile.codecs.audio.pre_insert_plugin import AudioPreInsertPluginCodec
from wing_snapfile.codecs.audio.post_insert_plugin import (
    AudioPostInsertPluginCodec,
    AudioPostInsertPluginWithAutomixCodec,
)
from wing_snapfile.codecs.audio.send import AudioFullSendCodec, AudioLimitedSendCodec


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


class AudioDirectInputCodec:
    @staticmethod
    def decode(data: dict) -> AudioDirectInput:
        return AudioDirectInput(
            direct_input=data["on"],
            fader_level=float(data["lvl"]),
            phase_invert=data["inv"],
            input_selector=data["in"],
        )

    @staticmethod
    def encode(obj: AudioDirectInput) -> dict:
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
        "eq_plugin": AudioEQCodec.decode(data["eq"]),
        "dynamics_plugin": AudioDynamicsCodec.decode(data["dyn"]),
        "pre_insert_plugin": AudioPreInsertPluginCodec.decode(data["preins"]),
        "tags": data["tags"].split(",") if data["tags"] else [],
    }


def _encode_channel_base(obj: AudioChannel) -> dict:
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
        "eq": AudioEQCodec.encode(obj.eq_plugin),
        "dyn": AudioDynamicsCodec.encode(obj.dynamics_plugin),
        "preins": AudioPreInsertPluginCodec.encode(obj.pre_insert_plugin),
        "tags": ",".join(obj.tags),
    }


def _decode_dynamics_fully_processable(data: dict) -> dict:
    return {
        "dynamics_sidechain": AudioDynamicsSidechainCodec.decode(data["dynsc"]),
        "dynamics_crossover": AudioDynamicsCrossoverCodec.decode(data["dynxo"]),
    }


def _encode_dynamics_fully_processable(obj) -> dict:
    return {
        "dynsc": AudioDynamicsSidechainCodec.encode(obj.dynamics_sidechain),
        "dynxo": AudioDynamicsCrossoverCodec.encode(obj.dynamics_crossover),
    }


def _decode_limited_sends(data: dict) -> dict:
    send = data["send"]
    return {
        "bus_sends": parse_indexed(
            {k: v for k, v in send.items() if not k.startswith("MX")},
            AudioLimitedSendCodec.decode,
        ),
        "matrix_sends": parse_indexed(
            {k[2:]: v for k, v in send.items() if k.startswith("MX")},
            AudioLimitedSendCodec.decode,
        ),
    }


def _encode_limited_sends(obj) -> dict:
    return {
        **encode_indexed(obj.bus_sends, AudioLimitedSendCodec.encode),
        **encode_indexed(
            obj.matrix_sends, AudioLimitedSendCodec.encode, prefix="MX"
        ),
    }


def _decode_full_sends(data: dict) -> dict:
    send = data["send"]
    return {
        "bus_sends": parse_indexed(
            {k: v for k, v in send.items() if not k.startswith("MX")},
            AudioFullSendCodec.decode,
        ),
        "matrix_sends": parse_indexed(
            {k[2:]: v for k, v in send.items() if k.startswith("MX")},
            AudioFullSendCodec.decode,
        ),
    }


def _encode_full_sends(obj) -> dict:
    return {
        **encode_indexed(obj.bus_sends, AudioFullSendCodec.encode),
        **encode_indexed(obj.matrix_sends, AudioFullSendCodec.encode, prefix="MX"),
    }


def _decode_main_sends(data: dict) -> dict:
    return {
        "main_sends": parse_indexed(data["main"], AudioLimitedSendCodec.decode),
    }


def _encode_main_sends(obj) -> dict:
    return encode_indexed(obj.main_sends, AudioLimitedSendCodec.encode)


# ---------------------------------------------------------------------------
# Concrete channel codecs
# ---------------------------------------------------------------------------

class AudioBusChannelCodec:
    @staticmethod
    def decode(data: dict) -> AudioBusChannel:
        return AudioBusChannel(
            **_decode_channel_base(data),
            **_decode_limited_sends(data),
            **_decode_main_sends(data),
            **_decode_dynamics_fully_processable(data),
            input=AudioInputCodec.decode(data["in"]),
            post_insert_plugin=AudioPostInsertPluginCodec.decode(data["postins"]),
            delay_settings=DelaySettingsCodec.decode(data["dly"]),
            mono_bus=data["busmono"],
        )

    @staticmethod
    def encode(obj: AudioBusChannel) -> dict:
        return {
            **_encode_channel_base(obj),
            **_encode_dynamics_fully_processable(obj),
            "in": AudioInputCodec.encode(obj.input),
            "postins": AudioPostInsertPluginCodec.encode(obj.post_insert_plugin),
            "dly": DelaySettingsCodec.encode(obj.delay_settings),
            "send": _encode_limited_sends(obj),
            "main": _encode_main_sends(obj),
            "busmono": obj.mono_bus,
        }


class AudioMatrixChannelCodec:
    @staticmethod
    def decode(data: dict) -> AudioMatrixChannel:
        return AudioMatrixChannel(
            **_decode_channel_base(data),
            **_decode_dynamics_fully_processable(data),
            input=AudioInputCodec.decode(data["in"]),
            post_insert_plugin=AudioPostInsertPluginCodec.decode(data["postins"]),
            delay_settings=DelaySettingsCodec.decode(data["dly"]),
            direct_input_settings=AudioDirectInputCodec.decode(data["dir"]),
            mono_bus=data["busmono"],
        )

    @staticmethod
    def encode(obj: AudioMatrixChannel) -> dict:
        return {
            **_encode_channel_base(obj),
            **_encode_dynamics_fully_processable(obj),
            "in": AudioInputCodec.encode(obj.input),
            "postins": AudioPostInsertPluginCodec.encode(obj.post_insert_plugin),
            "dly": DelaySettingsCodec.encode(obj.delay_settings),
            "dir": AudioDirectInputCodec.encode(obj.direct_input_settings),
            "busmono": obj.mono_bus,
        }


class AudioMainChannelCodec:
    @staticmethod
    def decode(data: dict) -> AudioMainChannel:
        return AudioMainChannel(
            **_decode_channel_base(data),
            **_decode_limited_sends(data),
            **_decode_dynamics_fully_processable(data),
            input=AudioInputCodec.decode(data["in"]),
            post_insert_plugin=AudioPostInsertPluginCodec.decode(data["postins"]),
            delay_settings=DelaySettingsCodec.decode(data["dly"]),
            mono_bus=data["busmono"],
        )

    @staticmethod
    def encode(obj: AudioMainChannel) -> dict:
        return {
            **_encode_channel_base(obj),
            "in": AudioInputCodec.encode(obj.input),
            "send": _encode_limited_sends(obj),
            **_encode_dynamics_fully_processable(obj),
            "postins": AudioPostInsertPluginCodec.encode(obj.post_insert_plugin),
            "dly": DelaySettingsCodec.encode(obj.delay_settings),
            "busmono": obj.mono_bus,
        }


class AudioAuxChannelCodec:
    @staticmethod
    def decode(data: dict) -> AudioAuxChannel:
        return AudioAuxChannel(
            **_decode_channel_base(data),
            **_decode_full_sends(data),
            **_decode_main_sends(data),
            input=AudioSourceSwitchableDelayableInputCodec.decode(data["in"]),
            link_customization_to_source=data["clink"],
            solo_safe=data["solosafe"],
            dynamics_sidechain=AudioDynamicsSidechainCodec.decode(data["dynsc"]),
        )

    @staticmethod
    def encode(obj: AudioAuxChannel) -> dict:
        return {
            **_encode_channel_base(obj),
            "in": AudioSourceSwitchableDelayableInputCodec.encode(obj.input),
            "clink": obj.link_customization_to_source,
            "solosafe": obj.solo_safe,
            "send": _encode_full_sends(obj),
            "main": _encode_main_sends(obj),
            "dynsc": AudioDynamicsSidechainCodec.encode(obj.dynamics_sidechain),
        }


class AudioFullChannelCodec:
    @staticmethod
    def decode(data: dict) -> AudioFullChannel:
        return AudioFullChannel(
            **_decode_channel_base(data),
            **_decode_dynamics_fully_processable(data),
            **_decode_full_sends(data),
            **_decode_main_sends(data),
            input=AudioSourceSwitchableDelayableInputCodec.decode(data["in"]),
            link_customization_to_source=data["clink"],
            solo_safe=data["solosafe"],
            post_insert_plugin=AudioPostInsertPluginWithAutomixCodec.decode(
                data["postins"]
            ),
            filter=AudioFilterCodec.decode(data["flt"]),
            processing_order=data["proc"],
            processing_tap_point=data["ptap"],
            tap_eq=AudioTapEQCodec.decode(data["peq"]),
            gate_plugin=AudioDynamicsCodec.decode(data["gate"]),
            gate_sidechain=AudioGateSidechainCodec.decode(data["gatesc"]),
            tap_width=data["tapwid"],
        )

    @staticmethod
    def encode(obj: AudioFullChannel) -> dict:
        return {
            **_encode_channel_base(obj),
            **_encode_dynamics_fully_processable(obj),
            "in": AudioSourceSwitchableDelayableInputCodec.encode(obj.input),
            "clink": obj.link_customization_to_source,
            "solosafe": obj.solo_safe,
            "postins": AudioPostInsertPluginWithAutomixCodec.encode(
                obj.post_insert_plugin
            ),
            "send": _encode_full_sends(obj),
            "main": _encode_main_sends(obj),
            "flt": AudioFilterCodec.encode(obj.filter),
            "proc": obj.processing_order,
            "ptap": obj.processing_tap_point,
            "peq": AudioTapEQCodec.encode(obj.tap_eq),
            "gate": AudioDynamicsCodec.encode(obj.gate_plugin),
            "gatesc": AudioGateSidechainCodec.encode(obj.gate_sidechain),
            "tapwid": obj.tap_width,
        }