from wing_snapfile.models.audio.record_settings import RecordSettings


class RecordSettingsCodec:
    @staticmethod
    def decode(data: dict) -> RecordSettings:
        return RecordSettings(
            path=data["path"],
            resolution=data["resolution"],
            channels=data["channels"],
        )

    @staticmethod
    def encode(obj: RecordSettings) -> dict:
        return {
            "path": obj.path,
            "resolution": obj.resolution,
            "channels": obj.channels,
        }