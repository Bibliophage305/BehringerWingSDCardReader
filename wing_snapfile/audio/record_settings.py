from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

@dataclass_validate
@dataclass
class AudioRecordSettings:
    path: str
    resolution: str
    channels: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            path=data["path"],
            resolution=data["resolution"],
            channels=data["channels"],
        )
    
    def to_dict(self):
        return {
            "path": self.path,
            "resolution": self.resolution,
            "channels": self.channels,
        }
