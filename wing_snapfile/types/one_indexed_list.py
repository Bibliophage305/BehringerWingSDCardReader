from typing import Generic, TypeVar, Protocol, runtime_checkable

T = TypeVar("T")


@runtime_checkable
class DictSerializable(Protocol):
    def to_dict(self) -> dict: ...


class OneIndexedList(list[T], Generic[T]):
    """List with 1-based indexing for snapfile key parity."""

    def __getitem__(self, index):
        if isinstance(index, int):
            if index == 0:
                raise IndexError("OneIndexedList is 1-indexed")
            if index > 0:
                return super().__getitem__(index - 1)
            return super().__getitem__(index)

        if isinstance(index, slice):
            start = None if index.start is None else index.start - 1
            stop = None if index.stop is None else index.stop - 1
            return OneIndexedList(super().__getitem__(slice(start, stop, index.step)))

        raise TypeError("Indices must be integers or slices")

    @classmethod
    def from_indexed_dict(cls, data: dict[str, T], parser=lambda x: x):
        try:
            items = sorted(data.items(), key=lambda p: int(p[0]))
        except ValueError as e:
            raise ValueError(f"Invalid indexed dict keys: {data}") from e

        out = OneIndexedList()

        for i, (k, v) in enumerate(items):
            expected = str(i + 1)
            if k != expected:
                raise ValueError(
                    f"Non-contiguous indexed list: expected {expected}, got {k}"
                )

            out.append(parser(v))

        return out

    def to_dict(self, offset=0, prefix=""):
        def _serialize(item):
            if isinstance(item, DictSerializable):
                return item.to_dict()
            return item

        return {
            f"{prefix}{i}": _serialize(item)
            for i, item in enumerate(self, start=1 + offset)
        }