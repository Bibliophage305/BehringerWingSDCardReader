from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate
from wing_snapfile.audio.input_settings import AudioInputSettings
from wing_snapfile.audio.input_connections import AudioInputConnections

class Connectable:
    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            "connections": AudioInputConnections.from_dict(data["conn"]),
        }

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

@dataclass_validate
@dataclass
class AudioRoutableInput(AudioInput, Connectable):
    connections: AudioInputConnections

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioInput._from_dict_kwargs(data),
            **Connectable._from_dict_kwargs(data),
        }
