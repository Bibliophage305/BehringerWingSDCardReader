from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

@dataclass_validate
@dataclass
class AudioGateSidechain:
    type: str
    frequency: float
    q: float
    source: str
    tap: str

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioGateSidechain":
        return AudioGateSidechain(
            type=data["type"],
            frequency=float(data["f"]),
            q=float(data["q"]),
            source=data["src"],
            tap=data["tap"]
        )
