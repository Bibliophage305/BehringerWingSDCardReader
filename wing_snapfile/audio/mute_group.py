from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

@dataclass_validate
@dataclass
class AudioMuteGroup:
    name: str
    mute_on: bool

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data["name"],
            mute_on=data["mute"],
        )
