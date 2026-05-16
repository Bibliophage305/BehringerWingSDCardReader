# TODO

from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

from .audio_engine_source import AudioEngineSourceBank

from .snapfile_reader import (
    IoRouteBank,
)

@dataclass_validate
@dataclass
class AudioEngineIo:
    sources: AudioEngineSourceBank
    out_routes: list[IoRouteBank]
    alternate_inputs: bool
    global_input_select_override: bool

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioEngineIo":
        # in_routes = [IoRouteBank.from_dict(name, value) for name, value in data["in"].items()]
        out_routes = [IoRouteBank.from_dict(name, value) for name, value in data["out"].items()]
        return AudioEngineIo(
            sources=AudioEngineSourceBank.from_dict(data["in"]),
            out_routes=out_routes,
            alternate_inputs=data["altsw"],
            global_input_select_override=data["autoaltovr"],
        )
