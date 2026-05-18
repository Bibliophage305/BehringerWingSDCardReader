from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

@dataclass_validate
@dataclass
class AudioDynamicsSidechain:
    type: str
    frequency: float
    q: float
    source: str
    tap: str

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioDynamicsSidechain":
        return AudioDynamicsSidechain(
            type=data["type"],
            frequency=float(data["f"]),
            q=float(data["q"]),
            source=data["src"],
            tap=data["tap"]
        )
