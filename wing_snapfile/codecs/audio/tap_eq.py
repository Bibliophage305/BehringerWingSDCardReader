from wing_snapfile.models.audio.tap_eq import AudioTapEQ


class AudioTapEQCodec:
    @staticmethod
    def decode(data: dict) -> AudioTapEQ:
        return AudioTapEQ(
            on=data["on"],
            band1_gain=float(data["1g"]),
            band1_freq=float(data["1f"]),
            band1_q=float(data["1q"]),
            band2_gain=float(data["2g"]),
            band2_freq=float(data["2f"]),
            band2_q=float(data["2q"]),
            band3_gain=float(data["3g"]),
            band3_freq=float(data["3f"]),
            band3_q=float(data["3q"]),
        )

    @staticmethod
    def encode(obj: AudioTapEQ) -> dict:
        return {
            "on": obj.on,
            "1g": obj.band1_gain,
            "1f": obj.band1_freq,
            "1q": obj.band1_q,
            "2g": obj.band2_gain,
            "2f": obj.band2_freq,
            "2q": obj.band2_q,
            "3g": obj.band3_gain,
            "3f": obj.band3_freq,
            "3q": obj.band3_q,
        }
