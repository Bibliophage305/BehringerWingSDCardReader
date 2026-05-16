from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

@dataclass_validate
@dataclass
class AudioEngineFilter:
    low_cut_enabled: bool
    low_cut_frequency: float
    low_cut_slope: str
    high_cut_enabled: bool
    high_cut_frequency: float
    high_cut_slope: str
    tilt_enabled: bool
    tilt_mode: str
    tilt_amount: float

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioEngineFilter":
        return AudioEngineFilter(
            low_cut_enabled=data["lc"],
            low_cut_frequency=float(data["lcf"]),
            low_cut_slope=data["lcs"],
            high_cut_enabled=data["hc"],
            high_cut_frequency=float(data["hcf"]),
            high_cut_slope=data["hcs"],
            tilt_enabled=data["tf"],
            tilt_mode=data["mdl"],
            tilt_amount=float(data["tilt"])
        )
