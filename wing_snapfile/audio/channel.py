from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

from wing_snapfile.audio.dynamics_crossover import AudioDynamicsCrossover
from wing_snapfile.audio.dynamics_sidechain import AudioDynamicsSidechain
from wing_snapfile.audio.eq import AudioEQ
from wing_snapfile.audio.input import AudioInput, AudioRoutableInput
from wing_snapfile.audio.filter import AudioFilter
from wing_snapfile.audio.tap_eq import AudioTapEQ
from wing_snapfile.audio.gate_sidechain import AudioGateSidechain
from wing_snapfile.audio.dynamics import AudioDynamics
from wing_snapfile.audio.pre_insert_plugin import AudioPreInsertPlugin
from wing_snapfile.audio.post_insert_plugin import AudioPostInsertPlugin
from wing_snapfile.audio.send import AudioFullSend, AudioLimitedSend

from wing_snapfile.types import OneIndexedList

@dataclass_validate
@dataclass
class Routable:
    link_customization_to_source: bool

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            "input": AudioRoutableInput.from_dict(data["in"]),
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
    bus_sends: OneIndexedList[AudioFullSend]

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            "bus_sends": OneIndexedList.from_indexed_dict(
                {k: v for k, v in data["send"].items() if not k.startswith("MX")},
                AudioFullSend.from_dict,
            ),
        }

@dataclass_validate
@dataclass
class LimitedBusSendable:
    bus_sends: OneIndexedList[AudioLimitedSend]

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            "bus_sends": OneIndexedList.from_indexed_dict(
                {k: v for k, v in data["send"].items() if not k.startswith("MX")},
                AudioLimitedSend.from_dict,
            ),
        }

@dataclass_validate
@dataclass
class FullMatrixSendable:
    matrix_sends: OneIndexedList[AudioFullSend]

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            "matrix_sends": OneIndexedList.from_indexed_dict(
                {k[2:]: v for k, v in data["send"].items() if k.startswith("MX")},
                AudioFullSend.from_dict,
            ),
        }

@dataclass_validate
@dataclass
class LimitedMatrixSendable:
    matrix_sends: OneIndexedList[AudioLimitedSend]

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            "matrix_sends": OneIndexedList.from_indexed_dict(
                {k[2:]: v for k, v in data["send"].items() if k.startswith("MX")},
                AudioLimitedSend.from_dict,
            ),
        }

@dataclass_validate
@dataclass
class MainSendable:
    main_sends: OneIndexedList[AudioLimitedSend]

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            "main_sends": OneIndexedList.from_indexed_dict(
                data["main"],
                AudioLimitedSend.from_dict,
            ),
        }

@dataclass_validate
@dataclass
class AudioChannel:
    input: AudioInput
    color: int
    name: str
    icon: int
    led_on: bool
    mute_on: bool
    fader_level: float
    pan: int
    width: int
    monitor_mode: str
    eq_plugin: AudioEQ
    dynamics_plugin: AudioDynamics
    pre_insert_plugin: AudioPreInsertPlugin
    tags: list[str]

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            "input": AudioInput.from_dict(data["in"]),
            "color": data["col"],
            "name": data["name"],
            "icon": data["icon"],
            "led_on": data["led"],
            "mute_on": data["mute"],
            "fader_level": float(data["fdr"]),
            "pan": data["pan"],
            "width": data["wid"],
            "monitor_mode": data["mon"],
            "eq_plugin": AudioEQ.from_dict(data["eq"]),
            "dynamics_plugin": AudioDynamics.from_dict(data["dyn"]),
            "pre_insert_plugin": AudioPreInsertPlugin.from_dict(data["preins"]),
            "tags": data["tags"].split(","),
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**cls._from_dict_kwargs(data))

@dataclass_validate
@dataclass
class AudioBusChannel(AudioChannel, LimitedBusSendable, LimitedMatrixSendable, MainSendable):
    mono_bus: bool

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioChannel._from_dict_kwargs(data),
            **LimitedBusSendable._from_dict_kwargs(data),
            **LimitedMatrixSendable._from_dict_kwargs(data),
            **MainSendable._from_dict_kwargs(data),
            "mono_bus": data["busmono"],
        }

@dataclass_validate
@dataclass
class AudioDirectInput:
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
class AudioMatrixChannel(AudioChannel):
    direct_input_settings: AudioDirectInput
    mono_bus: bool

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioChannel._from_dict_kwargs(data),
            "direct_input_settings": AudioDirectInput.from_dict(data["dir"]),
            "mono_bus": data["busmono"],
        }

@dataclass_validate
@dataclass
class AudioMainChannel(AudioChannel, LimitedBusSendable, LimitedMatrixSendable):
    mono_bus: bool

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioChannel._from_dict_kwargs(data),
            **LimitedBusSendable._from_dict_kwargs(data),
            **LimitedMatrixSendable._from_dict_kwargs(data),
            "mono_bus": data["busmono"],
        }

@dataclass_validate
@dataclass
class AudioAuxChannel(AudioChannel, Routable, Soloable, FullBusSendable, FullMatrixSendable, MainSendable):
    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioChannel._from_dict_kwargs(data),
            **Routable._from_dict_kwargs(data),
            **Soloable._from_dict_kwargs(data),
            **FullBusSendable._from_dict_kwargs(data),
            **FullMatrixSendable._from_dict_kwargs(data),
            **MainSendable._from_dict_kwargs(data),
        }

@dataclass_validate
@dataclass
class AudioFullChannel(AudioChannel, Routable, Soloable, FullBusSendable, FullMatrixSendable, MainSendable):
    filter: AudioFilter
    processing_order: str
    processing_tap_point: str
    tap_eq: AudioTapEQ
    gate_plugin: AudioDynamics
    gate_sidechain: AudioGateSidechain
    dynamics_crossover: AudioDynamicsCrossover
    dynamics_sidechain: AudioDynamicsSidechain
    tap_width: int
    post_insert_plugin: AudioPostInsertPlugin

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioChannel._from_dict_kwargs(data),
            **Routable._from_dict_kwargs(data),
            **Soloable._from_dict_kwargs(data),
            **FullBusSendable._from_dict_kwargs(data),
            **FullMatrixSendable._from_dict_kwargs(data),
            **MainSendable._from_dict_kwargs(data),
            "filter": AudioFilter.from_dict(data["flt"]),
            "processing_order": data["proc"],
            "processing_tap_point": data["ptap"],
            "tap_eq": AudioTapEQ.from_dict(data["peq"]),
            "gate_plugin": AudioDynamics.from_dict(data["gate"]),
            "gate_sidechain": AudioGateSidechain.from_dict(data["gatesc"]),
            "dynamics_crossover": AudioDynamicsCrossover.from_dict(data["dynxo"]),
            "dynamics_sidechain": AudioDynamicsSidechain.from_dict(data["dynsc"]),
            "tap_width": data["tapwid"],
            "post_insert_plugin": AudioPostInsertPlugin.from_dict(data["postins"]),
        }
