from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate


@dataclass_validate
@dataclass
class AudioInputConnections:
    group: str
    input: int
    alt_group: str
    alt_input: int

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioInputConnections":
        return AudioInputConnections(
            group=data["grp"],
            input=data["in"],
            alt_group=data["altgrp"],
            alt_input=data["altin"],
        )

    def to_dict(self):
        return {
            "grp": self.group,
            "in": self.input,
            "altgrp": self.alt_group,
            "altin": self.alt_input,
        }
