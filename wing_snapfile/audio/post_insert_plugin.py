from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

@dataclass_validate
@dataclass
class AudioPostInsertPlugin:
    on: bool
    mode: str
    insert: str
    autogain_weight: float

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioPostInsertPlugin":
        return AudioPostInsertPlugin(
            on=data["on"],
            mode=data["mode"],
            insert=data["ins"],
            autogain_weight=float(data["w"])
        )
