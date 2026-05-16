from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate
from typing import Type

# {'on': True, 'mdl': 'GATE', 'mix': 100, 'gain': 0, 'thr': -40, 'range': 40, 'att': 10, 'hld': 10, 'rel': 200.474884, 'acc': 0, 'ratio': '1:3'}
# {'on': True, 'mdl': 'DUCK', 'mix': 100, 'gain': 0, 'thr': -20, 'range': 20, 'att': 100, 'hld': 100.4754639, 'rel': 503.5701599}
# {'on': True, 'mdl': 'E88', 'mix': 100, 'gain': 0, 'thr': -35, 'hyst': 6, 'range': 60, 'rel': 354.5083618, 'fast': False, 'm40': False}
# {'on': False, 'mdl': 'D241G', 'mix': 100, 'gain': 0, 'thr': -40, 'slow': False}
# {'on': False, 'mdl': '9000G', 'mix': 100, 'gain': 0, 'thr': -35, 'range': 40, 'hld': 50.81421661, 'rel': 806.477356, 'fast': False, 'mode': 'GATE'}
# {'on': False, 'mdl': 'DEQ', 'mix': 100, 'gain': 0, 'thr': -20, 'ratio': 2, 'att': 50, 'rel': 300.8161621, 'filt': 'BP', 'g': 0, 'f': 1002.37439, 'q': 0.997970223, 'mode': 'high'}
# {'on': False, 'mdl': 'DEQ2', 'mix': 100, 'gain': 0, '1-thr': -20, '1-ratio': 2, '1-att': 50, '1-rel': 300.8161621, '1-filt': 'BP', '1-g': 0, '1-f': 200, '1-q': 0.997970223, '1-mode': 'high', '2-thr': -20, '2-ratio': 2, '2-att': 50, '2-rel': 300.8161621, '2-filt': 'BP', '2-g': 0, '2-f': 2992.470947, '2-q': 0.997970223, '2-mode': 'high'}
# {'on': False, 'mdl': 'DS902', 'mix': 100, 'gain': 0, 'f': 5029.671387, 'range': 4, 'mode': 'HF'}
# {'on': False, 'mdl': 'WAVE', 'mix': 100, 'gain': 0, 'att': 0, 'sust': 0, 'g': 0}
# {'on': False, 'mdl': 'RIDE', 'mix': 100, 'gain': 0, 'thr': -40, 'tgt': -18, 'spd': 10, 'ratio': 4, 'hld': 1.539926767, 'range': 6}
# {'on': False, 'mdl': 'WARM', 'mix': 100, 'gain': 0, 'drv': 33, 'hrm': 0, 'col': 0, 'trim': 0, 'wmix': 100}
# {'on': False, 'mdl': 'COMP', 'mix': 100, 'gain': 0, 'thr': -10, 'ratio': 3, 'knee': 3, 'det': 'RMS', 'att': 50, 'hld': 20, 'rel': 150.3349457, 'env': 'LOG', 'auto': True}
# {'on': False, 'mdl': 'EXP', 'mix': 100, 'gain': 0, 'thr': -40, 'ratio': 3, 'knee': 1, 'det': 'RMS', 'att': 50, 'hld': 100.0000076, 'rel': 150.3349457, 'env': 'LOG', 'auto': True}
# {'on': False, 'mdl': 'E88C', 'mix': 100, 'gain': 0, 'knee': 'SOFT', 'thr': 0, 'thrpull': False, 'ratio': 3.019951582, 'att': 'SLOW', 'rel': 353.3465271}
# {'on': False, 'mdl': 'ONEC', 'mix': 100, 'gain': 0, 'gr': 3, 'dag': True}
# {'on': False, 'mdl': '9000C', 'mix': 100, 'gain': 0, 'thr': -10, 'ratio': 2.799999952, 'fast': False, 'rel': 398.815918, 'peak': False}
# {'on': False, 'mdl': 'B160', 'mix': 100, 'gain': 0, 'thr': 0.512091637, 'comp': 3}
# {'on': False, 'mdl': 'B560', 'mix': 100, 'gain': 0, 'thr': 0, 'ratio': 3, 'easy': True}
# {'on': False, 'mdl': 'RED3', 'mix': 100, 'gain': 0, 'thr': -12, 'ratio': 3, 'att': 20.06982613, 'rel': 398.815918, 'auto': False}
# {'on': False, 'mdl': 'LMT', 'mix': 100, 'gain': 0, 'tspd': 0.5, 'trans': 0, 'tgain': 0, 'ton': False, 'comp': 10, 'cgain': 0, 'con': True}
# {'on': False, 'mdl': 'SBUS', 'mix': 100, 'gain': 0, 'thr': -12, 'ratio': 3, 'att': 10, 'rel': 'AUTO'}
# {'on': False, 'mdl': '2250', 'mix': 100, 'gain': 0, 'thr': 2, 'ratio': 3, 'att': 'MED', 'rel': 202.0557404, 'knee': 'SOFT', 'type': 'NEW'}
# {'on': False, 'mdl': '76LA', 'mix': 100, 'gain': 0, 'in': -30, 'out': -27, 'att': 2, 'rel': 2, 'ratio': '8'}
# {'on': False, 'mdl': 'LA', 'mix': 100, 'gain': 0, 'ingain': 40, 'peak': 20, 'mode': 'COMP'}
# {'on': False, 'mdl': 'F670', 'mix': 100, 'gain': 0, 'in': -10, 'thr': 5, 'time': 2, 'bias': 1}
# {'on': False, 'mdl': 'L100', 'mix': 100, 'gain': 0, 'ingain': 3, 'gr': 3, 'att': 'MED', 'rel': 'MED'}
# {'on': False, 'mdl': 'BLISS', 'mix': 100, 'gain': 0, 'thr': -15, 'ratio': 3, 'att': 9.915781021, 'rel': 101.8793488, 'afast': False, 'alog': False, 'glon': False, 'glim': -12}
# {'on': False, 'mdl': 'NSTR', 'mix': 100, 'gain': 0, 'in': 4, 'out': 3, 'att': 4, 'rel': 5, 'ratio': '3:1'}
# {'on': False, 'mdl': 'PSE', 'mix': 100, 'gain': 0, 'thr': 0, 'depth': 12, 'fast': False, 'peak': False}
# {'on': False, 'mdl': 'CMB', 'mix': 100, 'gain': 0, 'thr': -36, 'depth': 12, 'fast': False, 'peak': False, 'ingain': 40, 'cpeak': 0, 'cmode': 'COMP'}
# {'on': False, 'mdl': 'ECL33', 'mix': 100, 'gain': 0, 'lon': False, 'lthr': -5, 'lrec': 'A1', 'lfast': False, 'con': True, 'cthr': -15, 'ratio': 3, 'crec': 'A1', 'cfast': False, 'cgain': 0}
# {'on': False, 'mdl': 'D241C', 'mix': 100, 'gain': 0, 'thr': -20, 'ratio': 3, 'att': 10.06669521, 'rel': 397.1640625, 'lim': 0, 'lrel': 397.1640625, 'auto': True}

