from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate


@dataclass_validate
@dataclass(kw_only=True)
class InputSettings:
    is_phase_inverted: bool
    trim: float
    balance: float


@dataclass_validate
@dataclass(kw_only=True)
class FullInputSettings(InputSettings):
    auto_source_switch: bool
    use_alternate_source: bool
    delay_mode: str
    delay_amount: float
    delay_on: bool