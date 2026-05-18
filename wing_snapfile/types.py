class OneIndexedList(list):
    """List with 1-based integer indexing for direct snapfile key parity."""

    def __getitem__(self, index):
        if isinstance(index, int):
            if index == 0:
                raise IndexError("OneIndexedList is 1-indexed")
            if index > 0:
                return super().__getitem__(index - 1)
            return super().__getitem__(index)
        if isinstance(index, slice):
            start = None if index.start is None else max(index.start - 1, 0)
            stop = None if index.stop is None else max(index.stop - 1, 0)
            step = index.step
            return OneIndexedList(super().__getitem__(slice(start, stop, step)))
        raise TypeError("Indices must be integers or slices")
    
    @classmethod
    def from_indexed_dict(cls, data: dict[str, object], parser=lambda x: x) -> "OneIndexedList":
        items = OneIndexedList()
        for i, (k, v) in enumerate(sorted(data.items(), key=lambda pair: int(pair[0]))):
            if k != str(i + 1):
                raise ValueError(f"Expected contiguous 1-indexed keys, found {k} at position {i + 1}")
            items.append(parser(v))
        return items