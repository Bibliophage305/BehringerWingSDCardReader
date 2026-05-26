import msgspec
from typing import Union


class WingEQ(msgspec.Struct, kw_only=True):
    low_gain: float
    low_frequency: float
    low_q: float
    low_type: str
    band_1_gain: float
    band_1_frequency: float
    band_1_q: float
    band_2_gain: float
    band_2_frequency: float
    band_2_q: float
    band_3_gain: float
    band_3_frequency: float
    band_3_q: float
    band_4_gain: float
    band_4_frequency: float
    band_4_q: float
    high_gain: float
    high_frequency: float
    high_q: float
    high_type: str

class WingSixBandEQ(WingEQ):
    band_5_gain: float
    band_5_frequency: float
    band_5_q: float
    band_6_gain: float
    band_6_frequency: float
    band_6_q: float
    tilt: float

class SoulAnalogue(msgspec.Struct, kw_only=True):
    low_frequency: float
    low_gain: float
    low_mid_frequency: float
    low_mid_frequency_x3: bool
    low_mid_q: float
    low_mid_gain: float
    high_mid_frequency: float
    high_mid_frequency_x3: bool
    high_mid_q: float
    high_mid_gain: float
    high_frequency: float
    high_gain: float

class Even88Formant(msgspec.Struct, kw_only=True):
    low_frequency: float
    low_gain: float
    low_q: str
    low_type: str
    low_mid_frequency: float
    low_mid_gain: float
    low_mid_q: float
    high_mid_frequency: float
    high_mid_gain: float
    high_mid_q: float
    high_frequency: float
    high_gain: float
    high_q: str
    high_type: str

class Even84(msgspec.Struct, kw_only=True):
    gain: float
    low_frequency: str
    low_gain: float
    mid_frequency: str
    mid_gain: float
    mid_q: str
    high_frequency: str
    high_gain: float

class Fortissimo110(msgspec.Struct, kw_only=True):
    parametric_eq: bool
    low_mid_frequency: float
    low_mid_gain: float
    low_mid_q: float
    low_mid_frequency_x3: bool
    high_mid_frequency: float
    high_mid_gain: float
    high_mid_q: float
    high_mid_frequency_x3: bool
    shelving: bool
    low_frequency: str
    low_gain: float
    high_frequency: str
    high_gain: float
    gain: float

class Pulsar(msgspec.Struct, kw_only=True):
    eq1_enabled: bool
    eq1_low_boost: float
    eq1_low_attenuation: float
    eq1_low_frequency: str
    eq1_high_width: float
    eq1_high_boost: float
    eq1_high_frequency: str
    eq1_high_attenuation: float
    eq1_high_attenuation_frequency: str
    eq5_enabled: bool
    eq5_low_boost: float
    eq5_low_frequency: str
    eq5_mid_dip: float
    eq5_mid_frequency: str
    eq5_high_boost: float
    eq5_high_frequency: str

class MachEQ4(msgspec.Struct, kw_only=True):
    sub: float
    hz_40: float
    hz_160: float
    hz_650: float
    khz_2_5: float
    air: float
    air_mode: str
    again: bool


EQPlugin = Union[WingEQ, WingSixBandEQ, SoulAnalogue, Even88Formant, Even84, Fortissimo110, Pulsar, MachEQ4]

PLUGIN_MODEL_MAP: dict[str, type[EQPlugin]] = {
    "STD": WingEQ,
    "SOUL": SoulAnalogue,
    "E88": Even88Formant,
    "E84": Even84,
    "F110": Fortissimo110,
    "PULSAR": Pulsar,
    "MACH4": MachEQ4,
}