@dataclass_validate
@dataclass
class DynamicsPlugin:
    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "DynamicsPlugin":
        raise NotImplementedError

@dataclass_validate
@dataclass
class WingGate(DynamicsPlugin):
    threshold: float
    range: float
    attack: int
    hold: int
    release: float
    accent: int
    ratio: str

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "WingGate":
        return WingGate(
            threshold=float(data["thr"]),
            range=float(data["range"]),
            attack=data["att"],
            hold=data["hld"],
            release=data["rel"],
            accent=data["acc"],
            ratio=data["ratio"]
        )

@dataclass_validate
@dataclass
class WingDucker(DynamicsPlugin):
    threshold: float
    range: float
    attack: int
    hold: float
    release: float

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "WingDucker":
        return WingDucker(
            threshold=float(data["thr"]),
            range=float(data["range"]),
            attack=data["att"],
            hold=float(data["hld"]),
            release=float(data["rel"]),
        )

@dataclass_validate
@dataclass
class Even88Gate(DynamicsPlugin):
    threshold: float
    hysteresis: float
    range: float
    release: float
    fast: bool
    m40: bool

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Even88Gate":
        return Even88Gate(
            threshold=float(data["thr"]),
            hysteresis=float(data["hyst"]),
            range=float(data["range"]),
            release=float(data["rel"]),
            fast=data["fast"],
            m40=data["m40"],
        )

