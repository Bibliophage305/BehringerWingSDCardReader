from wing_snapfile.models.audio.dca import AudioDCA


class AudioDCACodec:
    @staticmethod
    def decode(data: dict) -> AudioDCA:
        return AudioDCA(
            name=data["name"],
            color=data["col"],
            icon=data["icon"],
            led_on=data["led"],
            mute_on=data["mute"],
            fader_level=float(data["fdr"]),
            monitor_mode=data["mon"],
        )

    @staticmethod
    def encode(obj: AudioDCA) -> dict:
        return {
            "name": obj.name,
            "col": obj.color,
            "icon": obj.icon,
            "led": obj.led_on,
            "mute": obj.mute_on,
            "fdr": obj.fader_level,
            "mon": obj.monitor_mode,
        }
