from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

@dataclass_validate
@dataclass
class AudioPostInsertPlugin:
    on: bool
    insert: str

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            "on": data["on"],
            "insert": data["ins"],
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**cls._from_dict_kwargs(data))
    
    def to_dict(self):
        return {
            "on": self.on,
            "ins": self.insert,
        }


@dataclass_validate
@dataclass
class AudioPostInsertPluginWithAutomix(AudioPostInsertPlugin):
    mode: str
    autogain_weight: float

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioPostInsertPlugin._from_dict_kwargs(data),
            "mode": data["mode"],
            "autogain_weight": float(data["w"]),
        }
    
    def to_dict(self):
        return {
            "on": self.on,
            "mode": self.mode,
            "ins": self.insert,
            "w": self.autogain_weight,
        }
