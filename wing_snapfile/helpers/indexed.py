from wing_snapfile.types.one_indexed_list import OneIndexedList
from typing import Callable


def parse_indexed(data: dict, decoder: Callable) -> OneIndexedList:
    return OneIndexedList.from_indexed_dict(data, decoder)


def encode_indexed(
    data: OneIndexedList,
    encoder: Callable = lambda x: x,
    offset: int = 0,
    prefix: str = "",
) -> dict:
    return data.to_dict(encoder=encoder, offset=offset, prefix=prefix)


def filter_indexed_keys(data: dict) -> dict:
    return {
        k: v
        for k, v in data.items()
        if k.isdigit()
    }