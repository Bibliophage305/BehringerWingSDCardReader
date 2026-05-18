from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate
from wing_snapfile.console.data import ConsoleData
from wing_snapfile.audio.data import AudioData

@dataclass_validate
@dataclass
class Snapfile:
    type: str
    creator: str
    creator_vers: str
    creator_model: str
    creator_name: str
    audio_engine_data: AudioData
    console_engine_data: ConsoleData

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Snapfile":
        return Snapfile(
            type=data["type"],
            creator=data["creator"],
            creator_vers=data["creator_vers"],
            creator_model=data["creator_model"],
            creator_name=data["creator_name"],
            audio_engine_data=AudioData.from_dict(data["ae_data"]),
            console_engine_data=ConsoleData.from_dict(data["ce_data"]),
        )

    def to_dict(self) -> dict[str, object]:
        return {
            "type": self.type,
            "creator": self.creator,
            "creator_vers": self.creator_vers,
            "creator_model": self.creator_model,
            "creator_name": self.creator_name,
            "ae_data": self.audio_engine_data.to_dict(),
            "ce_data": self.console_engine_data.to_dict(),
        }
