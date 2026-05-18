# TODO

from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

from wing_snapfile.audio.source import AudioSourceBank

from wing_snapfile.snapfile_reader import (
    IoRouteBank,
)

@dataclass_validate
@dataclass
class AudioIo:
    sources: AudioSourceBank
    out_routes: list[IoRouteBank]
    alternate_inputs: bool
    global_input_select_override: bool

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioIo":
        # in_routes = [IoRouteBank.from_dict(name, value) for name, value in data["in"].items()]
        out_routes = [IoRouteBank.from_dict(name, value) for name, value in data["out"].items()]
        return AudioIo(
            sources=AudioSourceBank.from_dict(data["in"]),
            out_routes=out_routes,
            alternate_inputs=data["altsw"],
            global_input_select_override=data["autoaltovr"],
        )
