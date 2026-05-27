from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate
from wing_snapfile.models.audio.dynamics_plugins import DynamicsPlugin


@dataclass_validate
@dataclass(kw_only=True)
class DynamicsBlock:
    on: bool
    model: str
    mix: int
    gain: float
    parameters: DynamicsPlugin