@dataclass_validate
@dataclass
class DrawMore241(DynamicsPlugin):
    threshold: float
    slow: bool

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "DrawMore241":
        return DrawMore241(
            threshold=float(data["thr"]),
            slow=data["slow"],
        )

@dataclass_validate
@dataclass
class Soul9000Gate(DynamicsPlugin):
    threshold: float
    range: float
    hold: float
    release: float
    fast: bool
    mode: str

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Soul9000Gate":
        return Soul9000Gate(
            threshold=float(data["thr"]),
            range=float(data["range"]),
            hold=float(data["hld"]),
            release=float(data["rel"]),
            fast=data["fast"],
            mode=data["mode"],
        )

@dataclass_validate
@dataclass
class DynamicEQ(DynamicsPlugin):
    threshold: float
    ratio: float
    attack: float
    release: float
    filter_type: str
    gain: float
    frequency: float
    q: float
    mode: str

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "DynamicEQ":
        return DynamicEQ(
            threshold=float(data["thr"]),
            ratio=float(data["ratio"]),
            attack=float(data["att"]),
            release=float(data["rel"]),
            filter_type=data["filt"],
            gain=float(data["g"]),
            frequency=float(data["f"]),
            q=float(data["q"]),
            mode=data["mode"],
        )

# {'on': False, 'mdl': 'DEQ2', 'mix': 100, 'gain': 0, '1-thr': -20, '1-ratio': 2, '1-att': 50, '1-rel': 300.8161621, '1-filt': 'BP', '1-g': 0, '1-f': 200, '1-q': 0.997970223, '1-mode': 'high', '2-thr': -20, '2-ratio': 2, '2-att': 50, '2-rel': 300.8161621, '2-filt': 'BP', '2-g': 0, '2-f': 2992.470947, '2-q': 0.997970223, '2-mode': 'high'}
@dataclass_validate
@dataclass
class DualDynamicEQ(DynamicsPlugin):
    band1_threshold: float
    band1_ratio: float
    band1_attack: float
    band1_release: float
    band1_filter_type: str
    band1_gain: float
    band1_frequency: float
    band1_q: float
    band1_mode: str
    band2_threshold: float
    band2_ratio: float
    band2_attack: float
    band2_release: float
    band2_filter_type: str
    band2_gain: float
    band2_frequency: float
    band2_q: float
    band2_mode: str

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "DualDynamicEQ":
        return DualDynamicEQ(
            band1_threshold=float(data["1-thr"]),
            band1_ratio=float(data["1-ratio"]),
            band1_attack=float(data["1-att"]),
            band1_release=float(data["1-rel"]),
            band1_filter_type=data["1-filt"],
            band1_gain=float(data["1-g"]),
            band1_frequency=float(data["1-f"]),
            band1_q=float(data["1-q"]),
            band1_mode=data["1-mode"],
            band2_threshold=float(data["2-thr"]),
            band2_ratio=float(data["2-ratio"]),
            band2_attack=float(data["2-att"]),
            band2_release=float(data["2-rel"]),
            band2_filter_type=data["2-filt"],
            band2_gain=float(data["2-g"]),
            band2_frequency=float(data["2-f"]),
            band2_q=float(data["2-q"]),
            band2_mode=data["2-mode"],
        )
    
@dataclass_validate
@dataclass
class BDX902DeEsser(DynamicsPlugin):
    frequency: float
    range: float
    mode: str

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "BDX902DeEsser":
        return BDX902DeEsser(
            frequency=float(data["f"]),
            range=float(data["range"]),
            mode=data["mode"],
        )

@dataclass_validate
@dataclass
class WaveDesigner(DynamicsPlugin):
    attack: float
    sustain: float
    gain: float

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "WaveDesigner":
        return WaveDesigner(
            attack=float(data["att"]),
            sustain=float(data["sust"]),
            gain=float(data["g"]),
        )


