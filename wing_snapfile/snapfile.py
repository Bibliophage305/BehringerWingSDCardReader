from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate
from .console_engine_data import ConsoleEngineData
from .audio_engine_data import AudioEngineData

@dataclass_validate
@dataclass
class Snapfile:
    type: str
    creator: str
    creator_vers: str
    creator_model: str
    creator_name: str
    audio_engine_data: AudioEngineData
    console_engine_data: ConsoleEngineData

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Snapfile":
        return Snapfile(
            type=data["type"],
            creator=data["creator"],
            creator_vers=data["creator_vers"],
            creator_model=data["creator_model"],
            creator_name=data["creator_name"],
            audio_engine_data=AudioEngineData.from_dict(data["ae_data"]),
            console_engine_data=ConsoleEngineData.from_dict(data["ce_data"]),
        )
