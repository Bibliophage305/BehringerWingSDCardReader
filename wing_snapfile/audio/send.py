from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

@dataclass_validate
@dataclass
class AudioSend:
    on: bool
    fader_level: float

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            "on": data["on"],
            "fader_level": float(data["lvl"]),
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**cls._from_dict_kwargs(data))

@dataclass_validate
@dataclass
class AudioLimitedSend(AudioSend):
    pre_fader: bool

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioSend._from_dict_kwargs(data),
            "pre_fader": data["pre"],
        }

@dataclass_validate
@dataclass
class AudioFullSend(AudioSend):
    pre_always_on: bool
    mode: str
    pan_link: int
    pan: int

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioSend._from_dict_kwargs(data),
            "pre_always_on": data["pon"],
            "mode": data["mode"],
            "pan_link": data["plink"],
            "pan": int(data["pan"]),
        }
