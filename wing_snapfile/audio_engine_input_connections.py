from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

@dataclass_validate
@dataclass
class AudioEngineInputConnections:
    group: str
    input: int
    alt_group: str
    alt_input: int

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioEngineInputConnections":
        return AudioEngineInputConnections(
            group=data["grp"],
            input=data["in"],
            alt_group=data["altgrp"],
            alt_input=data["altin"]
        )
