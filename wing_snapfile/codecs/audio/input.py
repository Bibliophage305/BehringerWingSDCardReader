from wing_snapfile.models.audio.input import (
    Input,
    FullInput,
)
from wing_snapfile.codecs.audio.input_connections import InputConnectionsCodec
from wing_snapfile.codecs.audio.input_settings import (
    InputSettingsCodec,
    FullInputSettingsCodec,
)


class InputCodec:
    @staticmethod
    def decode(data: dict) -> Input:
        return Input(
            settings=InputSettingsCodec.decode(data["set"]),
        )

    @staticmethod
    def encode(obj: Input) -> dict:
        return {
            "set": InputSettingsCodec.encode(obj.settings),
        }


class FullInputCodec:
    @staticmethod
    def decode(data: dict) -> FullInput:
        return FullInput(
            settings=FullInputSettingsCodec.decode(
                data["set"]
            ),
            connections=InputConnectionsCodec.decode(data["conn"]),
        )

    @staticmethod
    def encode(obj: FullInput) -> dict:
        return {
            "set": FullInputSettingsCodec.encode(
                obj.settings
            ),
            "conn": InputConnectionsCodec.encode(obj.connections),
        }