from wing_snapfile.models.audio.post_insert_plugin import (
    AudioPostInsertPlugin,
    AudioPostInsertPluginWithAutomix,
)


class AudioPostInsertPluginCodec:
    @staticmethod
    def decode(data: dict) -> AudioPostInsertPlugin:
        return AudioPostInsertPlugin(
            on=data["on"],
            insert=data["ins"],
        )

    @staticmethod
    def encode(obj: AudioPostInsertPlugin) -> dict:
        return {
            "on": obj.on,
            "ins": obj.insert,
        }


class AudioPostInsertPluginWithAutomixCodec:
    @staticmethod
    def decode(data: dict) -> AudioPostInsertPluginWithAutomix:
        return AudioPostInsertPluginWithAutomix(
            on=data["on"],
            insert=data["ins"],
            mode=data["mode"],
            autogain_weight=float(data["w"]),
        )

    @staticmethod
    def encode(obj: AudioPostInsertPluginWithAutomix) -> dict:
        return {
            "on": obj.on,
            "mode": obj.mode,
            "ins": obj.insert,
            "w": obj.autogain_weight,
        }
