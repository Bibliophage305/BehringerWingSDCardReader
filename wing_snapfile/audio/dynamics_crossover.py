from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

@dataclass_validate
@dataclass
class AudioDynamicsCrossover:
    depth: int
    type: str
    frequency: float
    q: float

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioDynamicsCrossover":
        return AudioDynamicsCrossover(
            depth=data["depth"],
            type=data["type"],
            frequency=float(data["f"]),
            q=float(data["q"])
        )
    
    def to_dict(self):
        return {
            "depth": self.depth,
            "type": self.type,
            "f": self.frequency,
            "q": self.q,
        }
