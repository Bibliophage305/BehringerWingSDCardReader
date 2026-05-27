from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

from wing_snapfile.models.audio.input_connections import InputConnections
from wing_snapfile.models.audio.input_settings import (
    InputSettings,
    FullInputSettings,
)


@dataclass_validate
@dataclass(kw_only=True)
class Input:
    settings: InputSettings


@dataclass_validate
@dataclass(kw_only=True)
class FullInput:
    settings: FullInputSettings
    connections: InputConnections