from wing_snapfile.models.audio.dynamics_crossover import AudioDynamicsCrossover


class AudioDynamicsCrossoverCodec:
    @staticmethod
    def decode(data: dict) -> AudioDynamicsCrossover:
        return AudioDynamicsCrossover(
            depth=data["depth"],
            type=data["type"],
            frequency=float(data["f"]),
            q=float(data["q"]),
        )

    @staticmethod
    def encode(obj: AudioDynamicsCrossover) -> dict:
        return {
            "depth": obj.depth,
            "type": obj.type,
            "f": obj.frequency,
            "q": obj.q,
        }
