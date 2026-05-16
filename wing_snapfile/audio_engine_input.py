from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate
from .audio_engine_input_settings import AudioEngineInputSettings
from .audio_engine_input_connections import AudioEngineInputConnections

class Connectable:
    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            "connections": AudioEngineInputConnections.from_dict(data["conn"]),
        }

@dataclass_validate
@dataclass
class AudioEngineInput:
    settings: AudioEngineInputSettings

    @classmethod
    def from_dict(cls, data):
        return cls(**cls._from_dict_kwargs(data))

    @classmethod
    def _from_dict_kwargs(cls, data: dict[str, object]) -> dict[str, object]:
        return {
            "settings": AudioEngineInputSettings.from_dict(data["set"]),
        }

@dataclass_validate
@dataclass
class AudioEngineRoutableInput(AudioEngineInput, Connectable):
    connections: AudioEngineInputConnections

    @classmethod
    def _from_dict_kwargs(cls, data):
        return {
            **AudioEngineInput._from_dict_kwargs(data),
            **Connectable._from_dict_kwargs(data),
        }
