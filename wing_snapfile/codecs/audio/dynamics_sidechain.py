from wing_snapfile.models.audio.dynamics_sidechain import AudioDynamicsSidechain


class AudioDynamicsSidechainCodec:
    @staticmethod
    def decode(data: dict) -> AudioDynamicsSidechain:
        return AudioDynamicsSidechain(
            type=data["type"],
            frequency=float(data["f"]),
            q=float(data["q"]),
            source=data["src"],
            tap=data["tap"],
        )

    @staticmethod
    def encode(obj: AudioDynamicsSidechain) -> dict:
        return {
            "type": obj.type,
            "f": obj.frequency,
            "q": obj.q,
            "src": obj.source,
            "tap": obj.tap,
        }
