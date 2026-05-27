from wing_snapfile.models.snapfile import Snapfile

from wing_snapfile.codecs.audio.data import AudioDataCodec
from wing_snapfile.codecs.console.data import ConsoleDataCodec


class SnapfileCodec:
    @staticmethod
    def decode(data: dict) -> Snapfile:
        return Snapfile(
            type=data["type"],

            creator=data["creator"],
            creator_version=data["creator_vers"],
            creator_model=data["creator_model"],
            creator_name=data["creator_name"],

            audio_engine_data=AudioDataCodec.decode(
                data["ae_data"]
            ),

            console_engine_data=ConsoleDataCodec.decode(
                data["ce_data"]
            ),
        )

    @staticmethod
    def encode(snapfile: Snapfile) -> dict:
        return {
            "type": snapfile.type,

            "creator": snapfile.creator,
            "creator_vers": snapfile.creator_version,
            "creator_model": snapfile.creator_model,
            "creator_name": snapfile.creator_name,

            "ae_data": AudioDataCodec.encode(
                snapfile.audio_engine_data
            ),

            "ce_data": ConsoleDataCodec.encode(
                snapfile.console_engine_data
            ),
        }