from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate


@dataclass_validate
@dataclass(kw_only=True)
class Filter:
    low_cut_enabled: bool
    low_cut_frequency: float
    low_cut_slope: str
    high_cut_enabled: bool
    high_cut_frequency: float
    high_cut_slope: str
    tilt_enabled: bool
    tilt_mode: str
    tilt_amount: float
