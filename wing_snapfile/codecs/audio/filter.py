from wing_snapfile.models.audio.filter import Filter


class FilterCodec:
    @staticmethod
    def decode(data: dict) -> Filter:
        return Filter(
            low_cut_enabled=data["lc"],
            low_cut_frequency=float(data["lcf"]),
            low_cut_slope=data["lcs"],
            high_cut_enabled=data["hc"],
            high_cut_frequency=float(data["hcf"]),
            high_cut_slope=data["hcs"],
            tilt_enabled=data["tf"],
            tilt_mode=data["mdl"],
            tilt_amount=float(data["tilt"]),
        )

    @staticmethod
    def encode(obj: Filter) -> dict:
        return {
            "lc": obj.low_cut_enabled,
            "lcf": obj.low_cut_frequency,
            "lcs": obj.low_cut_slope,
            "hc": obj.high_cut_enabled,
            "hcf": obj.high_cut_frequency,
            "hcs": obj.high_cut_slope,
            "tf": obj.tilt_enabled,
            "mdl": obj.tilt_mode,
            "tilt": obj.tilt_amount,
        }
