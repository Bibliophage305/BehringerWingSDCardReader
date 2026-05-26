from wing_snapfile.models.audio.io import AudioIo
from wing_snapfile.protocol.codecs.audio.source import AudioSourceBankCodec
from wing_snapfile.protocol.codecs.audio.output import AudioOutputBankCodec


class AudioIoCodec:
    @staticmethod
    def decode(data: dict) -> AudioIo:
        return AudioIo(
            sources=AudioSourceBankCodec.decode(data["in"]),
            outputs=AudioOutputBankCodec.decode(data["out"]),
            alternate_inputs=data["altsw"],
            global_input_select_override=data["autoaltovr"],
        )

    @staticmethod
    def encode(obj: AudioIo) -> dict:
        return {
            "in": AudioSourceBankCodec.encode(obj.sources),
            "out": AudioOutputBankCodec.encode(obj.outputs),
            "altsw": obj.alternate_inputs,
            "autoaltovr": obj.global_input_select_override,
        }