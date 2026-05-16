from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate
from .eq_plugins import EQPlugin, parse_eq_plugin

@dataclass_validate
@dataclass
class AudioEngineEQ:
    on: bool
    model: str
    mix: int
    parameters: EQPlugin

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioEngineEQ":
        return AudioEngineEQ(
            on=data["on"],
            model=data["mdl"],
            mix=data["mix"],
            parameters=parse_eq_plugin(data)
        )
