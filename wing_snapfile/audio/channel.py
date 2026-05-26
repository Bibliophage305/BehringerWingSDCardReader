from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

from wing_snapfile.audio.dynamics_crossover import AudioDynamicsCrossover
from wing_snapfile.audio.dynamics_sidechain import AudioDynamicsSidechain
from wing_snapfile.audio.eq import AudioEQ
from wing_snapfile.audio.input import (
    AudioInput,
    AudioRoutableInput,
    AudioSourceSwitchableDelayableInput,
)
from wing_snapfile.audio.filter import AudioFilter
from wing_snapfile.audio.tap_eq import AudioTapEQ
from wing_snapfile.audio.gate_sidechain import AudioGateSidechain
from wing_snapfile.audio.dynamics import AudioDynamics
from wing_snapfile.audio.pre_insert_plugin import AudioPreInsertPlugin
from wing_snapfile.audio.post_insert_plugin import (
    AudioPostInsertPlugin,
    AudioPostInsertPluginWithAutomix,
)
from wing_snapfile.audio.send import AudioFullSend, AudioLimitedSend

from wing_snapfile.types.one_indexed_list import OneIndexedList


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

    def to_dict(self):
        return {
            "in": self.input.to_dict(),
            "clink": self.link_customization_to_source,
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

    def to_dict(self):
        return {
            "solosafe": self.solo_safe,
        }


@dataclass_validate
@dataclass
class DelaySettings:
    on: bool
    delay_mode: str
    delay_amount: float

    @classmethod
    def from_dict(cls, data):
        return cls(
            on=data["on"],
            delay_mode=data["mode"],
            delay_amount=float(data["dly"]),
        )

    def to_dict(self):
        return {
            "on": self.on,
            "mode": self.delay_mode,
            "dly": self.delay_amount,
        }


@dataclass_validate
@dataclass
class Delayable:
    delay_settings: DelaySettings

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            "delay_settings": DelaySettings.from_dict(data["dly"]),
        }

    def to_dict(self):
        return {
            "dly": self.delay_settings.to_dict(),
        }


@dataclass_validate
@dataclass
class DynamicsSidechainable:
    dynamics_sidechain: AudioDynamicsSidechain

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            "dynamics_sidechain": AudioDynamicsSidechain.from_dict(data["dynsc"]),
        }

    def to_dict(self):
        return {
            "dynsc": self.dynamics_sidechain.to_dict(),
        }


@dataclass_validate
@dataclass
class DynamicsFullyProcessable(DynamicsSidechainable):
    dynamics_crossover: AudioDynamicsCrossover

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **DynamicsSidechainable._from_dict_kwargs(data),
            "dynamics_crossover": AudioDynamicsCrossover.from_dict(data["dynxo"]),
        }

    def to_dict(self):
        return {
            **super().to_dict(),
            "dynxo": self.dynamics_crossover.to_dict(),
        }


@dataclass_validate
@dataclass
class WithPostInsertPlugin:
    post_insert_plugin: AudioPostInsertPlugin

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            "post_insert_plugin": AudioPostInsertPlugin.from_dict(data["postins"]),
        }

    def to_dict(self):
        return {
            "postins": self.post_insert_plugin.to_dict(),
        }


