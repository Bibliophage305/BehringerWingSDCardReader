from wing_snapfile.models.audio.pre_insert_block import PreInsertBlock


class PreInsertPluginCodec:
    @staticmethod
    def decode(data: dict) -> PreInsertBlock:
        return PreInsertBlock(on=data["on"], insert=data["ins"])

    @staticmethod
    def encode(obj: PreInsertBlock) -> dict:
        return {
            "on": obj.on,
            "ins": obj.insert,
        }
