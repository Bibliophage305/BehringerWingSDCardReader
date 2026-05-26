from wing_snapfile.models.snapfile import Snapfile
from wing_snapfile.protocol.codecs.snapfile import SnapfileCodec

def load_snapfile(data: dict) -> Snapfile:
    return SnapfileCodec.decode(data)

def dump_snapfile(snapfile: Snapfile) -> dict:
    return SnapfileCodec.encode(snapfile)