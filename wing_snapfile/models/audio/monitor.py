from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate


@dataclass_validate
@dataclass(kw_only=True)
class MonitorEQ:
    on: bool

    lsg: float
    lsf: float

    g1: float
    f1: float
    q1: float

    g2: float
    f2: float
    q2: float

    g3: float
    f3: float
    q3: float

    g4: float
    f4: float
    q4: float

    g5: float
    f5: float
    q5: float

    g6: float
    f6: float
    q6: float

    hsg: float
    hsf: float


@dataclass_validate
@dataclass(kw_only=True)
class MonitorDelay:
    on: bool
    metres: float


@dataclass_validate
@dataclass(kw_only=True)
class Monitor:
    fader_level: float
    phase_invert: bool

    pan: int
    width: int

    eq: MonitorEQ
    limiter_threshold: int
    delay: MonitorDelay

    dim: int
    pfl_dim: int
    band_solo_trim: int

    source_level: float
    source_mix: float

    source: str
    direct_input: str

    tags: list[str]