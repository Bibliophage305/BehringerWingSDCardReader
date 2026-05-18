from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate
from typing import Type

@dataclass_validate
@dataclass
class EQPlugin:
    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "EQPlugin":
        raise NotImplementedError


@dataclass_validate
@dataclass
class WingEQ(EQPlugin):
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

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "WingEQ":
        return WingEQ(
            low_gain=float(data["lg"]),
            low_frequency=float(data["lf"]),
            low_q=float(data["lq"]),
            low_type=data["leq"],
            band_1_gain=float(data["1g"]),
            band_1_frequency=float(data["1f"]),
            band_1_q=float(data["1q"]),
            band_2_gain=float(data["2g"]),
            band_2_frequency=float(data["2f"]),
            band_2_q=float(data["2q"]),
            band_3_gain=float(data["3g"]),
            band_3_frequency=float(data["3f"]),
            band_3_q=float(data["3q"]),
            band_4_gain=float(data["4g"]),
            band_4_frequency=float(data["4f"]),
            band_4_q=float(data["4q"]),
            high_gain=float(data["hg"]),
            high_frequency=float(data["hf"]),
            high_q=float(data["hq"]),
            high_type=data["heq"],
        )


@dataclass_validate
@dataclass
class SoulAnalogue(EQPlugin):
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

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "SoulAnalogue":
        return SoulAnalogue(
            low_frequency=float(data["lf"]),
            low_gain=float(data["lg"]),
            low_mid_frequency=float(data["lmf"]),
            low_mid_frequency_x3=data["lmf3"],
            low_mid_q=float(data["lmq"]),
            low_mid_gain=float(data["lmg"]),
            high_mid_frequency=float(data["hmf"]),
            high_mid_frequency_x3=data["hmf3"],
            high_mid_q=float(data["hmq"]),
            high_mid_gain=float(data["hmg"]),
            high_frequency=float(data["hf"]),
            high_gain=float(data["hg"]),
        )


@dataclass_validate
@dataclass
class Even88Formant(EQPlugin):
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

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Even88Formant":
        return Even88Formant(
            low_frequency=float(data["lf"]),
            low_gain=float(data["lg"]),
            low_q=data["lq"],
            low_type=data["lt"],
            low_mid_frequency=float(data["lmf"]),
            low_mid_gain=float(data["lmg"]),
            low_mid_q=float(data["lmq"]),
            high_mid_frequency=float(data["hmf"]),
            high_mid_gain=float(data["hmg"]),
            high_mid_q=float(data["hmq"]),
            high_frequency=float(data["hf"]),
            high_gain=float(data["hg"]),
            high_q=data["hq"],
            high_type=data["ht"],
        )


@dataclass_validate
@dataclass
class Even84(EQPlugin):
    gain: float
    low_frequency: str
    low_gain: float
    mid_frequency: str
    mid_gain: float
    mid_q: str
    high_frequency: str
    high_gain: float

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Even84":
        return Even84(
            gain=float(data["g"]),
            low_frequency=data["lf"],
            low_gain=float(data["lg"]),
            mid_frequency=data["mf"],
            mid_gain=float(data["mg"]),
            mid_q=data["mq"],
            high_frequency=data["hf"],
            high_gain=float(data["hg"]),
        )


@dataclass_validate
@dataclass
class Fortissimo110(EQPlugin):
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

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Fortissimo110":
        return Fortissimo110(
            parametric_eq=data["peq"],
            low_mid_frequency=float(data["lmf"]),
            low_mid_gain=float(data["lmg"]),
            low_mid_q=float(data["lmq"]),
            low_mid_frequency_x3=data["lmf3"],
            high_mid_frequency=float(data["hmf"]),
            high_mid_gain=float(data["hmg"]),
            high_mid_q=float(data["hmq"]),
            high_mid_frequency_x3=data["hmf3"],
            shelving=data["shv"],
            low_frequency=data["lf"],
            low_gain=float(data["lg"]),
            high_frequency=data["hf"],
            high_gain=float(data["hg"]),
            gain=float(data["g"]),
        )


@dataclass_validate
@dataclass
class Pulsar(EQPlugin):
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

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Pulsar":
        return Pulsar(
            eq1_enabled=data["eq1"],
            eq1_low_boost=float(data["1lb"]),
            eq1_low_attenuation=float(data["1latt"]),
            eq1_low_frequency=data["1lf"],
            eq1_high_width=float(data["1hw"]),
            eq1_high_boost=float(data["1hb"]),
            eq1_high_frequency=data["1hf"],
            eq1_high_attenuation=float(data["1hatt"]),
            eq1_high_attenuation_frequency=data["1hattf"],
            eq5_enabled=data["eq5"],
            eq5_low_boost=float(data["5lb"]),
            eq5_low_frequency=data["5lf"],
            eq5_mid_dip=float(data["5md"]),
            eq5_mid_frequency=data["5mf"],
            eq5_high_boost=float(data["5hb"]),
            eq5_high_frequency=data["5hf"],
        )


@dataclass_validate
@dataclass
class MachEQ4(EQPlugin):
    sub: float
    hz_40: float
    hz_160: float
    hz_650: float
    khz_2_5: float
    air: float
    air_mode: str
    again: bool

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "MachEQ4":
        return MachEQ4(
            sub=float(data["sub"]),
            hz_40=float(data["40"]),
            hz_160=float(data["160"]),
            hz_650=float(data["650"]),
            khz_2_5=float(data["2k5"]),
            air=float(data["air"]),
            air_mode=data["airm"],
            again=data["again"],
        )


PLUGIN_MODEL_MAP: dict[str, Type[EQPlugin]] = {
    "STD": WingEQ,
    "SOUL": SoulAnalogue,
    "E88": Even88Formant,
    "E84": Even84,
    "F110": Fortissimo110,
    "PULSAR": Pulsar,
    "MACH4": MachEQ4,
}


def parse_eq_plugin(data: dict[str, object]) -> EQPlugin:
    model = data["mdl"]
    plugin_cls = PLUGIN_MODEL_MAP[model]
    plugin_data = {k: v for k, v in data.items() if k not in {"on", "mdl", "mix"}}
    return plugin_cls.from_dict(plugin_data)