@dataclass_validate
@dataclass
class AutoRider(DynamicsPlugin):
    threshold: float
    target: float
    speed: float
    ratio: float
    hold: float
    range: float

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AutoRider":
        return AutoRider(
            threshold=float(data["thr"]),
            target=float(data["tgt"]),
            speed=float(data["spd"]),
            ratio=float(data["ratio"]),
            hold=float(data["hld"]),
            range=float(data["range"]),
        )

@dataclass_validate
@dataclass
class SoulWarmthPre(DynamicsPlugin):
    drive: float
    harmonic: float
    color: float
    trim: float
    mix: float

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "SoulWarmthPre":
        return SoulWarmthPre(
            drive=float(data["drv"]),
            harmonic=float(data["hrm"]),
            color=float(data["col"]),
            trim=float(data["trim"]),
            mix=float(data["wmix"]),
        )




@dataclass_validate
@dataclass
class WingCompressor(DynamicsPlugin):
    threshold: float
    ratio: float
    knee: float
    detector: str
    attack: float
    hold: float
    release: float
    envelope: str
    auto: bool

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "WingCompressor":
        return WingCompressor(
            threshold=float(data["thr"]),
            ratio=float(data["ratio"]),
            knee=float(data["knee"]),
            detector=data["det"],
            attack=float(data["att"]),
            hold=float(data["hld"]),
            release=float(data["rel"]),
            envelope=data["env"],
            auto=data["auto"],
        )


@dataclass_validate
@dataclass
class WingExpander(DynamicsPlugin):
    threshold: float
    ratio: float
    knee: float
    detector: str
    attack: float
    hold: float
    release: float
    envelope: str
    auto: bool

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "WingExpander":
        return WingExpander(
            threshold=float(data["thr"]),
            ratio=float(data["ratio"]),
            knee=float(data["knee"]),
            detector=data["det"],
            attack=float(data["att"]),
            hold=float(data["hld"]),
            release=float(data["rel"]),
            envelope=data["env"],
            auto=data["auto"],
        )

@dataclass_validate
@dataclass
class Even88Comp(DynamicsPlugin):
    # {'on': False, 'mdl': 'E88C', 'mix': 100, 'gain': 0, 'knee': 'SOFT', 'thr': 0, 'thrpull': False, 'ratio': 3.019951582, 'att': 'SLOW', 'rel': 353.3465271}
    knee: str
    threshold: float
    threshold_pad: bool
    ratio: float
    attack: str
    release: float

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Even88Comp":
        return Even88Comp(
            knee=data["knee"],
            threshold=float(data["thr"]),
            threshold_pad=data["thrpull"],
            ratio=float(data["ratio"]),
            attack=data["att"],
            release=float(data["rel"]),
        )

@dataclass_validate
@dataclass
class OneKnobComp(DynamicsPlugin):
    # {'on': False, 'mdl': 'ONEC', 'mix': 100, 'gain': 0, 'gr': 3, 'dag': True}
    gain_reduction: float
    auto_gain: bool

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "OneKnobComp":
        return OneKnobComp(
            gain_reduction=float(data["gr"]),
            auto_gain=data["dag"],
        )

@dataclass_validate
@dataclass
class Soul9000(DynamicsPlugin):
    threshold: float
    ratio: float
    fast: bool
    release: float
    peak: bool

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Soul9000":
        return Soul9000(
            threshold=float(data["thr"]),
            ratio=float(data["ratio"]),
            fast=data["fast"],
            release=float(data["rel"]),
            peak=data["peak"],
        )



@dataclass_validate
@dataclass
class BDX160Comp(DynamicsPlugin):
    threshold: float
    compression: float

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "BDX160Comp":
        return BDX160Comp(
            threshold=float(data["thr"]),
            compression=float(data["comp"]),
        )


@dataclass_validate
@dataclass
class BDX560Easy(DynamicsPlugin):
    threshold: float
    ratio: float
    easy: bool

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "BDX560Easy":
        return BDX560Easy(
            threshold=float(data["thr"]),
            ratio=float(data["ratio"]),
            easy=data["easy"],
        )

