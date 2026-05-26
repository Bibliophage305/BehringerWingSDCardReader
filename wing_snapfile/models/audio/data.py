import msgspec

from wing_snapfile.types.one_indexed_list import OneIndexedList

from wing_snapfile.models.audio.config import AudioConfig
from wing_snapfile.models.audio.io import AudioIo
from wing_snapfile.models.audio.channel import (
    AudioAuxChannel,
    AudioFullChannel,
    AudioBusChannel,
    AudioMainChannel,
    AudioMatrixChannel,
)
from wing_snapfile.models.audio.dca import AudioDCA
from wing_snapfile.models.audio.mute_group import AudioMuteGroup
from wing_snapfile.models.audio.cards import AudioCards
from wing_snapfile.models.audio.play_settings import AudioPlaySettings
from wing_snapfile.models.audio.record_settings import AudioRecordSettings


class AudioData(msgspec.Struct, kw_only=True):
    config: AudioConfig
    io: AudioIo

    channels: OneIndexedList[AudioFullChannel]
    aux_channels: OneIndexedList[AudioAuxChannel]
    busses: OneIndexedList[AudioBusChannel]
    mains: OneIndexedList[AudioMainChannel]
    matrices: OneIndexedList[AudioMatrixChannel]

    dcas: OneIndexedList[AudioDCA]
    mute_groups: OneIndexedList[AudioMuteGroup]

    fx: OneIndexedList[dict]

    cards: AudioCards
    play_settings: AudioPlaySettings
    record_settings: AudioRecordSettings