from wing_snapfile.models.audio.dynamics_block import DynamicsBlock
from wing_snapfile.codecs.audio.dynamics_plugins import DynamicsPluginCodec


class DynamicsBlockCodec:
    @staticmethod
    def decode(data: dict) -> DynamicsBlock:
        return DynamicsBlock(
            on=data["on"],
            model=data["mdl"],
            mix=data["mix"],
            gain=float(data["gain"]),
            parameters=DynamicsPluginCodec.decode(data),
        )

    @staticmethod
    def encode(obj: DynamicsBlock) -> dict:
        return {
            "on": obj.on,
            "mdl": obj.model,
            "mix": obj.mix,
            "gain": obj.gain,
            **DynamicsPluginCodec.encode(obj.parameters),
        }
