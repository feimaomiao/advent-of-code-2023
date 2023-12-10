import re
from typing import List, Any, Self


class nrange:
    def __init__(self, a: int, b: int):
        self.start: int = a
        self.stop: int = b
        self.valid: bool = True

    def __iter__(self):
        return iter(range(self.start, self.stop))

    def __eq__(self, other):
        if type(other) != nrange and type(other) != range:
            raise TypeError
        return self.start == other.start and self.stop == other.stop

    def __repr__(self) -> str:
        if self.valid:
            return f"nrange[{self.start},{self.stop})"
        else:
            return " " + "".join(
                ["\u0336{}".format(c) for c in repr(nrange(self.start, self.stop))]
            )

    def intersection(self, other) -> Self:
        if type(other) != nrange and type(other) != range:
            print("abc")
            raise TypeError
        if self.stop <= other.start or self.start >= other.stop:
            print("DF")
            return None
        print("IM HERE")
        return nrange(max(self.start, other.start), min(self.stop, other.stop))

    def __and__(self, other) -> Self:
        if type(other) != nrange and type(other) != range:
            return None
        return self.intersection(other)


# def intList(s: str)->List[int]
