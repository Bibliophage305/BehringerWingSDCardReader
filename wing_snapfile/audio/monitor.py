from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

@dataclass_validate
@dataclass
class AudioMonitorEQ:
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

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioMonitorEQ":
        return AudioMonitorEQ(
            on=data["on"],
            lsg=float(data["lsg"]),
            lsf=float(data["lsf"]),
            g1=float(data["1g"]),
            f1=float(data["1f"]),
            q1=float(data["1q"]),
            g2=float(data["2g"]),
            f2=float(data["2f"]),
            q2=float(data["2q"]),
            g3=float(data["3g"]),
            f3=float(data["3f"]),
            q3=float(data["3q"]),
            g4=float(data["4g"]),
            f4=float(data["4f"]),
            q4=float(data["4q"]),
            g5=float(data["5g"]),
            f5=float(data["5f"]),
            q5=float(data["5q"]),
            g6=float(data["6g"]),
            f6=float(data["6f"]),
            q6=float(data["6q"]),
            hsg=float(data["hsg"]),
            hsf=float(data["hsf"])
        )
    
    def to_dict(self):
        return {
            "on": self.on,
            "lsg": self.lsg,
            "lsf": self.lsf,
            "1g": self.g1,
            "1f": self.f1,
            "1q": self.q1,
            "2g": self.g2,
            "2f": self.f2,
            "2q": self.q2,
            "3g": self.g3,
            "3f": self.f3,
            "3q": self.q3,
            "4g": self.g4,
            "4f": self.f4,
            "4q": self.q4,
            "5g": self.g5,
            "5f": self.f5,
            "5q": self.q5,
            "6g": self.g6,
            "6f": self.f6,
            "6q": self.q6,
            "hsg": self.hsg,
            "hsf": self.hsf
        }

@dataclass_validate
@dataclass
class AudioMonitorDelay:
    on: bool
    metres: float

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioMonitorDelay":
        return AudioMonitorDelay(
            on=data["on"],
            metres=float(data["m"])
        )
    
    def to_dict(self):
        return {
            "on": self.on,
            "m": self.metres
        }

@dataclass_validate
@dataclass
class AudioMonitor:
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

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioMonitor":
        return AudioMonitor(
            fader_level=float(data["lvl"]),
            phase_invert=data["inv"],
            pan=data["pan"],
            width=data["wid"],
            eq=AudioMonitorEQ.from_dict(data["eq"]),
            limiter_threshold=data["lim"],
            delay=AudioMonitorDelay.from_dict(data["dly"]),
            dim=data["dim"],
            pfl_dim=data["pfldim"],
            band_solo_trim=data["eqbdtrim"],
            source_level=float(data["srclvl"]),
            source_mix=float(data["srcmix"]),
            source=data["src"],
            direct_input=data["dirin"],
            tags=data["tags"].split(","),
        )
    
    def to_dict(self):
        return {
            "lvl": self.fader_level,
            "inv": self.phase_invert,
            "pan": self.pan,
            "wid": self.width,
            "eq": self.eq.to_dict(),
            "lim": self.limiter_threshold,
            "dly": self.delay.to_dict(),
            "dim": self.dim,
            "pfldim": self.pfl_dim,
            "eqbdtrim": self.band_solo_trim,
            "srclvl": self.source_level,
            "srcmix": self.source_mix,
            "src": self.source,
            "dirin": self.direct_input,
            "tags": ",".join(self.tags),
        }