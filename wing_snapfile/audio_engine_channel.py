from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

from .audio_engine_dynamics_crossover import AudioEngineDynamicsCrossover
from .audio_engine_dynamics_sidechain import AudioEngineDynamicsSidechain
from .audio_engine_eq import AudioEngineEQ
from .audio_engine_input import AudioEngineInput, AudioEngineRoutableInput
from .audio_engine_filter import AudioEngineFilter
from .audio_engine_tap_eq import AudioEngineTapEQ
from .audio_engine_gate_sidechain import AudioEngineGateSidechain
from .audio_engine_dynamics import AudioEngineDynamics
from .audio_engine_pre_insert_plugin import AudioEnginePreInsertPlugin
from .audio_engine_post_insert_plugin import AudioEnginePostInsertPlugin
from .audio_engine_send import AudioEngineFullSend, AudioEngineLimitedSend

from .snapfile_reader import OneIndexedList

@dataclass_validate
@dataclass
class Routable:
    link_customization_to_source: bool

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            "input": AudioEngineRoutableInput.from_dict(data["in"]),
            "link_customization_to_source": data["clink"],
        }

@dataclass_validate
@dataclass
class Soloable:
    solo_safe: bool

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            "solo_safe": data["solosafe"],
        }

@dataclass_validate
@dataclass
class FullBusSendable:
    bus_sends: OneIndexedList[AudioEngineFullSend]

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            "bus_sends": OneIndexedList.from_indexed_dict(
                {k: v for k, v in data["send"].items() if not k.startswith("MX")},
                AudioEngineFullSend.from_dict,
            ),
        }

@dataclass_validate
@dataclass
class LimitedBusSendable:
    bus_sends: OneIndexedList[AudioEngineLimitedSend]

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            "bus_sends": OneIndexedList.from_indexed_dict(
                {k: v for k, v in data["send"].items() if not k.startswith("MX")},
                AudioEngineLimitedSend.from_dict,
            ),
        }

@dataclass_validate
@dataclass
class FullMatrixSendable:
    matrix_sends: OneIndexedList[AudioEngineFullSend]

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            "matrix_sends": OneIndexedList.from_indexed_dict(
                {k[2:]: v for k, v in data["send"].items() if k.startswith("MX")},
                AudioEngineFullSend.from_dict,
            ),
        }

@dataclass_validate
@dataclass
class LimitedMatrixSendable:
    matrix_sends: OneIndexedList[AudioEngineLimitedSend]

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            "matrix_sends": OneIndexedList.from_indexed_dict(
                {k[2:]: v for k, v in data["send"].items() if k.startswith("MX")},
                AudioEngineLimitedSend.from_dict,
            ),
        }

@dataclass_validate
@dataclass
class MainSendable:
    main_sends: OneIndexedList[AudioEngineLimitedSend]

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            "main_sends": OneIndexedList.from_indexed_dict(
                data["main"],
                AudioEngineLimitedSend.from_dict,
            ),
        }

@dataclass_validate
@dataclass
class AudioEngineChannel:
    input: AudioEngineInput
    color: int
    name: str
    icon: int
    led_on: bool
    mute_on: bool
    fader_level: float
    pan: int
    width: int
    monitor_mode: str
    eq_plugin: AudioEngineEQ
    dynamics_plugin: AudioEngineDynamics
    pre_insert_plugin: AudioEnginePreInsertPlugin
    tags: list[str]

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            "input": AudioEngineInput.from_dict(data["in"]),
            "color": data["col"],
            "name": data["name"],
            "icon": data["icon"],
            "led_on": data["led"],
            "mute_on": data["mute"],
            "fader_level": float(data["fdr"]),
            "pan": data["pan"],
            "width": data["wid"],
            "monitor_mode": data["mon"],
            "eq_plugin": AudioEngineEQ.from_dict(data["eq"]),
            "dynamics_plugin": AudioEngineDynamics.from_dict(data["dyn"]),
            "pre_insert_plugin": AudioEnginePreInsertPlugin.from_dict(data["preins"]),
            "tags": data["tags"].split(","),
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**cls._from_dict_kwargs(data))

