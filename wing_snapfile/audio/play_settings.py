from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

@dataclass_validate
@dataclass
class AudioPlaySettings:
    repeat: bool

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            repeat=data["repeat"]
        )
    
    def to_dict(self):
        return {
            "repeat": self.repeat,
        }
