from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

from wing_snapfile.models.audio.data import AudioData
from wing_snapfile.models.console.data import ConsoleData


@dataclass_validate
@dataclass(kw_only=True)
class Snapfile:
    type: str

    creator: str
    creator_version: str
    creator_model: str
    creator_name: str

    audio_engine_data: AudioData
    console_engine_data: ConsoleData