@dataclass_validate
@dataclass
class AudioEngineBusChannel(AudioEngineChannel, LimitedBusSendable, LimitedMatrixSendable, MainSendable):
    mono_bus: bool

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioEngineChannel._from_dict_kwargs(data),
            **LimitedBusSendable._from_dict_kwargs(data),
            **LimitedMatrixSendable._from_dict_kwargs(data),
            **MainSendable._from_dict_kwargs(data),
            "mono_bus": data["busmono"],
        }

@dataclass_validate
@dataclass
class AudioEngineDirectInput:
    direct_input: bool
    fader_level: float
    phase_invert: bool
    input_selector: str

    @classmethod
    def from_dict(cls, data):
        return cls(
            direct_input=data["on"],
            fader_level=float(data["lvl"]),
            phase_invert=data["inv"],
            input_selector=data["in"],
        )

@dataclass_validate
@dataclass
class AudioEngineMatrixChannel(AudioEngineChannel):
    direct_input_settings: AudioEngineDirectInput
    mono_bus: bool

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioEngineChannel._from_dict_kwargs(data),
            "direct_input_settings": AudioEngineDirectInput.from_dict(data["dir"]),
            "mono_bus": data["busmono"],
        }

@dataclass_validate
@dataclass
class AudioEngineMainChannel(AudioEngineChannel, LimitedBusSendable, LimitedMatrixSendable):
    mono_bus: bool

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioEngineChannel._from_dict_kwargs(data),
            **LimitedBusSendable._from_dict_kwargs(data),
            **LimitedMatrixSendable._from_dict_kwargs(data),
            "mono_bus": data["busmono"],
        }

@dataclass_validate
@dataclass
class AudioEngineAuxChannel(AudioEngineChannel, Routable, Soloable, FullBusSendable, FullMatrixSendable, MainSendable):
    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioEngineChannel._from_dict_kwargs(data),
            **Routable._from_dict_kwargs(data),
            **Soloable._from_dict_kwargs(data),
            **FullBusSendable._from_dict_kwargs(data),
            **FullMatrixSendable._from_dict_kwargs(data),
            **MainSendable._from_dict_kwargs(data),
        }

@dataclass_validate
@dataclass
class AudioEngineFullChannel(AudioEngineChannel, Routable, Soloable, FullBusSendable, FullMatrixSendable, MainSendable):
    filter: AudioEngineFilter
    processing_order: str
    processing_tap_point: str
    tap_eq: AudioEngineTapEQ
    gate_plugin: AudioEngineDynamics
    gate_sidechain: AudioEngineGateSidechain
    dynamics_crossover: AudioEngineDynamicsCrossover
    dynamics_sidechain: AudioEngineDynamicsSidechain
    tap_width: int
    post_insert_plugin: AudioEnginePostInsertPlugin

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioEngineChannel._from_dict_kwargs(data),
            **Routable._from_dict_kwargs(data),
            **Soloable._from_dict_kwargs(data),
            **FullBusSendable._from_dict_kwargs(data),
            **FullMatrixSendable._from_dict_kwargs(data),
            **MainSendable._from_dict_kwargs(data),
            "filter": AudioEngineFilter.from_dict(data["flt"]),
            "processing_order": data["proc"],
            "processing_tap_point": data["ptap"],
            "tap_eq": AudioEngineTapEQ.from_dict(data["peq"]),
            "gate_plugin": AudioEngineDynamics.from_dict(data["gate"]),
            "gate_sidechain": AudioEngineGateSidechain.from_dict(data["gatesc"]),
            "dynamics_crossover": AudioEngineDynamicsCrossover.from_dict(data["dynxo"]),
            "dynamics_sidechain": AudioEngineDynamicsSidechain.from_dict(data["dynsc"]),
            "tap_width": data["tapwid"],
            "post_insert_plugin": AudioEnginePostInsertPlugin.from_dict(data["postins"]),
        }
