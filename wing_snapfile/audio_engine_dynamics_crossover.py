from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

@dataclass_validate
@dataclass
class AudioEngineDynamicsCrossover:
    depth: int
    type: str
    frequency: float

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioEngineDynamicsCrossover":
        return AudioEngineDynamicsCrossover(
            depth=data["depth"],
            type=data["type"],
            frequency=float(data["f"])
        )
