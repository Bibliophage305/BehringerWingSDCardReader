from wing_snapfile.models.audio.send import AudioSend, AudioLimitedSend, AudioFullSend


class AudioSendCodec:
    @staticmethod
    def decode(data: dict) -> AudioSend:
        return AudioSend(
            on=data["on"],
            fader_level=float(data["lvl"]),
        )

    @staticmethod
    def encode(obj: AudioSend) -> dict:
        return {
            "on": obj.on,
            "lvl": obj.fader_level,
        }


class AudioLimitedSendCodec:
    @staticmethod
    def decode(data: dict) -> AudioLimitedSend:
        return AudioLimitedSend(
            on=data["on"],
            fader_level=float(data["lvl"]),
            pre_fader=data["pre"],
        )

    @staticmethod
    def encode(obj: AudioLimitedSend) -> dict:
        return {
            "on": obj.on,
            "lvl": obj.fader_level,
            "pre": obj.pre_fader,
        }


class AudioFullSendCodec:
    @staticmethod
    def decode(data: dict) -> AudioFullSend:
        return AudioFullSend(
            on=data["on"],
            fader_level=float(data["lvl"]),
            pre_always_on=data["pon"],
            mode=data["mode"],
            pan_link=data["plink"],
            pan=int(data["pan"]),
        )

    @staticmethod
    def encode(obj: AudioFullSend) -> dict:
        return {
            "on": obj.on,
            "lvl": obj.fader_level,
            "pon": obj.pre_always_on,
            "mode": obj.mode,
            "plink": obj.pan_link,
            "pan": obj.pan,
        }
