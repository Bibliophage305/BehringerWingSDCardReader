from wing_snapfile.models.audio.input_connections import AudioInputConnections


class AudioInputConnectionsCodec:
    @staticmethod
    def decode(data: dict) -> AudioInputConnections:
        return AudioInputConnections(
            group=data["grp"],
            input=data["in"],
            alt_group=data["altgrp"],
            alt_input=data["altin"],
        )

    @staticmethod
    def encode(obj: AudioInputConnections) -> dict:
        return {
            "grp": obj.group,
            "in": obj.input,
            "altgrp": obj.alt_group,
            "altin": obj.alt_input,
        }