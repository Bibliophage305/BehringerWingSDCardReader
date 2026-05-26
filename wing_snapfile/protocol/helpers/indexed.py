from wing_snapfile.types.one_indexed_list import OneIndexedList


def parse_indexed(data, decoder):
    return OneIndexedList.from_indexed_dict(data, decoder)


def filter_indexed_keys(data):
    return {
        k: v
        for k, v in data.items()
        if k.isdigit()
    }