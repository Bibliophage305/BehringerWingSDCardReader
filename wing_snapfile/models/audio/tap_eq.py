from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate


@dataclass_validate
@dataclass(kw_only=True)
class TapEQ:
    on: bool
    band1_gain: float
    band1_freq: float
    band1_q: float
    band2_gain: float
    band2_freq: float
    band2_q: float
    band3_gain: float
    band3_freq: float
    band3_q: float
