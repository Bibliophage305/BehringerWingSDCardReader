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
    
    def to_dict(self):
        return {
            "on": self.on,
            "lvl": self.fader_level,
        }

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
    
    def to_dict(self):
        return {
            **super().to_dict(),
            "pre": self.pre_fader,
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
    
    def to_dict(self):
        return {
            **super().to_dict(),
            "pon": self.pre_always_on,
            "mode": self.mode,
            "plink": self.pan_link,
            "pan": self.pan,
        }
