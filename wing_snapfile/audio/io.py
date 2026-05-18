from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

from wing_snapfile.audio.source import AudioSourceBank
from wing_snapfile.audio.output import AudioOutputBank

@dataclass_validate
@dataclass
class AudioIo:
    sources: AudioSourceBank
    outputs: AudioOutputBank
    alternate_inputs: bool
    global_input_select_override: bool

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioIo":
        return AudioIo(
            sources=AudioSourceBank.from_dict(data["in"]),
            outputs=AudioOutputBank.from_dict(data["out"]),
            alternate_inputs=data["altsw"],
            global_input_select_override=data["autoaltovr"],
        )
