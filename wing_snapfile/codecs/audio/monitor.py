from wing_snapfile.models.audio.monitor import (
    AudioMonitor,
    AudioMonitorEQ,
    AudioMonitorDelay,
)

class AudioMonitorEQCodec:
    @staticmethod
    def decode(data: dict) -> AudioMonitorEQ:
        return AudioMonitorEQ(
            on=data["on"],
            lsg=float(data["lsg"]),
            lsf=float(data["lsf"]),

            g1=float(data["1g"]),
            f1=float(data["1f"]),
            q1=float(data["1q"]),

            g2=float(data["2g"]),
            f2=float(data["2f"]),
            q2=float(data["2q"]),

            g3=float(data["3g"]),
            f3=float(data["3f"]),
            q3=float(data["3q"]),

            g4=float(data["4g"]),
            f4=float(data["4f"]),
            q4=float(data["4q"]),

            g5=float(data["5g"]),
            f5=float(data["5f"]),
            q5=float(data["5q"]),

            g6=float(data["6g"]),
            f6=float(data["6f"]),
            q6=float(data["6q"]),

            hsg=float(data["hsg"]),
            hsf=float(data["hsf"]),
        )

    @staticmethod
    def encode(obj: AudioMonitorEQ) -> dict:
        return {
            "on": obj.on,
            "lsg": obj.lsg,
            "lsf": obj.lsf,

            "1g": obj.g1,
            "1f": obj.f1,
            "1q": obj.q1,

            "2g": obj.g2,
            "2f": obj.f2,
            "2q": obj.q2,

            "3g": obj.g3,
            "3f": obj.f3,
            "3q": obj.q3,

            "4g": obj.g4,
            "4f": obj.f4,
            "4q": obj.q4,

            "5g": obj.g5,
            "5f": obj.f5,
            "5q": obj.q5,

            "6g": obj.g6,
            "6f": obj.f6,
            "6q": obj.q6,

            "hsg": obj.hsg,
            "hsf": obj.hsf,
        }
    
class AudioMonitorDelayCodec:
    @staticmethod
    def decode(data: dict) -> AudioMonitorDelay:
        return AudioMonitorDelay(
            on=data["on"],
            metres=float(data["m"]),
        )

    @staticmethod
    def encode(obj: AudioMonitorDelay) -> dict:
        return {
            "on": obj.on,
            "m": obj.metres,
        }

class AudioMonitorCodec:
    @staticmethod
    def decode(data: dict) -> AudioMonitor:
        return AudioMonitor(
            fader_level=float(data["lvl"]),
            phase_invert=data["inv"],

            pan=data["pan"],
            width=data["wid"],

            eq=AudioMonitorEQCodec.decode(data["eq"]),
            limiter_threshold=data["lim"],

            delay=AudioMonitorDelayCodec.decode(data["dly"]),

            dim=data["dim"],
            pfl_dim=data["pfldim"],
            band_solo_trim=data["eqbdtrim"],

            source_level=float(data["srclvl"]),
            source_mix=float(data["srcmix"]),

            source=data["src"],
            direct_input=data["dirin"],

            tags=data["tags"].split(",") if data.get("tags") else [],
        )

    @staticmethod
    def encode(obj: AudioMonitor) -> dict:
        return {
            "lvl": obj.fader_level,
            "inv": obj.phase_invert,

            "pan": obj.pan,
            "wid": obj.width,

            "eq": AudioMonitorEQCodec.encode(obj.eq),
            "lim": obj.limiter_threshold,

            "dly": AudioMonitorDelayCodec.encode(obj.delay),

            "dim": obj.dim,
            "pfldim": obj.pfl_dim,
            "eqbdtrim": obj.band_solo_trim,

            "srclvl": obj.source_level,
            "srcmix": obj.source_mix,

            "src": obj.source,
            "dirin": obj.direct_input,

            "tags": ",".join(obj.tags),
        }