import msgspec


class AudioMonitorEQ(msgspec.Struct, kw_only=True):
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


class AudioMonitorDelay(msgspec.Struct, kw_only=True):
    on: bool
    metres: float


class AudioMonitor(msgspec.Struct, kw_only=True):
    fader_level: float
    phase_invert: bool

    pan: int
    width: int

    eq: AudioMonitorEQ
    limiter_threshold: int
    delay: AudioMonitorDelay

    dim: int
    pfl_dim: int
    band_solo_trim: int

    source_level: float
    source_mix: float

    source: str
    direct_input: str

    tags: list[str]