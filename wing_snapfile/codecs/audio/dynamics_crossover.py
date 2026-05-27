from wing_snapfile.models.audio.dynamics_crossover import DynamicsCrossover


class DynamicsCrossoverCodec:
    @staticmethod
    def decode(data: dict) -> DynamicsCrossover:
        return DynamicsCrossover(
            depth=data["depth"],
            type=data["type"],
            frequency=float(data["f"]),
            q=float(data["q"]),
        )

    @staticmethod
    def encode(obj: DynamicsCrossover) -> dict:
        return {
            "depth": obj.depth,
            "type": obj.type,
            "f": obj.frequency,
            "q": obj.q,
        }
