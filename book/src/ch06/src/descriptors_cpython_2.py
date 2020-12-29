"""Clean Code in Python - Chapter 6: Descriptors

> How Python uses descriptors internally: __slots__
"""
from dataclasses import dataclass


@dataclass
class Coordinate2D:
    """Example of a class that uses __slots__."""

    __slots__ = ("lat", "long")

    lat: float
    long: float

    def __repr__(self):
        return f"{self.__class__.__name__}({self.lat}, {self.long})"
