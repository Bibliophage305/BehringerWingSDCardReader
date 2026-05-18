from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

@dataclass_validate
@dataclass
class AudioDCA:
    name: str
    color: int
    icon: int
    led_on: bool
    mute_on: bool
    fader_level: float
    monitor_mode: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data["name"],
            color=data["col"],
            icon=data["icon"],
            led_on=data["led"],
            mute_on=data["mute"],
            fader_level=float(data["fdr"]),
            monitor_mode=data["mon"],
        )