@dataclass_validate
@dataclass
class Red3Compressor(DynamicsPlugin):
    threshold: float
    ratio: float
    attack: float
    release: float
    auto: bool

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Red3Compressor":
        return Red3Compressor(
            threshold=float(data["thr"]),
            ratio=float(data["ratio"]),
            attack=float(data["att"]),
            release=float(data["rel"]),
            auto=data["auto"],
        )

@dataclass_validate
@dataclass
class LMTCompressor(DynamicsPlugin):
    # {'on': False, 'mdl': 'LMT', 'mix': 100, 'gain': 0, 'tspd': 0.5, 'trans': 0, 'tgain': 0, 'ton': False, 'comp': 10, 'cgain': 0, 'con': True}
    transient_speed: float
    transient_emphasis: float
    transient_gain: float
    transient_shaper_on: bool
    compression_amount: float
    compressor_gain: float
    compressor_on: bool

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "LMTCompressor":
        return LMTCompressor(
            transient_speed=float(data["tspd"]),
            transient_emphasis=float(data["trans"]),
            transient_gain=float(data["tgain"]),
            transient_shaper_on=data["ton"],
            compression_amount=float(data["comp"]),
            compressor_gain=float(data["cgain"]),
            compressor_on=data["con"],
        )

@dataclass_validate
@dataclass
class SoulBusComp(DynamicsPlugin):
    threshold: float
    ratio: float
    attack: float
    release: str

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "SoulBusComp":
        return SoulBusComp(
            threshold=float(data["thr"]),
            ratio=float(data["ratio"]),
            attack=float(data["att"]),
            release=data["rel"],
        )

@dataclass_validate
@dataclass
class PIA2250Rack(DynamicsPlugin):
    threshold: float
    ratio: float
    attack: str
    release: float
    knee: str
    type: str

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "PIA2250Rack":
        return PIA2250Rack(
            threshold=float(data["thr"]),
            ratio=float(data["ratio"]),
            attack=data["att"],
            release=float(data["rel"]),
            knee=data["knee"],
            type=data["type"],
        )

@dataclass_validate
@dataclass
class LimiterAmp76(DynamicsPlugin):
    input_gain: float
    output_gain: float
    attack: float
    release: float
    ratio: str

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "LimiterAmp76":
        return LimiterAmp76(
            input_gain=float(data["in"]),
            output_gain=float(data["out"]),
            attack=float(data["att"]),
            release=float(data["rel"]),
            ratio=data["ratio"],
        )


@dataclass_validate
@dataclass
class LALeveler(DynamicsPlugin):
    input_gain: float
    peak: float
    mode: str

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "LALeveler":
        return LALeveler(
            input_gain=float(data["ingain"]),
            peak=float(data["peak"]),
            mode=data["mode"],
        )

@dataclass_validate
@dataclass
class FairKid(DynamicsPlugin):
    input_gain: float
    threshold: float
    time_constant: float
    bias: float

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "FairKid":
        return FairKid(
            input_gain=float(data["in"]),
            threshold=float(data["thr"]),
            time_constant=float(data["time"]),
            bias=float(data["bias"]),
        )

@dataclass_validate
@dataclass
class LTA100Leveler(DynamicsPlugin):
    input_gain: float
    gain_reduction: float
    attack: str
    release: str

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "LTA100Leveler":
        return LTA100Leveler(
            input_gain=float(data["ingain"]),
            gain_reduction=float(data["gr"]),
            attack=data["att"],
            release=data["rel"],
        )

@dataclass_validate
@dataclass
class EternalBliss(DynamicsPlugin):
    threshold: float
    ratio: float
    attack: float
    release: float
    attack_fast: bool
    attack_log: bool
    gate_limit_on: bool
    gate_limit: float

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "EternalBliss":
        return EternalBliss(
            threshold=float(data["thr"]),
            ratio=float(data["ratio"]),
            attack=float(data["att"]),
            release=float(data["rel"]),
            attack_fast=data["afast"],
            attack_log=data["alog"],
            gate_limit_on=data["glon"],
            gate_limit=float(data["glim"]),
        )