@dataclass_validate
@dataclass
class WithPostInsertPluginWithAutomix:
    post_insert_plugin: AudioPostInsertPluginWithAutomix

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            "post_insert_plugin": AudioPostInsertPluginWithAutomix.from_dict(
                data["postins"]
            ),
        }

    def to_dict(self):
        return {
            "postins": self.post_insert_plugin.to_dict(),
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

    def to_dict(self):
        return self.bus_sends.to_dict()


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

    def to_dict(self):
        return self.bus_sends.to_dict()


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

    def to_dict(self):
        return self.matrix_sends.to_dict(prefix="MX")


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

    def to_dict(self):
        return self.matrix_sends.to_dict(prefix="MX")


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

    def to_dict(self):
        return self.main_sends.to_dict()


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

    def to_dict(self):
        return {
            "in": self.input.to_dict(),
            "col": self.color,
            "name": self.name,
            "icon": self.icon,
            "led": self.led_on,
            "mute": self.mute_on,
            "fdr": self.fader_level,
            "pan": self.pan,
            "wid": self.width,
            "mon": self.monitor_mode,
            "eq": self.eq_plugin.to_dict(),
            "dyn": self.dynamics_plugin.to_dict(),
            "preins": self.pre_insert_plugin.to_dict(),
            "tags": ",".join(self.tags),
        }


@dataclass_validate
@dataclass
class AudioBusChannel(
    AudioChannel,
    LimitedBusSendable,
    LimitedMatrixSendable,
    MainSendable,
    DynamicsFullyProcessable,
    WithPostInsertPlugin,
    Delayable,
):
    mono_bus: bool

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioChannel._from_dict_kwargs(data),
            **LimitedBusSendable._from_dict_kwargs(data),
            **LimitedMatrixSendable._from_dict_kwargs(data),
            **MainSendable._from_dict_kwargs(data),
            **DynamicsFullyProcessable._from_dict_kwargs(data),
            **WithPostInsertPlugin._from_dict_kwargs(data),
            **Delayable._from_dict_kwargs(data),
            "mono_bus": data["busmono"],
        }

    def to_dict(self):
        return {
            **super().to_dict(),
            **DynamicsFullyProcessable.to_dict(self),
            **WithPostInsertPlugin.to_dict(self),
            **Delayable.to_dict(self),
            "send": {
                **LimitedBusSendable.to_dict(self),
                **LimitedMatrixSendable.to_dict(self),
            },
            "main": MainSendable.to_dict(self),
            "busmono": self.mono_bus,
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

    def to_dict(self):
        return {
            "on": self.direct_input,
            "lvl": self.fader_level,
            "inv": self.phase_invert,
            "in": self.input_selector,
        }


@dataclass_validate
@dataclass
class AudioMatrixChannel(
    AudioChannel, DynamicsFullyProcessable, WithPostInsertPlugin, Delayable
):
    direct_input_settings: AudioDirectInput
    mono_bus: bool

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioChannel._from_dict_kwargs(data),
            **DynamicsFullyProcessable._from_dict_kwargs(data),
            **WithPostInsertPlugin._from_dict_kwargs(data),
            **Delayable._from_dict_kwargs(data),
            "direct_input_settings": AudioDirectInput.from_dict(data["dir"]),
            "mono_bus": data["busmono"],
        }

    def to_dict(self):
        return {
            **super().to_dict(),
            **DynamicsFullyProcessable.to_dict(self),
            **WithPostInsertPlugin.to_dict(self),
            **Delayable.to_dict(self),
            "dir": self.direct_input_settings.to_dict(),
            "busmono": self.mono_bus,
        }


@dataclass_validate
@dataclass
class AudioMainChannel(
    AudioChannel,
    LimitedBusSendable,
    LimitedMatrixSendable,
    Delayable,
    DynamicsFullyProcessable,
    WithPostInsertPlugin,
):
    mono_bus: bool

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioChannel._from_dict_kwargs(data),
            **LimitedBusSendable._from_dict_kwargs(data),
            **LimitedMatrixSendable._from_dict_kwargs(data),
            **Delayable._from_dict_kwargs(data),
            **DynamicsFullyProcessable._from_dict_kwargs(data),
            **WithPostInsertPlugin._from_dict_kwargs(data),
            "mono_bus": data["busmono"],
        }

    def to_dict(self):
        return {
            **super().to_dict(),
            "send": {
                **LimitedBusSendable.to_dict(self),
                **LimitedMatrixSendable.to_dict(self),
            },
            **Delayable.to_dict(self),
            **DynamicsFullyProcessable.to_dict(self),
            **WithPostInsertPlugin.to_dict(self),
            "busmono": self.mono_bus,
        }


