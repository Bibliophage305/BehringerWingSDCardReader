from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

from wing_snapfile.types.one_indexed_list import OneIndexedList

from wing_snapfile.models.audio.config import AudioConfig
from wing_snapfile.models.audio.io import IO
from wing_snapfile.models.audio.channel import (
    AuxChannel,
    FullChannel,
    BusChannel,
    MainChannel,
    MatrixChannel,
)
from wing_snapfile.models.audio.dca import DCA
from wing_snapfile.models.audio.mute_group import MuteGroup
from wing_snapfile.models.audio.expansion_cards import ExpansionCards
from wing_snapfile.models.audio.play_settings import PlaySettings
from wing_snapfile.models.audio.record_settings import RecordSettings


@dataclass_validate
@dataclass(kw_only=True)
class AudioData:
    config: AudioConfig
    io: IO

    channels: OneIndexedList[FullChannel]
    aux_channels: OneIndexedList[AuxChannel]
    busses: OneIndexedList[BusChannel]
    mains: OneIndexedList[MainChannel]
    matrices: OneIndexedList[MatrixChannel]

    dcas: OneIndexedList[DCA]
    mute_groups: OneIndexedList[MuteGroup]

    fx: OneIndexedList[dict]

    expansion_cards: ExpansionCards
    play_settings: PlaySettings
    record_settings: RecordSettings