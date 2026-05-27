from wing_snapfile.models.audio.dynamics_sidechain import DynamicsSidechain


class DynamicsSidechainCodec:
    @staticmethod
    def decode(data: dict) -> DynamicsSidechain:
        return DynamicsSidechain(
            type=data["type"],
            frequency=float(data["f"]),
            q=float(data["q"]),
            source=data["src"],
            tap=data["tap"],
        )

    @staticmethod
    def encode(obj: DynamicsSidechain) -> dict:
        return {
            "type": obj.type,
            "f": obj.frequency,
            "q": obj.q,
            "src": obj.source,
            "tap": obj.tap,
        }
