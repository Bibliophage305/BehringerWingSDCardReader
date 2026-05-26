from wing_snapfile.models.audio.cards import (
    AudioCards,
    AudioWLiveCard,
    AudioWLiveCardSlot,
    AudioWLiveCardSlotConfig,
    AudioWMADICard,
)

from wing_snapfile.protocol.helpers.indexed import (
    filter_indexed_keys,
    parse_indexed,
)


class AudioWLiveCardSlotConfigCodec:
    @staticmethod
    def decode(data: dict) -> AudioWLiveCardSlotConfig:
        return AudioWLiveCardSlotConfig(
            rectracks=int(data["rectracks"]),
            playmode=data["playmode"],
        )

    @staticmethod
    def encode(obj: AudioWLiveCardSlotConfig) -> dict:
        return {
            "rectracks": str(obj.rectracks),
            "playmode": obj.playmode,
        }


class AudioWLiveCardSlotCodec:
    @staticmethod
    def decode(data: dict) -> AudioWLiveCardSlot:
        return AudioWLiveCardSlot(
            config=AudioWLiveCardSlotConfigCodec.decode(data["cfg"])
        )

    @staticmethod
    def encode(obj: AudioWLiveCardSlot) -> dict:
        return {
            "cfg": AudioWLiveCardSlotConfigCodec.encode(obj.config),
        }


class AudioWLiveCardCodec:
    @staticmethod
    def decode(data: dict) -> AudioWLiveCard:
        return AudioWLiveCard(
            sd_link_mode=data["sdlink"],
            auto_input=data["autoin"],
            show_meters=data["meters"],
            auto_stop=data["auto_stop"],
            auto_play=data["auto_play"],
            auto_record=data["auto_rec"],

            slots=parse_indexed(
                filter_indexed_keys(data),
                AudioWLiveCardSlotCodec.decode,
            ),
        )

    @staticmethod
    def encode(obj: AudioWLiveCard) -> dict:
        return {
            "sdlink": obj.sd_link_mode,
            "autoin": obj.auto_input,
            "meters": obj.show_meters,
            "auto_stop": obj.auto_stop,
            "auto_play": obj.auto_play,
            "auto_rec": obj.auto_record,

            **obj.slots.to_dict(
                serializer=AudioWLiveCardSlotCodec.encode
            ),
        }


class AudioWMADICardCodec:
    @staticmethod
    def decode(data: dict) -> AudioWMADICard:
        return AudioWMADICard(
            mode=data["mode"],
            rxclock=data["rxclock"],
        )

    @staticmethod
    def encode(obj: AudioWMADICard) -> dict:
        return {
            "mode": obj.mode,
            "rxclock": obj.rxclock,
        }


class AudioCardsCodec:
    @staticmethod
    def decode(data: dict) -> AudioCards:
        return AudioCards(
            wlive_card=AudioWLiveCardCodec.decode(data["wlive"]),
            wmadi_card=AudioWMADICardCodec.decode(data["wmadi"]),
        )

    @staticmethod
    def encode(obj: AudioCards) -> dict:
        return {
            "wlive": AudioWLiveCardCodec.encode(obj.wlive_card),
            "wmadi": AudioWMADICardCodec.encode(obj.wmadi_card),
        }