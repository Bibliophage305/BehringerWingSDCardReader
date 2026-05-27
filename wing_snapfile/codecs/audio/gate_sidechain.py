from wing_snapfile.models.audio.gate_sidechain import GateSidechain


class GateSidechainCodec:
    @staticmethod
    def decode(data: dict) -> GateSidechain:
        return GateSidechain(
            type=data["type"],
            frequency=float(data["f"]),
            q=float(data["q"]),
            source=data["src"],
            tap=data["tap"],
        )

    @staticmethod
    def encode(obj: GateSidechain) -> dict:
        return {
            "type": obj.type,
            "f": obj.frequency,
            "q": obj.q,
            "src": obj.source,
            "tap": obj.tap,
        }
