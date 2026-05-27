from wing_snapfile.models.audio.dca import DCA


class DCACodec:
    @staticmethod
    def decode(data: dict) -> DCA:
        return DCA(
            name=data["name"],
            color=data["col"],
            icon=data["icon"],
            led_on=data["led"],
            mute_on=data["mute"],
            fader_level=float(data["fdr"]),
            monitor_mode=data["mon"],
        )

    @staticmethod
    def encode(obj: DCA) -> dict:
        return {
            "name": obj.name,
            "col": obj.color,
            "icon": obj.icon,
            "led": obj.led_on,
            "mute": obj.mute_on,
            "fdr": obj.fader_level,
            "mon": obj.monitor_mode,
        }
