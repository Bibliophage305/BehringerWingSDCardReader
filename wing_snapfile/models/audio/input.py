import msgspec

from wing_snapfile.models.audio.input_connections import AudioInputConnections
from wing_snapfile.models.audio.input_settings import (
    AudioInputSettings,
    AudioSourceSwitchableDelayableInputSettings,
)


class AudioInput(msgspec.Struct, kw_only=True):
    """Basic input — settings only, no routing connections."""
    settings: AudioInputSettings


class AudioRoutableInput(msgspec.Struct, kw_only=True):
    """Input with routing connections and basic settings."""
    settings: AudioInputSettings
    connections: AudioInputConnections


class AudioSourceSwitchableDelayableInput(msgspec.Struct, kw_only=True):
    """Fully-featured input — routing connections, source switching, delay."""
    settings: AudioSourceSwitchableDelayableInputSettings
    connections: AudioInputConnections