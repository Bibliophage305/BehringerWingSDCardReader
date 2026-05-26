import msgspec
from typing import Union

class AudioDynamicsPlugin(msgspec.Struct, kw_only=True): pass

class WingGate(AudioDynamicsPlugin):
    threshold: float
    range: float
    attack: int
    hold: int
    release: float
    accent: int
    ratio: str

class WingDucker(AudioDynamicsPlugin):
    threshold: float
    range: float
    attack: int
    hold: float
    release: float

class Even88Gate(AudioDynamicsPlugin):
    threshold: float
    hysteresis: float
    range: float
    release: float
    fast: bool
    m40: bool

class DrawMore241(AudioDynamicsPlugin):
    threshold: float
    slow: bool

class Soul9000Gate(AudioDynamicsPlugin):
    threshold: float
    range: float
    hold: float
    release: float
    fast: bool
    mode: str

class DynamicEQ(AudioDynamicsPlugin):
    threshold: float
    ratio: float
    attack: float
    release: float
    filter_type: str
    gain: float
    frequency: float
    q: float
    mode: str

class DualDynamicEQ(AudioDynamicsPlugin):
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

class BDX902DeEsser(AudioDynamicsPlugin):
    frequency: float
    range: float
    mode: str

class WaveDesigner(AudioDynamicsPlugin):
    attack: float
    sustain: float
    gain: float

class AutoRider(AudioDynamicsPlugin):
    threshold: float
    target: float
    speed: float
    ratio: float
    hold: float
    range: float

class SoulWarmthPre(AudioDynamicsPlugin):
    drive: float
    harmonic: float
    color: float
    trim: float
    mix: float

class WingCompressor(AudioDynamicsPlugin):
    threshold: float
    ratio: float
    knee: float
    detector: str
    attack: float
    hold: float
    release: float
    envelope: str
    auto: bool

class WingExpander(AudioDynamicsPlugin):
    threshold: float
    ratio: float
    knee: float
    detector: str
    attack: float
    hold: float
    release: float
    envelope: str
    auto: bool

class Even88Comp(AudioDynamicsPlugin):
    knee: str
    threshold: float
    threshold_pad: bool
    ratio: float
    attack: str
    release: float

class OneKnobComp(AudioDynamicsPlugin):
    gain_reduction: float
    auto_gain: bool

class Soul9000(AudioDynamicsPlugin):
    threshold: float
    ratio: float
    fast: bool
    release: float
    peak: bool

class BDX160Comp(AudioDynamicsPlugin):
    threshold: float
    compression: float

class BDX560Easy(AudioDynamicsPlugin):
    threshold: float
    ratio: float
    easy: bool

class Red3Compressor(AudioDynamicsPlugin):
    threshold: float
    ratio: float
    attack: float
    release: float
    auto: bool

class LMTCompressor(AudioDynamicsPlugin):
    transient_speed: float
    transient_emphasis: float
    transient_gain: float
    transient_shaper_on: bool
    compression_amount: float
    compressor_gain: float
    compressor_on: bool

class SoulBusComp(AudioDynamicsPlugin):
    threshold: float
    ratio: float
    attack: float
    release: str

class PIA2250Rack(AudioDynamicsPlugin):
    threshold: float
    ratio: float
    attack: str
    release: float
    knee: str
    type: str

class LimiterAmp76(AudioDynamicsPlugin):
    input_gain: float
    output_gain: float
    attack: float
    release: float
    ratio: str

class LALeveler(AudioDynamicsPlugin):
    input_gain: float
    peak: float
    mode: str

class FairKid(AudioDynamicsPlugin):
    input_gain: float
    threshold: float
    time_constant: float
    bias: float

class LTA100Leveler(AudioDynamicsPlugin):
    input_gain: float
    gain_reduction: float
    attack: str
    release: str

class EternalBliss(AudioDynamicsPlugin):
    threshold: float
    ratio: float
    attack: float
    release: float
    attack_fast: bool
    attack_log: bool
    gate_limit_on: bool
    gate_limit: float

class NoStressor(AudioDynamicsPlugin):
    input_gain: float
    output_gain: float
    attack: float
    release: float
    ratio: str

class SourceExtractor(AudioDynamicsPlugin):
    threshold: float
    depth: float
    fast: bool
    peak: bool

class PSELACombo(AudioDynamicsPlugin):
    threshold: float
    depth: float
    fast: bool
    peak: bool
    input_gain: float
    compressor_peak: float
    compressor_mode: str

class EvenCompLim(AudioDynamicsPlugin):
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

class DrawMoreComp(AudioDynamicsPlugin):
    threshold: float
    ratio: float
    attack: float
    release: float
    limiter: float
    limiter_release: float
    auto: bool

PLUGIN_MODEL_MAP: dict[str, type[AudioDynamicsPlugin]] = {
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
