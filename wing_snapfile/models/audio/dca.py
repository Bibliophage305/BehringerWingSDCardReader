from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate


@dataclass_validate
@dataclass(kw_only=True)
class DCA:
    name: str
    color: int
    icon: int
    led_on: bool
    mute_on: bool
    fader_level: float
    monitor_mode: str
