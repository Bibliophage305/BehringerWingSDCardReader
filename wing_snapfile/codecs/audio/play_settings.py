from wing_snapfile.models.audio.play_settings import AudioPlaySettings


class AudioPlaySettingsCodec:
    @staticmethod
    def decode(data: dict) -> AudioPlaySettings:
        return AudioPlaySettings(repeat=data["repeat"])

    @staticmethod
    def encode(obj: AudioPlaySettings) -> dict:
        return {
            "repeat": obj.repeat,
        }
