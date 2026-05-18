from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate
from wing_snapfile.audio.input_settings import AudioInputSettings, AudioSourceSwitchableDelayableInputSettings
from wing_snapfile.audio.input_connections import AudioInputConnections

@dataclass_validate
@dataclass
class AudioInput:
    settings: AudioInputSettings

    @classmethod
    def from_dict(cls, data):
        return cls(**cls._from_dict_kwargs(data))

    @classmethod
    def _from_dict_kwargs(cls, data: dict[str, object]) -> dict[str, object]:
        return {
            "settings": AudioInputSettings.from_dict(data["set"]),
        }
    
    def to_dict(self):
        return {
            "set": self.settings.to_dict(),
        }

@dataclass_validate
@dataclass
class AudioRoutableInput(AudioInput):
    connections: AudioInputConnections

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioInput._from_dict_kwargs(data),
            "connections": AudioInputConnections.from_dict(data["conn"]),
        }
    
    def to_dict(self):
        return {
            **super().to_dict(),
            "conn": self.connections.to_dict(),
        }

@dataclass_validate
@dataclass
class AudioSourceSwitchableDelayableInput(AudioRoutableInput):
    settings: AudioSourceSwitchableDelayableInputSettings

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioRoutableInput._from_dict_kwargs(data),
            "settings": AudioSourceSwitchableDelayableInputSettings.from_dict(data["set"]),
        }
