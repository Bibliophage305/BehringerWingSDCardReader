import msgspec

from wing_snapfile.types.one_indexed_list import OneIndexedList


class AudioWLiveCardSlotConfig(msgspec.Struct, kw_only=True):
    rectracks: int
    playmode: str


class AudioWLiveCardSlot(msgspec.Struct, kw_only=True):
    config: AudioWLiveCardSlotConfig


class AudioWLiveCard(msgspec.Struct, kw_only=True):
    sd_link_mode: str
    auto_input: str
    show_meters: bool

    auto_stop: str
    auto_play: str
    auto_record: str

    slots: OneIndexedList[AudioWLiveCardSlot]


class AudioWMADICard(msgspec.Struct, kw_only=True):
    mode: str
    rxclock: bool


class AudioCards(msgspec.Struct, kw_only=True):
    wlive_card: AudioWLiveCard
    wmadi_card: AudioWMADICard