@dataclass_validate
@dataclass
class AudioAuxChannel(
    AudioChannel,
    Routable,
    Soloable,
    FullBusSendable,
    FullMatrixSendable,
    MainSendable,
    DynamicsSidechainable,
):
    input: AudioSourceSwitchableDelayableInput

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioChannel._from_dict_kwargs(data),
            **Routable._from_dict_kwargs(data),
            **Soloable._from_dict_kwargs(data),
            **FullBusSendable._from_dict_kwargs(data),
            **FullMatrixSendable._from_dict_kwargs(data),
            **MainSendable._from_dict_kwargs(data),
            **DynamicsSidechainable._from_dict_kwargs(data),
            "input": AudioSourceSwitchableDelayableInput.from_dict(data["in"]),
        }

    def to_dict(self):
        return {
            **super().to_dict(),
            **Routable.to_dict(self),
            **Soloable.to_dict(self),
            "send": {
                **FullBusSendable.to_dict(self),
                **FullMatrixSendable.to_dict(self),
            },
            "main": MainSendable.to_dict(self),
            **DynamicsSidechainable.to_dict(self),
            # "in": self.input.to_dict(),
        }


@dataclass_validate
@dataclass
class AudioFullChannel(
    AudioChannel,
    Routable,
    Soloable,
    DynamicsFullyProcessable,
    WithPostInsertPluginWithAutomix,
    FullBusSendable,
    FullMatrixSendable,
    MainSendable,
):
    input: AudioSourceSwitchableDelayableInput
    filter: AudioFilter
    processing_order: str
    processing_tap_point: str
    tap_eq: AudioTapEQ
    gate_plugin: AudioDynamics
    gate_sidechain: AudioGateSidechain
    tap_width: int

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioChannel._from_dict_kwargs(data),
            **Routable._from_dict_kwargs(data),
            **Soloable._from_dict_kwargs(data),
            **DynamicsFullyProcessable._from_dict_kwargs(data),
            **WithPostInsertPluginWithAutomix._from_dict_kwargs(data),
            **FullBusSendable._from_dict_kwargs(data),
            **FullMatrixSendable._from_dict_kwargs(data),
            **MainSendable._from_dict_kwargs(data),
            "input": AudioSourceSwitchableDelayableInput.from_dict(data["in"]),
            "filter": AudioFilter.from_dict(data["flt"]),
            "processing_order": data["proc"],
            "processing_tap_point": data["ptap"],
            "tap_eq": AudioTapEQ.from_dict(data["peq"]),
            "gate_plugin": AudioDynamics.from_dict(data["gate"]),
            "gate_sidechain": AudioGateSidechain.from_dict(data["gatesc"]),
            "dynamics_crossover": AudioDynamicsCrossover.from_dict(data["dynxo"]),
            "dynamics_sidechain": AudioDynamicsSidechain.from_dict(data["dynsc"]),
            "tap_width": data["tapwid"],
        }

    def to_dict(self):
        return {
            **super().to_dict(),
            **Routable.to_dict(self),
            **Soloable.to_dict(self),
            **DynamicsFullyProcessable.to_dict(self),
            **WithPostInsertPluginWithAutomix.to_dict(self),
            "in": self.input.to_dict(),
            "send": {
                **FullBusSendable.to_dict(self),
                **FullMatrixSendable.to_dict(self),
            },
            "main": MainSendable.to_dict(self),
            "flt": self.filter.to_dict(),
            "proc": self.processing_order,
            "ptap": self.processing_tap_point,
            "peq": self.tap_eq.to_dict(),
            "gate": self.gate_plugin.to_dict(),
            "gatesc": self.gate_sidechain.to_dict(),
            "dynxo": self.dynamics_crossover.to_dict(),
            "dynsc": self.dynamics_sidechain.to_dict(),
            "tapwid": self.tap_width,
        }
