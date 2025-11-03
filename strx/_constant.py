#!/bin/python3

# Global
import enum


@enum.unique
class RadixPoint(enum.Enum):
    DECIMAL = (".", ",")
    COMMA = (",", ",")
    THIN_SPACE = ("", ",")
    HALF_SPACE = (" ", ",")
    FULL_SPACE = (" ", ",")
    UNDERSCORE = ("_", ",")
    APOSTROPHE = ("'", ",")

    def __init__(self, symbol: str, thousand_point: str):
        self.symbol = symbol
        self.decimal_point = symbol
        self.thousand_point = thousand_point

    def __str__(self):
        return self.symbol

    @classmethod
    def search(cls, keyword: str) -> "RadixPoint":
        for mem in cls:
            if keyword == mem.symbol or keyword == mem.name:
                return mem
        raise ValueError(f"Can not find radix point with keyword: {keyword}")
