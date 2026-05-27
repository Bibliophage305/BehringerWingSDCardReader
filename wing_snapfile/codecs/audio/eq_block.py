from wing_snapfile.models.audio.eq import EQBlock
from wing_snapfile.codecs.audio.eq_plugins import EQPluginCodec


class EQBlockCodec:
    @staticmethod
    def decode(data: dict) -> EQBlock:
        return EQBlock(
            on=data["on"],
            model=data["mdl"],
            mix=data["mix"],
            parameters=EQPluginCodec.decode(data),
        )

    @staticmethod
    def encode(obj: EQBlock) -> dict:
        return {
            "on": obj.on,
            "mdl": obj.model,
            "mix": obj.mix,
            **EQPluginCodec.encode(obj.parameters),
        }