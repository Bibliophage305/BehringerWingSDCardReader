from wing_snapfile.models.audio.input import (
    AudioInput,
    AudioRoutableInput,
    AudioSourceSwitchableDelayableInput,
)
from wing_snapfile.codecs.audio.input_connections import AudioInputConnectionsCodec
from wing_snapfile.codecs.audio.input_settings import (
    AudioInputSettingsCodec,
    AudioSourceSwitchableDelayableInputSettingsCodec,
)


class AudioInputCodec:
    @staticmethod
    def decode(data: dict) -> AudioInput:
        return AudioInput(
            settings=AudioInputSettingsCodec.decode(data["set"]),
        )

    @staticmethod
    def encode(obj: AudioInput) -> dict:
        return {
            "set": AudioInputSettingsCodec.encode(obj.settings),
        }


class AudioRoutableInputCodec:
    @staticmethod
    def decode(data: dict) -> AudioRoutableInput:
        return AudioRoutableInput(
            settings=AudioInputSettingsCodec.decode(data["set"]),
            connections=AudioInputConnectionsCodec.decode(data["conn"]),
        )

    @staticmethod
    def encode(obj: AudioRoutableInput) -> dict:
        return {
            "set": AudioInputSettingsCodec.encode(obj.settings),
            "conn": AudioInputConnectionsCodec.encode(obj.connections),
        }


class AudioSourceSwitchableDelayableInputCodec:
    @staticmethod
    def decode(data: dict) -> AudioSourceSwitchableDelayableInput:
        return AudioSourceSwitchableDelayableInput(
            settings=AudioSourceSwitchableDelayableInputSettingsCodec.decode(
                data["set"]
            ),
            connections=AudioInputConnectionsCodec.decode(data["conn"]),
        )

    @staticmethod
    def encode(obj: AudioSourceSwitchableDelayableInput) -> dict:
        return {
            "set": AudioSourceSwitchableDelayableInputSettingsCodec.encode(
                obj.settings
            ),
            "conn": AudioInputConnectionsCodec.encode(obj.connections),
        }