from typing import Any
from wing_snapfile.models.audio.dynamics_plugins import (
    AudioDynamicsPlugin,
    WingGate,
    WingDucker,
    Even88Gate,
    DrawMore241,
    Soul9000Gate,
    DynamicEQ,
    DualDynamicEQ,
    BDX902DeEsser,
    WaveDesigner,
    AutoRider,
    SoulWarmthPre,
    WingCompressor,
    WingExpander,
    Even88Comp,
    OneKnobComp,
    Soul9000,
    BDX160Comp,
    BDX560Easy,
    Red3Compressor,
    LMTCompressor,
    SoulBusComp,
    PIA2250Rack,
    LimiterAmp76,
    LALeveler,
    FairKid,
    LTA100Leveler,
    EternalBliss,
    NoStressor,
    SourceExtractor,
    PSELACombo,
    EvenCompLim,
    DrawMoreComp,
)

class WingGateCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> WingGate:
        return WingGate(
            threshold=float(data['thr']),
            range=float(data['range']),
            attack=data['att'],
            hold=data['hld'],
            release=data['rel'],
            accent=data['acc'],
            ratio=data['ratio'],
        )

    @staticmethod
    def encode(obj: WingGate) -> dict[str, Any]:
        return {
            "thr": obj.threshold,
            "range": obj.range,
            "att": obj.attack,
            "hld": obj.hold,
            "rel": obj.release,
            "acc": obj.accent,
            "ratio": obj.ratio,
        }

class WingDuckerCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> WingDucker:
        return WingDucker(
            threshold=float(data['thr']),
            range=float(data['range']),
            attack=data['att'],
            hold=float(data['hld']),
            release=float(data['rel']),
        )

    @staticmethod
    def encode(obj: WingDucker) -> dict[str, Any]:
        return {
            "thr": obj.threshold,
            "range": obj.range,
            "att": obj.attack,
            "hld": obj.hold,
            "rel": obj.release,
        }

class Even88GateCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> Even88Gate:
        return Even88Gate(
            threshold=float(data['thr']),
            hysteresis=float(data['hyst']),
            range=float(data['range']),
            release=float(data['rel']),
            fast=data['fast'],
            m40=data['m40'],
        )

    @staticmethod
    def encode(obj: Even88Gate) -> dict[str, Any]:
        return {
            "thr": obj.threshold,
            "hyst": obj.hysteresis,
            "range": obj.range,
            "rel": obj.release,
            "fast": obj.fast,
            "m40": obj.m40,
        }

class DrawMore241Codec:
    @staticmethod
    def decode(data: dict[str, Any]) -> DrawMore241:
        return DrawMore241(
            threshold=float(data['thr']),
            slow=data['slow'],
        )

    @staticmethod
    def encode(obj: DrawMore241) -> dict[str, Any]:
        return {
            "thr": obj.threshold,
            "slow": obj.slow,
        }

class Soul9000GateCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> Soul9000Gate:
        return Soul9000Gate(
            threshold=float(data['thr']),
            range=float(data['range']),
            hold=float(data['hld']),
            release=float(data['rel']),
            fast=data['fast'],
            mode=data['mode'],
        )

    @staticmethod
    def encode(obj: Soul9000Gate) -> dict[str, Any]:
        return {
            "thr": obj.threshold,
            "range": obj.range,
            "hld": obj.hold,
            "rel": obj.release,
            "fast": obj.fast,
            "mode": obj.mode,
        }

class DynamicEQCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> DynamicEQ:
        return DynamicEQ(
            threshold=float(data['thr']),
            ratio=float(data['ratio']),
            attack=float(data['att']),
            release=float(data['rel']),
            filter_type=data['filt'],
            gain=float(data['g']),
            frequency=float(data['f']),
            q=float(data['q']),
            mode=data['mode'],
        )

    @staticmethod
    def encode(obj: DynamicEQ) -> dict[str, Any]:
        return {
            "thr": obj.threshold,
            "ratio": obj.ratio,
            "att": obj.attack,
            "rel": obj.release,
            "filt": obj.filter_type,
            "g": obj.gain,
            "f": obj.frequency,
            "q": obj.q,
            "mode": obj.mode,
        }

class DualDynamicEQCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> DualDynamicEQ:
        return DualDynamicEQ(
            band1_threshold=float(data['1-thr']),
            band1_ratio=float(data['1-ratio']),
            band1_attack=float(data['1-att']),
            band1_release=float(data['1-rel']),
            band1_filter_type=data['1-filt'],
            band1_gain=float(data['1-g']),
            band1_frequency=float(data['1-f']),
            band1_q=float(data['1-q']),
            band1_mode=data['1-mode'],
            band2_threshold=float(data['2-thr']),
            band2_ratio=float(data['2-ratio']),
            band2_attack=float(data['2-att']),
            band2_release=float(data['2-rel']),
            band2_filter_type=data['2-filt'],
            band2_gain=float(data['2-g']),
            band2_frequency=float(data['2-f']),
            band2_q=float(data['2-q']),
            band2_mode=data['2-mode'],
        )

    @staticmethod
    def encode(obj: DualDynamicEQ) -> dict[str, Any]:
        return {
            "1-thr": obj.band1_threshold,
            "1-ratio": obj.band1_ratio,
            "1-att": obj.band1_attack,
            "1-rel": obj.band1_release,
            "1-filt": obj.band1_filter_type,
            "1-g": obj.band1_gain,
            "1-f": obj.band1_frequency,
            "1-q": obj.band1_q,
            "1-mode": obj.band1_mode,
            "2-thr": obj.band2_threshold,
            "2-ratio": obj.band2_ratio,
            "2-att": obj.band2_attack,
            "2-rel": obj.band2_release,
            "2-filt": obj.band2_filter_type,
            "2-g": obj.band2_gain,
            "2-f": obj.band2_frequency,
            "2-q": obj.band2_q,
            "2-mode": obj.band2_mode,
        }

class BDX902DeEsserCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> BDX902DeEsser:
        return BDX902DeEsser(
            frequency=float(data['f']),
            range=float(data['range']),
            mode=data['mode'],
        )

    @staticmethod
    def encode(obj: BDX902DeEsser) -> dict[str, Any]:
        return {
            "f": obj.frequency,
            "range": obj.range,
            "mode": obj.mode,
        }

class WaveDesignerCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> WaveDesigner:
        return WaveDesigner(
            attack=float(data['att']),
            sustain=float(data['sust']),
            gain=float(data['g']),
        )

    @staticmethod
    def encode(obj: WaveDesigner) -> dict[str, Any]:
        return {
            "att": obj.attack,
            "sust": obj.sustain,
            "g": obj.gain,
        }

class AutoRiderCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> AutoRider:
        return AutoRider(
            threshold=float(data['thr']),
            target=float(data['tgt']),
            speed=float(data['spd']),
            ratio=float(data['ratio']),
            hold=float(data['hld']),
            range=float(data['range']),
        )

    @staticmethod
    def encode(obj: AutoRider) -> dict[str, Any]:
        return {
            "thr": obj.threshold,
            "tgt": obj.target,
            "spd": obj.speed,
            "ratio": obj.ratio,
            "hld": obj.hold,
            "range": obj.range,
        }

class SoulWarmthPreCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> SoulWarmthPre:
        return SoulWarmthPre(
            drive=float(data['drv']),
            harmonic=float(data['hrm']),
            color=float(data['col']),
            trim=float(data['trim']),
            mix=float(data['wmix']),
        )

    @staticmethod
    def encode(obj: SoulWarmthPre) -> dict[str, Any]:
        return {
            "drv": obj.drive,
            "hrm": obj.harmonic,
            "col": obj.color,
            "trim": obj.trim,
            "wmix": obj.mix,
        }

class WingCompressorCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> WingCompressor:
        return WingCompressor(
            threshold=float(data['thr']),
            ratio=float(data['ratio']),
            knee=float(data['knee']),
            detector=data['det'],
            attack=float(data['att']),
            hold=float(data['hld']),
            release=float(data['rel']),
            envelope=data['env'],
            auto=data['auto'],
        )

    @staticmethod
    def encode(obj: WingCompressor) -> dict[str, Any]:
        return {
            "thr": obj.threshold,
            "ratio": obj.ratio,
            "knee": obj.knee,
            "det": obj.detector,
            "att": obj.attack,
            "hld": obj.hold,
            "rel": obj.release,
            "env": obj.envelope,
            "auto": obj.auto,
        }

class WingExpanderCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> WingExpander:
        return WingExpander(
            threshold=float(data['thr']),
            ratio=float(data['ratio']),
            knee=float(data['knee']),
            detector=data['det'],
            attack=float(data['att']),
            hold=float(data['hld']),
            release=float(data['rel']),
            envelope=data['env'],
            auto=data['auto'],
        )

    @staticmethod
    def encode(obj: WingExpander) -> dict[str, Any]:
        return {
            "thr": obj.threshold,
            "ratio": obj.ratio,
            "knee": obj.knee,
            "det": obj.detector,
            "att": obj.attack,
            "hld": obj.hold,
            "rel": obj.release,
            "env": obj.envelope,
            "auto": obj.auto,
        }

class Even88CompCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> Even88Comp:
        return Even88Comp(
            knee=data['knee'],
            threshold=float(data['thr']),
            threshold_pad=data['thrpull'],
            ratio=float(data['ratio']),
            attack=data['att'],
            release=float(data['rel']),
        )

    @staticmethod
    def encode(obj: Even88Comp) -> dict[str, Any]:
        return {
            "knee": obj.knee,
            "thr": obj.threshold,
            "thrpull": obj.threshold_pad,
            "ratio": obj.ratio,
            "att": obj.attack,
            "rel": obj.release,
        }

class OneKnobCompCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> OneKnobComp:
        return OneKnobComp(
            gain_reduction=float(data['gr']),
            auto_gain=data['dag'],
        )

    @staticmethod
    def encode(obj: OneKnobComp) -> dict[str, Any]:
        return {
            "gr": obj.gain_reduction,
            "dag": obj.auto_gain,
        }

class Soul9000Codec:
    @staticmethod
    def decode(data: dict[str, Any]) -> Soul9000:
        return Soul9000(
            threshold=float(data['thr']),
            ratio=float(data['ratio']),
            fast=data['fast'],
            release=float(data['rel']),
            peak=data['peak'],
        )

    @staticmethod
    def encode(obj: Soul9000) -> dict[str, Any]:
        return {
            "thr": obj.threshold,
            "ratio": obj.ratio,
            "fast": obj.fast,
            "rel": obj.release,
            "peak": obj.peak,
        }

class BDX160CompCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> BDX160Comp:
        return BDX160Comp(
            threshold=float(data['thr']),
            compression=float(data['comp']),
        )

    @staticmethod
    def encode(obj: BDX160Comp) -> dict[str, Any]:
        return {
            "thr": obj.threshold,
            "comp": obj.compression,
        }

class BDX560EasyCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> BDX560Easy:
        return BDX560Easy(
            threshold=float(data['thr']),
            ratio=float(data['ratio']),
            easy=data['easy'],
        )

    @staticmethod
    def encode(obj: BDX560Easy) -> dict[str, Any]:
        return {
            "thr": obj.threshold,
            "ratio": obj.ratio,
            "easy": obj.easy,
        }

class Red3CompressorCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> Red3Compressor:
        return Red3Compressor(
            threshold=float(data['thr']),
            ratio=float(data['ratio']),
            attack=float(data['att']),
            release=float(data['rel']),
            auto=data['auto'],
        )

    @staticmethod
    def encode(obj: Red3Compressor) -> dict[str, Any]:
        return {
            "thr": obj.threshold,
            "ratio": obj.ratio,
            "att": obj.attack,
            "rel": obj.release,
            "auto": obj.auto,
        }

class LMTCompressorCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> LMTCompressor:
        return LMTCompressor(
            transient_speed=float(data['tspd']),
            transient_emphasis=float(data['trans']),
            transient_gain=float(data['tgain']),
            transient_shaper_on=data['ton'],
            compression_amount=float(data['comp']),
            compressor_gain=float(data['cgain']),
            compressor_on=data['con'],
        )

    @staticmethod
    def encode(obj: LMTCompressor) -> dict[str, Any]:
        return {
            "tspd": obj.transient_speed,
            "trans": obj.transient_emphasis,
            "tgain": obj.transient_gain,
            "ton": obj.transient_shaper_on,
            "comp": obj.compression_amount,
            "cgain": obj.compressor_gain,
            "con": obj.compressor_on,
        }

class SoulBusCompCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> SoulBusComp:
        return SoulBusComp(
            threshold=float(data['thr']),
            ratio=float(data['ratio']),
            attack=float(data['att']),
            release=data['rel'],
        )

    @staticmethod
    def encode(obj: SoulBusComp) -> dict[str, Any]:
        return {
            "thr": obj.threshold,
            "ratio": obj.ratio,
            "att": obj.attack,
            "rel": obj.release,
        }

class PIA2250RackCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> PIA2250Rack:
        return PIA2250Rack(
            threshold=float(data['thr']),
            ratio=float(data['ratio']),
            attack=data['att'],
            release=float(data['rel']),
            knee=data['knee'],
            type=data['type'],
        )

    @staticmethod
    def encode(obj: PIA2250Rack) -> dict[str, Any]:
        return {
            "thr": obj.threshold,
            "ratio": obj.ratio,
            "att": obj.attack,
            "rel": obj.release,
            "knee": obj.knee,
            "type": obj.type,
        }

class LimiterAmp76Codec:
    @staticmethod
    def decode(data: dict[str, Any]) -> LimiterAmp76:
        return LimiterAmp76(
            input_gain=float(data['in']),
            output_gain=float(data['out']),
            attack=float(data['att']),
            release=float(data['rel']),
            ratio=data['ratio'],
        )

    @staticmethod
    def encode(obj: LimiterAmp76) -> dict[str, Any]:
        return {
            "in": obj.input_gain,
            "out": obj.output_gain,
            "att": obj.attack,
            "rel": obj.release,
            "ratio": obj.ratio,
        }

class LALevelerCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> LALeveler:
        return LALeveler(
            input_gain=float(data['ingain']),
            peak=float(data['peak']),
            mode=data['mode'],
        )

    @staticmethod
    def encode(obj: LALeveler) -> dict[str, Any]:
        return {
            "ingain": obj.input_gain,
            "peak": obj.peak,
            "mode": obj.mode,
        }

class FairKidCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> FairKid:
        return FairKid(
            input_gain=float(data['in']),
            threshold=float(data['thr']),
            time_constant=float(data['time']),
            bias=float(data['bias']),
        )

    @staticmethod
    def encode(obj: FairKid) -> dict[str, Any]:
        return {
            "in": obj.input_gain,
            "thr": obj.threshold,
            "time": obj.time_constant,
            "bias": obj.bias,
        }

class LTA100LevelerCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> LTA100Leveler:
        return LTA100Leveler(
            input_gain=float(data['ingain']),
            gain_reduction=float(data['gr']),
            attack=data['att'],
            release=data['rel'],
        )

    @staticmethod
    def encode(obj: LTA100Leveler) -> dict[str, Any]:
        return {
            "ingain": obj.input_gain,
            "gr": obj.gain_reduction,
            "att": obj.attack,
            "rel": obj.release,
        }

class EternalBlissCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> EternalBliss:
        return EternalBliss(
            threshold=float(data['thr']),
            ratio=float(data['ratio']),
            attack=float(data['att']),
            release=float(data['rel']),
            attack_fast=data['afast'],
            attack_log=data['alog'],
            gate_limit_on=data['glon'],
            gate_limit=float(data['glim']),
        )

    @staticmethod
    def encode(obj: EternalBliss) -> dict[str, Any]:
        return {
            "thr": obj.threshold,
            "ratio": obj.ratio,
            "att": obj.attack,
            "rel": obj.release,
            "afast": obj.attack_fast,
            "alog": obj.attack_log,
            "glon": obj.gate_limit_on,
            "glim": obj.gate_limit,
        }

class NoStressorCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> NoStressor:
        return NoStressor(
            input_gain=float(data['in']),
            output_gain=float(data['out']),
            attack=float(data['att']),
            release=float(data['rel']),
            ratio=data['ratio'],
        )

    @staticmethod
    def encode(obj: NoStressor) -> dict[str, Any]:
        return {
            "in": obj.input_gain,
            "out": obj.output_gain,
            "att": obj.attack,
            "rel": obj.release,
            "ratio": obj.ratio,
        }

class SourceExtractorCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> SourceExtractor:
        return SourceExtractor(
            threshold=float(data['thr']),
            depth=float(data['depth']),
            fast=data['fast'],
            peak=data['peak'],
        )

    @staticmethod
    def encode(obj: SourceExtractor) -> dict[str, Any]:
        return {
            "thr": obj.threshold,
            "depth": obj.depth,
            "fast": obj.fast,
            "peak": obj.peak,
        }

class PSELAComboCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> PSELACombo:
        return PSELACombo(
            threshold=float(data['thr']),
            depth=float(data['depth']),
            fast=data['fast'],
            peak=data['peak'],
            input_gain=float(data['ingain']),
            compressor_peak=float(data['cpeak']),
            compressor_mode=data['cmode'],
        )

    @staticmethod
    def encode(obj: PSELACombo) -> dict[str, Any]:
        return {
            "thr": obj.threshold,
            "depth": obj.depth,
            "fast": obj.fast,
            "peak": obj.peak,
            "ingain": obj.input_gain,
            "cpeak": obj.compressor_peak,
            "cmode": obj.compressor_mode,
        }

class EvenCompLimCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> EvenCompLim:
        return EvenCompLim(
            limiter_on=data['lon'],
            limiter_threshold=float(data['lthr']),
            limiter_recovery=data['lrec'],
            limiter_fast=data['lfast'],
            compressor_on=data['con'],
            compressor_threshold=float(data['cthr']),
            ratio=float(data['ratio']),
            compressor_recovery=data['crec'],
            compressor_fast=data['cfast'],
            compressor_gain=float(data['cgain']),
        )

    @staticmethod
    def encode(obj: EvenCompLim) -> dict[str, Any]:
        return {
            "lon": obj.limiter_on,
            "lthr": obj.limiter_threshold,
            "lrec": obj.limiter_recovery,
            "lfast": obj.limiter_fast,
            "con": obj.compressor_on,
            "cthr": obj.compressor_threshold,
            "ratio": obj.ratio,
            "crec": obj.compressor_recovery,
            "cfast": obj.compressor_fast,
            "cgain": obj.compressor_gain,
        }

class DrawMoreCompCodec:
    @staticmethod
    def decode(data: dict[str, Any]) -> DrawMoreComp:
        return DrawMoreComp(
            threshold=float(data['thr']),
            ratio=float(data['ratio']),
            attack=float(data['att']),
            release=float(data['rel']),
            limiter=float(data['lim']),
            limiter_release=float(data['lrel']),
            auto=data['auto'],
        )

    @staticmethod
    def encode(obj: DrawMoreComp) -> dict[str, Any]:
        return {
            "thr": obj.threshold,
            "ratio": obj.ratio,
            "att": obj.attack,
            "rel": obj.release,
            "lim": obj.limiter,
            "lrel": obj.limiter_release,
            "auto": obj.auto,
        }

