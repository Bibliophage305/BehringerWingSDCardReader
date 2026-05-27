from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

class DynamicsPlugin: pass

@dataclass_validate
@dataclass(kw_only=True)
class WingGate(DynamicsPlugin):
    threshold: float
    range: float
    attack: int
    hold: int
    release: float
    accent: int
    ratio: str

@dataclass_validate
@dataclass(kw_only=True)
class WingDucker(DynamicsPlugin):
    threshold: float
    range: float
    attack: int
    hold: float
    release: float

@dataclass_validate
@dataclass(kw_only=True)
class Even88Gate(DynamicsPlugin):
    threshold: float
    hysteresis: float
    range: float
    release: float
    fast: bool
    m40: bool

@dataclass_validate
@dataclass(kw_only=True)
class DrawMore241(DynamicsPlugin):
    threshold: float
    slow: bool

@dataclass_validate
@dataclass(kw_only=True)
class Soul9000Gate(DynamicsPlugin):
    threshold: float
    range: float
    hold: float
    release: float
    fast: bool
    mode: str

@dataclass_validate
@dataclass(kw_only=True)
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

@dataclass_validate
@dataclass(kw_only=True)
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

@dataclass_validate
@dataclass(kw_only=True)
class BDX902DeEsser(DynamicsPlugin):
    frequency: float
    range: float
    mode: str

@dataclass_validate
@dataclass(kw_only=True)
class WaveDesigner(DynamicsPlugin):
    attack: float
    sustain: float
    gain: float

@dataclass_validate
@dataclass(kw_only=True)
class AutoRider(DynamicsPlugin):
    threshold: float
    target: float
    speed: float
    ratio: float
    hold: float
    range: float

@dataclass_validate
@dataclass(kw_only=True)
class SoulWarmthPre(DynamicsPlugin):
    drive: float
    harmonic: float
    color: float
    trim: float
    mix: float

@dataclass_validate
@dataclass(kw_only=True)
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

@dataclass_validate
@dataclass(kw_only=True)
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

@dataclass_validate
@dataclass(kw_only=True)
class Even88Comp(DynamicsPlugin):
    knee: str
    threshold: float
    threshold_pad: bool
    ratio: float
    attack: str
    release: float

@dataclass_validate
@dataclass(kw_only=True)
class OneKnobComp(DynamicsPlugin):
    gain_reduction: float
    auto_gain: bool

@dataclass_validate
@dataclass(kw_only=True)
class Soul9000(DynamicsPlugin):
    threshold: float
    ratio: float
    fast: bool
    release: float
    peak: bool

@dataclass_validate
@dataclass(kw_only=True)
class BDX160Comp(DynamicsPlugin):
    threshold: float
    compression: float

@dataclass_validate
@dataclass(kw_only=True)
class BDX560Easy(DynamicsPlugin):
    threshold: float
    ratio: float
    easy: bool

@dataclass_validate
@dataclass(kw_only=True)
class Red3Compressor(DynamicsPlugin):
    threshold: float
    ratio: float
    attack: float
    release: float
    auto: bool

@dataclass_validate
@dataclass(kw_only=True)
class LMTCompressor(DynamicsPlugin):
    transient_speed: float
    transient_emphasis: float
    transient_gain: float
    transient_shaper_on: bool
    compression_amount: float
    compressor_gain: float
    compressor_on: bool

@dataclass_validate
@dataclass(kw_only=True)
class SoulBusComp(DynamicsPlugin):
    threshold: float
    ratio: float
    attack: float
    release: str

@dataclass_validate
@dataclass(kw_only=True)
class PIA2250Rack(DynamicsPlugin):
    threshold: float
    ratio: float
    attack: str
    release: float
    knee: str
    type: str

@dataclass_validate
@dataclass(kw_only=True)
class LimiterAmp76(DynamicsPlugin):
    input_gain: float
    output_gain: float
    attack: float
    release: float
    ratio: str

@dataclass_validate
@dataclass(kw_only=True)
class LALeveler(DynamicsPlugin):
    input_gain: float
    peak: float
    mode: str

@dataclass_validate
@dataclass(kw_only=True)
class FairKid(DynamicsPlugin):
    input_gain: float
    threshold: float
    time_constant: float
    bias: float

@dataclass_validate
@dataclass(kw_only=True)
class LTA100Leveler(DynamicsPlugin):
    input_gain: float
    gain_reduction: float
    attack: str
    release: str

@dataclass_validate
@dataclass(kw_only=True)
class EternalBliss(DynamicsPlugin):
    threshold: float
    ratio: float
    attack: float
    release: float
    attack_fast: bool
    attack_log: bool
    gate_limit_on: bool
    gate_limit: float

@dataclass_validate
@dataclass(kw_only=True)
class NoStressor(DynamicsPlugin):
    input_gain: float
    output_gain: float
    attack: float
    release: float
    ratio: str

@dataclass_validate
@dataclass(kw_only=True)
class SourceExtractor(DynamicsPlugin):
    threshold: float
    depth: float
    fast: bool
    peak: bool

@dataclass_validate
@dataclass(kw_only=True)
class PSELACombo(DynamicsPlugin):
    threshold: float
    depth: float
    fast: bool
    peak: bool
    input_gain: float
    compressor_peak: float
    compressor_mode: str

@dataclass_validate
@dataclass(kw_only=True)
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

@dataclass_validate
@dataclass(kw_only=True)
class DrawMoreComp(DynamicsPlugin):
    threshold: float
    ratio: float
    attack: float
    release: float
    limiter: float
    limiter_release: float
    auto: bool

PLUGIN_MODEL_MAP: dict[str, type[DynamicsPlugin]] = {
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
