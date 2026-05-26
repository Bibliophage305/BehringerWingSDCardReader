from wing_snapfile.models.audio.eq import AudioEQ
from wing_snapfile.codecs.audio.eq_plugins import AudioEQPluginCodec


class AudioEQCodec:
    @staticmethod
    def decode(data: dict) -> AudioEQ:
        return AudioEQ(
            on=data["on"],
            model=data["mdl"],
            mix=data["mix"],
            parameters=AudioEQPluginCodec.decode(data),
        )

    @staticmethod
    def encode(obj: AudioEQ) -> dict:
        return {
            "on": obj.on,
            "mdl": obj.model,
            "mix": obj.mix,
            **AudioEQPluginCodec.encode(obj.parameters),
        }