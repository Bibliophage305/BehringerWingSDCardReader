from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

from wing_snapfile.models.audio.eq_plugins import EQPlugin


@dataclass_validate
@dataclass(kw_only=True)
class EQBlock:
    on: bool
    model: str
    mix: int
    parameters: EQPlugin
