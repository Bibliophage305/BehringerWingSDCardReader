from wing_snapfile.models.audio.input_connections import InputConnections


class InputConnectionsCodec:
    @staticmethod
    def decode(data: dict) -> InputConnections:
        return InputConnections(
            group=data["grp"],
            input=data["in"],
            alt_group=data["altgrp"],
            alt_input=data["altin"],
        )

    @staticmethod
    def encode(obj: InputConnections) -> dict:
        return {
            "grp": obj.group,
            "in": obj.input,
            "altgrp": obj.alt_group,
            "altin": obj.alt_input,
        }