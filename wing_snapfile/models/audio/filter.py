import msgspec


class AudioFilter(msgspec.Struct, kw_only=True):
    low_cut_enabled: bool
    low_cut_frequency: float
    low_cut_slope: str
    high_cut_enabled: bool
    high_cut_frequency: float
    high_cut_slope: str
    tilt_enabled: bool
    tilt_mode: str
    tilt_amount: float
