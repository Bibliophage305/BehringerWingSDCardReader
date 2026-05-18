from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

class SourceSwitchable:
    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            "auto_source_switch": data["srcauto"],
            "use_alternate_source": data["altsrc"],
        }
    
    def to_dict(self):
        return {
            "srcauto": self.auto_source_switch,
            "altsrc": self.use_alternate_source,
        }

class Delayable:
    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            "delay_mode": data["dlymode"],
            "delay_amount": float(data["dly"]),
            "delay_on": data["dlyon"]
        }
    
    def to_dict(self):
        return {
            "dlymode": self.delay_mode,
            "dly": self.delay_amount,
            "dlyon": self.delay_on,
        }

@dataclass_validate
@dataclass
class AudioInputSettings:
    is_phase_inverted: bool
    trim: float
    balance: float

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            "is_phase_inverted": data["inv"],
            "trim": float(data["trim"]),
            "balance": float(data["bal"]),
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**cls._from_dict_kwargs(data))
    
    def to_dict(self):
        return {
            "inv": self.is_phase_inverted,
            "trim": self.trim,
            "bal": self.balance,
        }


@dataclass_validate
@dataclass
class AudioSourceSwitchableDelayableInputSettings(AudioInputSettings, SourceSwitchable, Delayable):
    auto_source_switch: bool
    use_alternate_source: bool
    is_phase_inverted: bool
    trim: float
    balance: float
    delay_mode: str
    delay_amount: float
    delay_on: bool

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioInputSettings._from_dict_kwargs(data),
            **SourceSwitchable._from_dict_kwargs(data),
            **Delayable._from_dict_kwargs(data),
        }
    
    def to_dict(self):
        return {
            **AudioInputSettings.to_dict(self),
            **SourceSwitchable.to_dict(self),
            **Delayable.to_dict(self),
        }
