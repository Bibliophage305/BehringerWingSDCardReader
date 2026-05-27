from wing_snapfile.models.audio.io import IO
from wing_snapfile.codecs.audio.source import SourceBankCodec
from wing_snapfile.codecs.audio.output import OutputBankCodec


class IOCodec:
    @staticmethod
    def decode(data: dict) -> IO:
        return IO(
            sources=SourceBankCodec.decode(data["in"]),
            outputs=OutputBankCodec.decode(data["out"]),
            alternate_inputs=data["altsw"],
            global_input_select_override=data["autoaltovr"],
        )

    @staticmethod
    def encode(obj: IO) -> dict:
        return {
            "in": SourceBankCodec.encode(obj.sources),
            "out": OutputBankCodec.encode(obj.outputs),
            "altsw": obj.alternate_inputs,
            "autoaltovr": obj.global_input_select_override,
        }