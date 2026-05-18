from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate
from wing_snapfile.audio.dynamics_plugins import DynamicsPlugin, parse_dynamics_plugin

@dataclass_validate
@dataclass
class AudioDynamics:
    on: bool
    model: str
    mix: int
    gain: float
    parameters: DynamicsPlugin

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioDynamics":
        return AudioDynamics(
            on=data["on"],
            model=data["mdl"],
            mix=data["mix"],
            gain=float(data["gain"]),
            parameters=parse_dynamics_plugin(data)
        )
