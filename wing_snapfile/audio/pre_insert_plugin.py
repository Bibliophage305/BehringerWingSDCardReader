from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate


@dataclass_validate
@dataclass
class AudioPreInsertPlugin:
    on: bool
    insert: str

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioPreInsertPlugin":
        return AudioPreInsertPlugin(on=data["on"], insert=data["ins"])

    def to_dict(self):
        return {
            "on": self.on,
            "ins": self.insert,
        }
