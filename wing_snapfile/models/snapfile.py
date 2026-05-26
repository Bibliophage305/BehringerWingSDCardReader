import msgspec

from wing_snapfile.models.audio.data import AudioData
from wing_snapfile.models.console.data import ConsoleData


class Snapfile(msgspec.Struct, kw_only=True):
    type: str

    creator: str
    creator_version: str
    creator_model: str
    creator_name: str

    audio_engine_data: AudioData
    console_engine_data: ConsoleData