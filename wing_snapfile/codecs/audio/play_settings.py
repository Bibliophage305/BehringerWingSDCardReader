from wing_snapfile.models.audio.play_settings import PlaySettings


class PlaySettingsCodec:
    @staticmethod
    def decode(data: dict) -> PlaySettings:
        return PlaySettings(repeat=data["repeat"])

    @staticmethod
    def encode(obj: PlaySettings) -> dict:
        return {
            "repeat": obj.repeat,
        }
