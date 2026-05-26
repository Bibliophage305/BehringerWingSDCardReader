from wing_snapfile.models.audio.pre_insert_plugin import AudioPreInsertPlugin


class AudioPreInsertPluginCodec:
    @staticmethod
    def decode(data: dict) -> AudioPreInsertPlugin:
        return AudioPreInsertPlugin(on=data["on"], insert=data["ins"])

    @staticmethod
    def encode(obj: AudioPreInsertPlugin) -> dict:
        return {
            "on": obj.on,
            "ins": obj.insert,
        }
