from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate
from wing_snapfile.audio.eq_plugins import EQPlugin, parse_eq_plugin

@dataclass_validate
@dataclass
class AudioEQ:
    on: bool
    model: str
    mix: int
    parameters: EQPlugin

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioEQ":
        return AudioEQ(
            on=data["on"],
            model=data["mdl"],
            mix=data["mix"],
            parameters=parse_eq_plugin(data)
        )
