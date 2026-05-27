from wing_snapfile.models.audio.mute_group import MuteGroup


class MuteGroupCodec:
    @staticmethod
    def decode(data: dict) -> MuteGroup:
        return MuteGroup(
            name=data["name"],
            mute_on=data["mute"],
        )

    @staticmethod
    def encode(obj: MuteGroup) -> dict:
        return {
            "name": obj.name,
            "mute": obj.mute_on,
        }
