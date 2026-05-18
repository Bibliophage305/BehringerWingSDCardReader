from dataclasses import dataclass

from wing_snapfile.types import OneIndexedList

JsonPrimitive = str | int | float | bool | None


@dataclass
class JsonScalar:
    value: JsonPrimitive


@dataclass
class JsonField:
    name: str
    value: "JsonNode"


@dataclass
class JsonObject:
    fields: list[JsonField]


@dataclass
class JsonArray:
    items: list["JsonNode"]


JsonNode = JsonScalar | JsonObject | JsonArray

# T = TypeVar("T")





@dataclass
class NamedObject:
    name: str
    value: JsonObject



@dataclass
class IoRoute:
    index: int
    route: JsonObject | JsonScalar


@dataclass
class IoRouteBank:
    name: str
    routes: list[IoRoute]

    @classmethod
    def from_dict(cls, name: str, value: object) -> "IoRouteBank":
        routes_data = value
        def parser(route_value: object, index: int) -> IoRoute:
            route_node = _parse_json_node(route_value)
            if isinstance(route_node, JsonArray):
                raise ValueError(f"Expected scalar or object route at {name}.{index}")
            return IoRoute(index=index, route=route_node)
        return IoRouteBank(name=name, routes=_parse_numbered_list(routes_data, parser))


@dataclass
class WLiveSlotConfig:
    playmode: str
    rectracks: str


@dataclass
class WLiveSlot:
    cfg: WLiveSlotConfig

    @classmethod
    def from_dict(cls, value: object, index: int) -> "WLiveSlot":
        slot = value
        cfg = slot["cfg"]
        return WLiveSlot(
            cfg=WLiveSlotConfig(
                playmode=cfg["playmode"],
                rectracks=cfg["rectracks"],
            )
        )


@dataclass
class WLiveCard:
    slots:list[WLiveSlot]
    autoin: str
    auto_play: str
    auto_rec: str
    auto_stop: str
    meters: bool
    sdlink: str


@dataclass
class AudioCards:
    wlive: WLiveCard

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioCards":
        wlive = data["wlive"]
        slots = _parse_numbered_list(wlive, WLiveSlot.from_dict)
        return AudioCards(
            wlive=WLiveCard(
                slots=slots,
                autoin=wlive["autoin"],
                auto_play=wlive["auto_play"],
                auto_rec=wlive["auto_rec"],
                auto_stop=wlive["auto_stop"],
                meters=wlive["meters"],
                sdlink=wlive["sdlink"],
            )
        )


@dataclass
class AudioPlay:
    repeat: bool


@dataclass
class AudioRec:
    channels: str
    path: str
    resolution: str


@dataclass
class ConsoleDataDaw:
    on: bool
    conn: str
    emul: str
    config: str
    ccup: bool
    disjog: bool
    preset: str

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "ConsoleDataDaw":
        return ConsoleDataDaw(
            on=data["on"],
            conn=data["conn"],
            emul=data["emul"],
            config=data["config"],
            ccup=data["ccup"],
            disjog=data["disjog"],
            preset=data["preset"],
        )


@dataclass
class GpioPin:
    gpstate: bool
    mode: str

    @classmethod
    def from_dict(cls, value: object, index: int) -> "GpioPin":
        gpio = value
        return GpioPin(
            gpstate=gpio["gpstate"],
            mode=gpio["mode"],
        )


@dataclass
class LayerAssignment:
    type: str
    i: int
    dst: int

    @classmethod
    def from_dict(cls, value: object, index: int) -> "LayerAssignment":
        assignment = value
        return LayerAssignment(
            type=assignment["type"],
            i=assignment["i"],
            dst=assignment["dst"],
        )


@dataclass
class LayerBank:
    assignments: list[LayerAssignment]
    name: str
    ofs: int

    @classmethod
    def from_dict(cls, value: object, index: int) -> "LayerBank":
        bank = value
        return LayerBank(
            assignments=_parse_numbered_list(bank, LayerAssignment.from_dict),
            name=bank["name"],
            ofs=bank["ofs"],
        )


@dataclass
class LayerSurface:
    banks: list[LayerBank]
    sel: int
    spidx: int

    @classmethod
    def from_dict(cls, value: object) -> "LayerSurface":
        surface = value
        return LayerSurface(
            banks=_parse_numbered_list(surface, LayerBank.from_dict),
            sel=surface["sel"],
            spidx=surface["spidx"],
        )


@dataclass
class NamedLayerSurface:
    name: str
    surface: LayerSurface


@dataclass
class ConsoleDataLayer:
    surfaces: list[NamedLayerSurface]

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "ConsoleDataLayer":
        surfaces = [
            NamedLayerSurface(name=name, surface=LayerSurface.from_dict(surface_value))
            for name, surface_value in data.items()
        ]
        return ConsoleDataLayer(surfaces=surfaces)


@dataclass
class UserAction:
    mode: str
    name: str

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "UserAction":
        return UserAction(
            mode=data["mode"],
            name=data["name"],
        )


