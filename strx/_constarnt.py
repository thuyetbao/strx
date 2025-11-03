#!/bin/python3

# Global
import enum


@enum.unique
class RadixPoint(enum.Enum):
    DECIMAL = (".", ",")
    COMMA = (",", ",")
    THIN_SPACE = ("", ",")
    SPACE = (" ", ",")
    UNDERSCORE = ("_", ",")
    APOSTROPHE = ("'", ",")
    HALF_SPACE = (" ", ",")
    FULL_SPACE = (" ", ",")

    def __init__(self, symbol: str, thousand_point: str):
        self.symbol = symbol
        self.decimal_point = symbol
        self.thousand_point = thousand_point

    def __str__(self):
        return self.symbol


# from typing import Literal

# Literal["DECIMAL", "COMMA", "THIN_SPACE", "SPACE", "UNDERSCORE", "APOSTROPHE", "HALF_SPACE", "FULL_SPACE"]
