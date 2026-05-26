from wing_snapfile.models.audio.mute_group import AudioMuteGroup


class AudioMuteGroupCodec:
    @staticmethod
    def decode(data: dict) -> AudioMuteGroup:
        return AudioMuteGroup(
            name=data["name"],
            mute_on=data["mute"],
        )

    @staticmethod
    def encode(obj: AudioMuteGroup) -> dict:
        return {
            "name": obj.name,
            "mute": obj.mute_on,
        }
