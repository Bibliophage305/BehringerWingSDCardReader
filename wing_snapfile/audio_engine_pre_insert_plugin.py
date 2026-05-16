from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

@dataclass_validate
@dataclass
class AudioEnginePreInsertPlugin:
    on: bool
    insert: str

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioEnginePreInsertPlugin":
        return AudioEnginePreInsertPlugin(
            on=data["on"],
            insert=data["ins"]
        )
