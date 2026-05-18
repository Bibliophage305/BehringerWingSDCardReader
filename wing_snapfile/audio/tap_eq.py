from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

@dataclass_validate
@dataclass
class AudioTapEQ:
    on: bool
    band1_gain: float
    band1_freq: float
    band1_q: float
    band2_gain: float
    band2_freq: float
    band2_q: float
    band3_gain: float
    band3_freq: float
    band3_q: float

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioTapEQ":
        return AudioTapEQ(
            on=data["on"],
            band1_gain=float(data["1g"]),
            band1_freq=float(data["1f"]),
            band1_q=float(data["1q"]),
            band2_gain=float(data["2g"]),
            band2_freq=float(data["2f"]),
            band2_q=float(data["2q"]),
            band3_gain=float(data["3g"]),
            band3_freq=float(data["3f"]),
            band3_q=float(data["3q"])
        )
    
    def to_dict(self):
        return {
            "on": self.on,
            "1g": self.band1_gain,
            "1f": self.band1_freq,
            "1q": self.band1_q,
            "2g": self.band2_gain,
            "2f": self.band2_freq,
            "2q": self.band2_q,
            "3g": self.band3_gain,
            "3f": self.band3_freq,
            "3q": self.band3_q,
        }
