from wing_snapfile.models.audio.dynamics import AudioDynamics
from wing_snapfile.codecs.audio.dynamics_plugins import AudioDynamicsPluginCodec


class AudioDynamicsCodec:
    @staticmethod
    def decode(data: dict) -> AudioDynamics:
        return AudioDynamics(
            on=data["on"],
            model=data["mdl"],
            mix=data["mix"],
            gain=float(data["gain"]),
            parameters=AudioDynamicsPluginCodec.decode(data),
        )

    @staticmethod
    def encode(obj: AudioDynamics) -> dict:
        return {
            "on": obj.on,
            "mdl": obj.model,
            "mix": obj.mix,
            "gain": obj.gain,
            **AudioDynamicsPluginCodec.encode(obj.parameters),
        }
