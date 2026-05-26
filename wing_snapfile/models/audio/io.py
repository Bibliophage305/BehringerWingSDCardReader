import msgspec

from wing_snapfile.models.audio.source import AudioSourceBank
from wing_snapfile.models.audio.output import AudioOutputBank


class AudioIo(msgspec.Struct, kw_only=True):
    sources: AudioSourceBank
    outputs: AudioOutputBank

    alternate_inputs: bool
    global_input_select_override: bool