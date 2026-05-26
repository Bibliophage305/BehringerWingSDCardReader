from wing_snapfile.models.audio.gate_sidechain import AudioGateSidechain


class AudioGateSidechainCodec:
    @staticmethod
    def decode(data: dict) -> AudioGateSidechain:
        return AudioGateSidechain(
            type=data["type"],
            frequency=float(data["f"]),
            q=float(data["q"]),
            source=data["src"],
            tap=data["tap"],
        )

    @staticmethod
    def encode(obj: AudioGateSidechain) -> dict:
        return {
            "type": obj.type,
            "f": obj.frequency,
            "q": obj.q,
            "src": obj.source,
            "tap": obj.tap,
        }
