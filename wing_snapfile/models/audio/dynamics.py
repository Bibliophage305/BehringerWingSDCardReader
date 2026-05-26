import msgspec
from wing_snapfile.models.audio.dynamics_plugins import AudioDynamicsPlugin


class AudioDynamics(msgspec.Struct, kw_only=True):
    on: bool
    model: str
    mix: int
    gain: float
    parameters: AudioDynamicsPlugin
