from typing import Any
from wing_snapfile.models.audio.eq_plugins import (
    WingEQ,
    WingSixBandEQ,
    SoulAnalogue,
    Even88Formant,
    Even84,
    Fortissimo110,
    Pulsar,
    MachEQ4,
    EQPlugin,
)


class WingEQCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> WingEQ:
        return WingEQ(
            low_gain=float(data['lg']),
            low_frequency=float(data['lf']),
            low_q=float(data['lq']),
            low_type=data['leq'],
            band_1_gain=float(data['1g']),
            band_1_frequency=float(data['1f']),
            band_1_q=float(data['1q']),
            band_2_gain=float(data['2g']),
            band_2_frequency=float(data['2f']),
            band_2_q=float(data['2q']),
            band_3_gain=float(data['3g']),
            band_3_frequency=float(data['3f']),
            band_3_q=float(data['3q']),
            band_4_gain=float(data['4g']),
            band_4_frequency=float(data['4f']),
            band_4_q=float(data['4q']),
            high_gain=float(data['hg']),
            high_frequency=float(data['hf']),
            high_q=float(data['hq']),
            high_type=data['heq'],
        )

    @staticmethod
    def encode(obj: WingEQ) -> dict[str, Any]:
        return {
            "lg": obj.low_gain,
            "lf": obj.low_frequency,
            "lq": obj.low_q,
            "leq": obj.low_type,
            "1g": obj.band_1_gain,
            "1f": obj.band_1_frequency,
            "1q": obj.band_1_q,
            "2g": obj.band_2_gain,
            "2f": obj.band_2_frequency,
            "2q": obj.band_2_q,
            "3g": obj.band_3_gain,
            "3f": obj.band_3_frequency,
            "3q": obj.band_3_q,
            "4g": obj.band_4_gain,
            "4f": obj.band_4_frequency,
            "4q": obj.band_4_q,
            "hg": obj.high_gain,
            "hf": obj.high_frequency,
            "hq": obj.high_q,
            "heq": obj.high_type,
        }

class WingSixBandEQCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> WingSixBandEQ:
        return WingSixBandEQ(
            low_gain=float(data['lg']),
            low_frequency=float(data['lf']),
            low_q=float(data['lq']),
            low_type=data['leq'],
            band_1_gain=float(data['1g']),
            band_1_frequency=float(data['1f']),
            band_1_q=float(data['1q']),
            band_2_gain=float(data['2g']),
            band_2_frequency=float(data['2f']),
            band_2_q=float(data['2q']),
            band_3_gain=float(data['3g']),
            band_3_frequency=float(data['3f']),
            band_3_q=float(data['3q']),
            band_4_gain=float(data['4g']),
            band_4_frequency=float(data['4f']),
            band_4_q=float(data['4q']),
            high_gain=float(data['hg']),
            high_frequency=float(data['hf']),
            high_q=float(data['hq']),
            high_type=data['heq'],
            band_5_gain=float(data['5g']),
            band_5_frequency=float(data['5f']),
            band_5_q=float(data['5q']),
            band_6_gain=float(data['6g']),
            band_6_frequency=float(data['6f']),
            band_6_q=float(data['6q']),
            tilt=float(data['tilt']),
        )

    @staticmethod
    def encode(obj: WingSixBandEQ) -> dict[str, Any]:
        return {
            "lg": obj.low_gain,
            "lf": obj.low_frequency,
            "lq": obj.low_q,
            "leq": obj.low_type,
            "1g": obj.band_1_gain,
            "1f": obj.band_1_frequency,
            "1q": obj.band_1_q,
            "2g": obj.band_2_gain,
            "2f": obj.band_2_frequency,
            "2q": obj.band_2_q,
            "3g": obj.band_3_gain,
            "3f": obj.band_3_frequency,
            "3q": obj.band_3_q,
            "4g": obj.band_4_gain,
            "4f": obj.band_4_frequency,
            "4q": obj.band_4_q,
            "hg": obj.high_gain,
            "hf": obj.high_frequency,
            "hq": obj.high_q,
            "heq": obj.high_type,
            "5g": obj.band_5_gain,
            "5f": obj.band_5_frequency,
            "5q": obj.band_5_q,
            "6g": obj.band_6_gain,
            "6f": obj.band_6_frequency,
            "6q": obj.band_6_q,
            "tilt": obj.tilt,
        }

class SoulAnalogueCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> SoulAnalogue:
        return SoulAnalogue(
            low_frequency=float(data['lf']),
            low_gain=float(data['lg']),
            low_mid_frequency=float(data['lmf']),
            low_mid_frequency_x3=data['lmf3'],
            low_mid_q=float(data['lmq']),
            low_mid_gain=float(data['lmg']),
            high_mid_frequency=float(data['hmf']),
            high_mid_frequency_x3=data['hmf3'],
            high_mid_q=float(data['hmq']),
            high_mid_gain=float(data['hmg']),
            high_frequency=float(data['hf']),
            high_gain=float(data['hg']),
        )

    @staticmethod
    def encode(obj: SoulAnalogue) -> dict[str, Any]:
        return {
            "lf": obj.low_frequency,
            "lg": obj.low_gain,
            "lmf": obj.low_mid_frequency,
            "lmf3": obj.low_mid_frequency_x3,
            "lmq": obj.low_mid_q,
            "lmg": obj.low_mid_gain,
            "hmf": obj.high_mid_frequency,
            "hmf3": obj.high_mid_frequency_x3,
            "hmq": obj.high_mid_q,
            "hmg": obj.high_mid_gain,
            "hf": obj.high_frequency,
            "hg": obj.high_gain,
        }

class Even88FormantCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> Even88Formant:
        return Even88Formant(
            low_frequency=float(data['lf']),
            low_gain=float(data['lg']),
            low_q=data['lq'],
            low_type=data['lt'],
            low_mid_frequency=float(data['lmf']),
            low_mid_gain=float(data['lmg']),
            low_mid_q=float(data['lmq']),
            high_mid_frequency=float(data['hmf']),
            high_mid_gain=float(data['hmg']),
            high_mid_q=float(data['hmq']),
            high_frequency=float(data['hf']),
            high_gain=float(data['hg']),
            high_q=data['hq'],
            high_type=data['ht'],
        )

    @staticmethod
    def encode(obj: Even88Formant) -> dict[str, Any]:
        return {
            "lf": obj.low_frequency,
            "lg": obj.low_gain,
            "lq": obj.low_q,
            "lt": obj.low_type,
            "lmf": obj.low_mid_frequency,
            "lmg": obj.low_mid_gain,
            "lmq": obj.low_mid_q,
            "hmf": obj.high_mid_frequency,
            "hmg": obj.high_mid_gain,
            "hmq": obj.high_mid_q,
            "hf": obj.high_frequency,
            "hg": obj.high_gain,
            "hq": obj.high_q,
            "ht": obj.high_type,
        }

class Even84Codec:
    @staticmethod
    def decode(data: dict[str, Any]) -> Even84:
        return Even84(
            gain=float(data['g']),
            low_frequency=data['lf'],
            low_gain=float(data['lg']),
            mid_frequency=data['mf'],
            mid_gain=float(data['mg']),
            mid_q=data['mq'],
            high_frequency=data['hf'],
            high_gain=float(data['hg']),
        )

    @staticmethod
    def encode(obj: Even84) -> dict[str, Any]:
        return {
            "g": obj.gain,
            "lf": obj.low_frequency,
            "lg": obj.low_gain,
            "mf": obj.mid_frequency,
            "mg": obj.mid_gain,
            "mq": obj.mid_q,
            "hf": obj.high_frequency,
            "hg": obj.high_gain,
        }

class Fortissimo110Codec:
    @staticmethod
    def decode(data: dict[str, Any]) -> Fortissimo110:
        return Fortissimo110(
            parametric_eq=data['peq'],
            low_mid_frequency=float(data['lmf']),
            low_mid_gain=float(data['lmg']),
            low_mid_q=float(data['lmq']),
            low_mid_frequency_x3=data['lmf3'],
            high_mid_frequency=float(data['hmf']),
            high_mid_gain=float(data['hmg']),
            high_mid_q=float(data['hmq']),
            high_mid_frequency_x3=data['hmf3'],
            shelving=data['shv'],
            low_frequency=data['lf'],
            low_gain=float(data['lg']),
            high_frequency=data['hf'],
            high_gain=float(data['hg']),
            gain=float(data['g']),
        )

    @staticmethod
    def encode(obj: Fortissimo110) -> dict[str, Any]:
        return {
            "peq": obj.parametric_eq,
            "lmf": obj.low_mid_frequency,
            "lmg": obj.low_mid_gain,
            "lmq": obj.low_mid_q,
            "lmf3": obj.low_mid_frequency_x3,
            "hmf": obj.high_mid_frequency,
            "hmg": obj.high_mid_gain,
            "hmq": obj.high_mid_q,
            "hmf3": obj.high_mid_frequency_x3,
            "shv": obj.shelving,
            "lf": obj.low_frequency,
            "lg": obj.low_gain,
            "hf": obj.high_frequency,
            "hg": obj.high_gain,
            "g": obj.gain,
        }

class PulsarCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> Pulsar:
        return Pulsar(
            eq1_enabled=data['eq1'],
            eq1_low_boost=float(data['1lb']),
            eq1_low_attenuation=float(data['1latt']),
            eq1_low_frequency=data['1lf'],
            eq1_high_width=float(data['1hw']),
            eq1_high_boost=float(data['1hb']),
            eq1_high_frequency=data['1hf'],
            eq1_high_attenuation=float(data['1hatt']),
            eq1_high_attenuation_frequency=data['1hattf'],
            eq5_enabled=data['eq5'],
            eq5_low_boost=float(data['5lb']),
            eq5_low_frequency=data['5lf'],
            eq5_mid_dip=float(data['5md']),
            eq5_mid_frequency=data['5mf'],
            eq5_high_boost=float(data['5hb']),
            eq5_high_frequency=data['5hf'],
        )

    @staticmethod
    def encode(obj: Pulsar) -> dict[str, Any]:
        return {
            "eq1": obj.eq1_enabled,
            "1lb": obj.eq1_low_boost,
            "1latt": obj.eq1_low_attenuation,
            "1lf": obj.eq1_low_frequency,
            "1hw": obj.eq1_high_width,
            "1hb": obj.eq1_high_boost,
            "1hf": obj.eq1_high_frequency,
            "1hatt": obj.eq1_high_attenuation,
            "1hattf": obj.eq1_high_attenuation_frequency,
            "eq5": obj.eq5_enabled,
            "5lb": obj.eq5_low_boost,
            "5lf": obj.eq5_low_frequency,
            "5md": obj.eq5_mid_dip,
            "5mf": obj.eq5_mid_frequency,
            "5hb": obj.eq5_high_boost,
            "5hf": obj.eq5_high_frequency,
        }

class MachEQ4Codec:
    @staticmethod
    def decode(data: dict[str, Any]) -> MachEQ4:
        return MachEQ4(
            sub=float(data['sub']),
            hz_40=float(data['40']),
            hz_160=float(data['160']),
            hz_650=float(data['650']),
            khz_2_5=float(data['2k5']),
            air=float(data['air']),
            air_mode=data['airm'],
            again=data['again'],
        )

    @staticmethod
    def encode(obj: MachEQ4) -> dict[str, Any]:
        return {
            "sub": obj.sub,
            "40": obj.hz_40,
            "160": obj.hz_160,
            "650": obj.hz_650,
            "2k5": obj.khz_2_5,
            "air": obj.air,
            "airm": obj.air_mode,
            "again": obj.again,
        }

PLUGIN_CODEC_MAP: dict[str, type] = {
    "STD": WingEQCodec,
    "SOUL": SoulAnalogueCodec,
    "E88": Even88FormantCodec,
    "E84": Even84Codec,
    "F110": Fortissimo110Codec,
    "PULSAR": PulsarCodec,
    "MACH4": MachEQ4Codec,
}

PLUGIN_MODEL_KEY_MAP: dict[type[EQPlugin], str] = {
    WingEQ: "STD",
    SoulAnalogue: "SOUL",
    Even88Formant: "E88",
    Even84: "E84",
    Fortissimo110: "F110",
    Pulsar: "PULSAR",
    MachEQ4: "MACH4",
}


class EQPluginCodec:
    BASE_KEYS = {"on", "mdl", "mix"}

    @staticmethod
    def decode(data: dict[str, Any]) -> EQPlugin:
        model = data["mdl"]
        plugin_data = {k: v for k, v in data.items() if k not in EQPluginCodec.BASE_KEYS}
        if model == "STD" and "5g" in plugin_data:
            return WingSixBandEQCodec.decode(plugin_data)
        codec = PLUGIN_CODEC_MAP.get(model)
        if codec is None:
            raise KeyError(f"Unknown EQ model: {model}")
        return codec.decode(plugin_data)

    @staticmethod
    def encode(obj: EQPlugin) -> dict[str, Any]:
        if isinstance(obj, WingSixBandEQ):
            return WingSixBandEQCodec.encode(obj)
        model_key = PLUGIN_MODEL_KEY_MAP.get(type(obj))
        if model_key is None:
            raise KeyError(f"Unknown EQ plugin type: {type(obj)}")
        return PLUGIN_CODEC_MAP[model_key].encode(obj)

