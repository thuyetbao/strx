#!/bin/python3

# Global
import enum


@enum.unique
class EnumurationRadix(enum.Enum):
    DOT = (".", ",")
    COMMA = (",", ".")

    def __init__(self, symbol: str, delimiter: str):
        self.symbol = symbol
        self.point = symbol
        self.delimiter = delimiter

    def __str__(self):
        return self.symbol

    @classmethod
    def search(cls, keyword: str) -> "EnumurationRadix":
        for mem in cls:
            if keyword == mem.symbol or keyword == mem.name:
                return mem
        raise ValueError(f"Not exist radix point with keyword={keyword} on enumuration {repr(cls)}")


@enum.unique
class EnumurationDelimiter(enum.Enum):
    DOT = "."
    COMMA = ","
    THIN_SPACE = ""
    HALF_SPACE = " "
    FULL_SPACE = " "
    UNDERSCORE = "_"
    APOSTROPHE = "'"

    def __init__(self, symbol: str):
        self.symbol = symbol

    def __str__(self):
        return self.symbol

    @classmethod
    def search(cls, keyword: str) -> "EnumurationDelimiter":
        for mem in cls:
            if keyword == mem.symbol or keyword == mem.name:
                return mem
        raise ValueError(f"Not exist delimiter with keyword={keyword} on enumuration {repr(cls)}")
