from wing_snapfile.models.audio.expansion_cards import (
    ExpansionCards,
    WLiveCard,
    WLiveCardSlot,
    WLiveCardSlotConfig,
    WMADICard,
)

from wing_snapfile.helpers.indexed import (
    encode_one_indexed_list,
    filter_indexed_keys,
    decode_one_indexed_list,
)


class WLiveCardSlotConfigCodec:
    @staticmethod
    def decode(data: dict) -> WLiveCardSlotConfig:
        return WLiveCardSlotConfig(
            rectracks=int(data["rectracks"]),
            playmode=data["playmode"],
        )

    @staticmethod
    def encode(obj: WLiveCardSlotConfig) -> dict:
        return {
            "rectracks": str(obj.rectracks),
            "playmode": obj.playmode,
        }


class WLiveCardSlotCodec:
    @staticmethod
    def decode(data: dict) -> WLiveCardSlot:
        return WLiveCardSlot(
            config=WLiveCardSlotConfigCodec.decode(data["cfg"])
        )

    @staticmethod
    def encode(obj: WLiveCardSlot) -> dict:
        return {
            "cfg": WLiveCardSlotConfigCodec.encode(obj.config),
        }


class WLiveCardCodec:
    @staticmethod
    def decode(data: dict) -> WLiveCard:
        return WLiveCard(
            sd_link_mode=data["sdlink"],
            auto_input=data["autoin"],
            show_meters=data["meters"],
            auto_stop=data["auto_stop"],
            auto_play=data["auto_play"],
            auto_record=data["auto_rec"],

            slots=decode_one_indexed_list(
                filter_indexed_keys(data),
                WLiveCardSlotCodec.decode,
            ),
        )

    @staticmethod
    def encode(obj: WLiveCard) -> dict:
        return {
            "sdlink": obj.sd_link_mode,
            "autoin": obj.auto_input,
            "meters": obj.show_meters,
            "auto_stop": obj.auto_stop,
            "auto_play": obj.auto_play,
            "auto_rec": obj.auto_record,
            **encode_one_indexed_list(obj.slots, WLiveCardSlotCodec.encode),
        }


class WMADICardCodec:
    @staticmethod
    def decode(data: dict) -> WMADICard:
        return WMADICard(
            mode=data["mode"],
            rxclock=data["rxclock"],
        )

    @staticmethod
    def encode(obj: WMADICard) -> dict:
        return {
            "mode": obj.mode,
            "rxclock": obj.rxclock,
        }


class ExpansionCardsCodec:
    @staticmethod
    def decode(data: dict) -> ExpansionCards:
        return ExpansionCards(
            wlive_card=WLiveCardCodec.decode(data["wlive"]),
            wmadi_card=WMADICardCodec.decode(data["wmadi"]),
        )

    @staticmethod
    def encode(obj: ExpansionCards) -> dict:
        return {
            "wlive": WLiveCardCodec.encode(obj.wlive_card),
            "wmadi": WMADICardCodec.encode(obj.wmadi_card),
        }