@dataclass
class UserButton:
    led: bool
    col: int
    enc: UserAction
    bu: UserAction
    bd: UserAction

    @classmethod
    def from_dict(cls, value: object, index: int) -> "UserButton":
        button = value
        return UserButton(
            led=button["led"],
            col=button["col"],
            enc=UserAction.from_dict(button["enc"]),
            bu=UserAction.from_dict(button["bu"]),
            bd=UserAction.from_dict(button["bd"]),
        )


@dataclass
class UserPage:
    buttons: list[UserButton]

    @classmethod
    def from_dict(cls, value: object, index: int) -> "UserPage":
        page = value
        return UserPage(buttons=_parse_numbered_list(page, UserButton.from_dict))


@dataclass
class NamedNode:
    name: str
    value: JsonNode


@dataclass
class ConsoleDataUser:
    pages:list[UserPage]
    settings: list[NamedNode]

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "ConsoleDataUser":
        pages = _parse_numbered_list(data, UserPage.from_dict)
        settings = [
            NamedNode(name=name, value=_parse_json_node(value))
            for name, value in data.items()
            if not name.isdigit()
        ]
        return ConsoleDataUser(pages=pages, settings=settings)

@dataclass
class ConsoleDataConfig:
    lights: dict
    rta: dict
    muteovr: bool
    soloexcl: bool
    selfsolo: bool
    solofsel: bool
    sof2solo: bool
    layerlinkl: bool
    layerlinkr: bool
    autoview: bool
    csctouch: bool
    autosel_L: bool
    autosel_C: bool
    autosel_R: bool
    autosel_CMPCT: bool
    autosel_RCK: bool
    autosel_EXT: bool
    autosel_VRT: bool
    autosel_WEDIT: bool
    fdrbanking: bool
    soffdr: str
    sofbutton: str
    sofframe: bool
    sofmode: bool
    seldblclick: str
    usrmode: str
    mfdr: str
    cscmode: str
    rackmode: str
    busspill: bool
    mainspill: bool
    mtxspill: bool
    dcaspill: bool
    dcacc: bool
    showfdr: bool

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "ConsoleDataConfig":
        return ConsoleDataConfig(
            lights=data["lights"],
            rta=data["rta"],
            muteovr=data["muteovr"],
            soloexcl=data["soloexcl"],
            selfsolo=data["selfsolo"],
            solofsel=data["solofsel"],
            sof2solo=data["sof2solo"],
            layerlinkl=data["layerlinkl"],
            layerlinkr=data["layerlinkr"],
            autoview=data["autoview"],
            csctouch=data["csctouch"],
            autosel_L=data["autosel_L"],
            autosel_C=data["autosel_C"],
            autosel_R=data["autosel_R"],
            autosel_CMPCT=data["autosel_CMPCT"],
            autosel_RCK=data["autosel_RCK"],
            autosel_EXT=data["autosel_EXT"],
            autosel_VRT=data["autosel_VRT"],
            autosel_WEDIT=data["autosel_WEDIT"],
            fdrbanking=data["fdrbanking"],
            soffdr=data["soffdr"],
            sofbutton=data["sofbutton"],
            sofframe=data["sofframe"],
            sofmode=data["sofmode"],
            seldblclick=data["seldblclick"],
            usrmode=data["usrmode"],
            mfdr=data["mfdr"],
            cscmode=data["cscmode"],
            rackmode=data["rackmode"],
            busspill=data["busspill"],
            mainspill=data["mainspill"],
            mtxspill=data["mtxspill"],
            dcaspill=data["dcaspill"],
            dcacc=data["dcacc"],
            showfdr=data["showfdr"],
        )




def _parse_json_node(value: object) -> JsonNode:
    if isinstance(value, dict):
        fields: list[JsonField] = []
        for name, child in value.items():
            if not isinstance(name, str):
                raise ValueError("JSON object keys must be strings")
            fields.append(JsonField(name=name, value=_parse_json_node(child)))
        return JsonObject(fields=fields)

    if isinstance(value, list):
        return JsonArray(items=[_parse_json_node(item) for item in value])

    if isinstance(value, (str, int, float, bool)) or value is None:
        return JsonScalar(value=value)

    raise ValueError(f"Unsupported JSON value type: {type(value)!r}")


def _parse_numbered_list(data: dict[str, object], parser) -> OneIndexedList:
    numbered = sorted(
        ((int(k), v) for k, v in data.items() if k.isdigit()),
        key=lambda pair: pair[0],
    )
    if not numbered:
        return OneIndexedList()

    expected = 1
    result = OneIndexedList()
    for index, value in numbered:
        if index != expected:
            raise ValueError(
                f"Expected contiguous 1-indexed keys, found {index} at position {expected}"
            )
        result.append(parser(value, index))
        expected += 1
    return result


def _parse_json_object_list(data: dict[str, object]) -> OneIndexedList[JsonObject]:
    def parser(value: object, index: int) -> JsonObject:
        node = _parse_json_node(value)
        if not isinstance(node, JsonObject):
            raise ValueError(f"Expected object at index {index}")
        return node

    return _parse_numbered_list(data, parser)


def _parse_json_object_as_object(value: object) -> JsonObject:
    node = _parse_json_node(value)
    if not isinstance(node, JsonObject):
        raise ValueError(f"Expected object")
    return node