@dataclass_validate
@dataclass
class NoStressor(DynamicsPlugin):
    input_gain: float
    output_gain: float
    attack: float
    release: float
    ratio: str

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "NoStressor":
        return NoStressor(
            input_gain=float(data["in"]),
            output_gain=float(data["out"]),
            attack=float(data["att"]),
            release=float(data["rel"]),
            ratio=data["ratio"],
        )

@dataclass_validate
@dataclass
class SourceExtractor(DynamicsPlugin):
    threshold: float
    depth: float
    fast: bool
    peak: bool

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "SourceExtractor":
        return SourceExtractor(
            threshold=float(data["thr"]),
            depth=float(data["depth"]),
            fast=data["fast"],
            peak=data["peak"],
        )

@dataclass_validate
@dataclass
class PSELACombo(DynamicsPlugin):
    threshold: float
    depth: float
    fast: bool
    peak: bool
    input_gain: float
    compressor_peak: float
    compressor_mode: str

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "PSELACombo":
        return PSELACombo(
            threshold=float(data["thr"]),
            depth=float(data["depth"]),
            fast=data["fast"],
            peak=data["peak"],
            input_gain=float(data["ingain"]),
            compressor_peak=float(data["cpeak"]),
            compressor_mode=data["cmode"],
        )








@dataclass_validate
@dataclass
class EvenCompLim(DynamicsPlugin):
    limiter_on: bool
    limiter_threshold: float
    limiter_recovery: str
    limiter_fast: bool
    compressor_on: bool
    compressor_threshold: float
    ratio: float
    compressor_recovery: str
    compressor_fast: bool
    compressor_gain: float

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "EvenCompLim":
        return EvenCompLim(
            limiter_on=data["lon"],
            limiter_threshold=float(data["lthr"]),
            limiter_recovery=data["lrec"],
            limiter_fast=data["lfast"],
            compressor_on=data["con"],
            compressor_threshold=float(data["cthr"]),
            ratio=float(data["ratio"]),
            compressor_recovery=data["crec"],
            compressor_fast=data["cfast"],
            compressor_gain=float(data["cgain"]),
        )



@dataclass_validate
@dataclass
class DrawMoreComp(DynamicsPlugin):
    threshold: float
    ratio: float
    attack: float
    release: float
    limiter: float
    limiter_release: float
    auto: bool

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "DrawMoreComp":
        return DrawMoreComp(
            threshold=float(data["thr"]),
            ratio=float(data["ratio"]),
            attack=float(data["att"]),
            release=float(data["rel"]),
            limiter=float(data["lim"]),
            limiter_release=float(data["lrel"]),
            auto=data["auto"],
        )






PLUGIN_MODEL_MAP: dict[str, Type[DynamicsPlugin]] = {
    "GATE": WingGate,
    "DUCK": WingDucker,
    "E88": Even88Gate,
    "D241G": DrawMore241,
    "9000G": Soul9000Gate,
    "DEQ": DynamicEQ,
    "DEQ2": DualDynamicEQ,
    "DS902": BDX902DeEsser,
    "WAVE": WaveDesigner,
    "RIDE": AutoRider,
    "WARM": SoulWarmthPre,
    "COMP": WingCompressor,
    "EXP": WingExpander,
    "E88C": Even88Comp,
    "ONEC": OneKnobComp,
    "9000C": Soul9000,
    "B160": BDX160Comp,
    "B560": BDX560Easy,
    "RED3": Red3Compressor,
    "LMT": LMTCompressor,
    "SBUS": SoulBusComp,
    "2250": PIA2250Rack,
    "76LA": LimiterAmp76,
    "LA": LALeveler,
    "F670": FairKid,
    "L100": LTA100Leveler,
    "BLISS": EternalBliss,
    "NSTR": NoStressor,
    "PSE": SourceExtractor,
    "CMB": PSELACombo,
    "ECL33": EvenCompLim,
    "D241C": DrawMoreComp,
}


def parse_dynamics_plugin(data: dict[str, object]) -> DynamicsPlugin:
    model = data["mdl"]
    plugin_cls = PLUGIN_MODEL_MAP[model]
    plugin_data = {k: v for k, v in data.items() if k not in {"on", "mdl", "mix", "gain"}}
    return plugin_cls.from_dict(plugin_data)