PLUGIN_CODEC_MAP = {
    "GATE": WingGateCodec,
    "DUCK": WingDuckerCodec,
    "E88": Even88GateCodec,
    "D241G": DrawMore241Codec,
    "9000G": Soul9000GateCodec,
    "DEQ": DynamicEQCodec,
    "DEQ2": DualDynamicEQCodec,
    "DS902": BDX902DeEsserCodec,
    "WAVE": WaveDesignerCodec,
    "RIDE": AutoRiderCodec,
    "WARM": SoulWarmthPreCodec,
    "COMP": WingCompressorCodec,
    "EXP": WingExpanderCodec,
    "E88C": Even88CompCodec,
    "ONEC": OneKnobCompCodec,
    "9000C": Soul9000Codec,
    "B160": BDX160CompCodec,
    "B560": BDX560EasyCodec,
    "RED3": Red3CompressorCodec,
    "LMT": LMTCompressorCodec,
    "SBUS": SoulBusCompCodec,
    "2250": PIA2250RackCodec,
    "76LA": LimiterAmp76Codec,
    "LA": LALevelerCodec,
    "F670": FairKidCodec,
    "L100": LTA100LevelerCodec,
    "BLISS": EternalBlissCodec,
    "NSTR": NoStressorCodec,
    "PSE": SourceExtractorCodec,
    "CMB": PSELAComboCodec,
    "ECL33": EvenCompLimCodec,
    "D241C": DrawMoreCompCodec,
}

PLUGIN_MODEL_KEY_MAP = {
    WingGate: "GATE",
    WingDucker: "DUCK",
    Even88Gate: "E88",
    DrawMore241: "D241G",
    Soul9000Gate: "9000G",
    DynamicEQ: "DEQ",
    DualDynamicEQ: "DEQ2",
    BDX902DeEsser: "DS902",
    WaveDesigner: "WAVE",
    AutoRider: "RIDE",
    SoulWarmthPre: "WARM",
    WingCompressor: "COMP",
    WingExpander: "EXP",
    Even88Comp: "E88C",
    OneKnobComp: "ONEC",
    Soul9000: "9000C",
    BDX160Comp: "B160",
    BDX560Easy: "B560",
    Red3Compressor: "RED3",
    LMTCompressor: "LMT",
    SoulBusComp: "SBUS",
    PIA2250Rack: "2250",
    LimiterAmp76: "76LA",
    LALeveler: "LA",
    FairKid: "F670",
    LTA100Leveler: "L100",
    EternalBliss: "BLISS",
    NoStressor: "NSTR",
    SourceExtractor: "PSE",
    PSELACombo: "CMB",
    EvenCompLim: "ECL33",
    DrawMoreComp: "D241C",
}

class AudioDynamicsPluginCodec:
    BASE_KEYS = {"on", "mdl", "mix", "gain"}

    @staticmethod
    def decode(data: dict[str, Any]) -> AudioDynamicsPlugin:
        model = data["mdl"]
        if model not in PLUGIN_CODEC_MAP:
            raise KeyError(f"Unknown dynamics model: {model}")
        codec = PLUGIN_CODEC_MAP[model]
        # Pure plugin data
        plugin_data = {k: v for k, v in data.items() if k not in AudioDynamicsPluginCodec.BASE_KEYS}
        return codec.decode(plugin_data)

    @staticmethod
    def encode(obj: AudioDynamicsPlugin) -> dict[str, Any]:
        obj_type = type(obj)
        if obj_type not in PLUGIN_MODEL_KEY_MAP:
            raise KeyError(f"Unknown dynamics plugin type: {obj_type}")
        model_key = PLUGIN_MODEL_KEY_MAP[obj_type]
        codec = PLUGIN_CODEC_MAP[model_key]
        return codec.encode(obj)
