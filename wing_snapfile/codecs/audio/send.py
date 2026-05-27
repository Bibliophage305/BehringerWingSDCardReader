from wing_snapfile.models.audio.send import BaseSend, Send, FullSend


class BaseSendCodec:
    @staticmethod
    def decode(data: dict) -> BaseSend:
        return BaseSend(
            on=data["on"],
            fader_level=float(data["lvl"]),
        )

    @staticmethod
    def encode(obj: BaseSend) -> dict:
        return {
            "on": obj.on,
            "lvl": obj.fader_level,
        }


class SendCodec:
    @staticmethod
    def decode(data: dict) -> Send:
        return Send(
            on=data["on"],
            fader_level=float(data["lvl"]),
            pre_fader=data["pre"],
        )

    @staticmethod
    def encode(obj: Send) -> dict:
        return {
            "on": obj.on,
            "lvl": obj.fader_level,
            "pre": obj.pre_fader,
        }


class FullSendCodec:
    @staticmethod
    def decode(data: dict) -> FullSend:
        return FullSend(
            on=data["on"],
            fader_level=float(data["lvl"]),
            pre_always_on=data["pon"],
            mode=data["mode"],
            pan_link=data["plink"],
            pan=int(data["pan"]),
        )

    @staticmethod
    def encode(obj: FullSend) -> dict:
        return {
            "on": obj.on,
            "lvl": obj.fader_level,
            "pon": obj.pre_always_on,
            "mode": obj.mode,
            "plink": obj.pan_link,
            "pan": obj.pan,
        }
