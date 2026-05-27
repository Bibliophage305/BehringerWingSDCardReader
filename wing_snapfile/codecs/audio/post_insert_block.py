from wing_snapfile.models.audio.post_insert_block import (
    PostInsertBlock,
    PostInsertBlockWithAutomix,
)


class PostInsertBlockCodec:
    @staticmethod
    def decode(data: dict) -> PostInsertBlock:
        return PostInsertBlock(
            on=data["on"],
            insert=data["ins"],
        )

    @staticmethod
    def encode(obj: PostInsertBlock) -> dict:
        return {
            "on": obj.on,
            "ins": obj.insert,
        }


class PostInsertBlockWithAutomixCodec:
    @staticmethod
    def decode(data: dict) -> PostInsertBlockWithAutomix:
        return PostInsertBlockWithAutomix(
            on=data["on"],
            insert=data["ins"],
            mode=data["mode"],
            autogain_weight=float(data["w"]),
        )

    @staticmethod
    def encode(obj: PostInsertBlockWithAutomix) -> dict:
        return {
            "on": obj.on,
            "mode": obj.mode,
            "ins": obj.insert,
            "w": obj.autogain_weight,
        }
