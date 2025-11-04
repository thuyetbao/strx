#!/bin/python3

# Global
import sys
import os
import math

sys.path.append(os.path.abspath(os.curdir))

# External
import pytest

# Internal
import strx


@pytest.mark.parametrize(
    "value, radix, delimiter, output",
    [
        ("1,000,000.00", "DOT", "auto", float(1000000)),
        ("1000000.00", "DOT", "auto", float(1000000)),
        ("23,234,512", "DOT", "auto", float(23234512)),
        ("231.800.000,00", "COMMA", "auto", float(231800000)),
        ("11.345,00", "COMMA", "DOT", float(11345)),
        ("92,245.00", "DOT", "COMMA", float(92245)),
        ("87672,00", "COMMA", "THIN_SPACE", float(87672)),
        ("75 224 192,00", "COMMA", "HALF_SPACE", float(75224192)),
        ("66 666,00", "COMMA", "FULL_SPACE", float(66666)),
        ("1_000_000,00", "COMMA", "UNDERSCORE", float(1000000)),
        ("720'055,00", "COMMA", "APOSTROPHE", float(720055)),
    ],
)
def test_parse_number_success(value, radix, delimiter, output):
    assert math.isclose(strx.str_to_number(value, radix=radix, delimiter=delimiter), output)


def test_parse_number_failure_on_multiple_decimal():
    with pytest.raises(ValueError):
        strx.str_to_number("19242.00.00", radix="DOT")


def test_parse_number_failure_on_same_radix_and_delimiter():
    with pytest.raises(ValueError):
        strx.str_to_number("1000,000.00", radix="DOT", delimiter="DOT")


@pytest.mark.parametrize(
    "value, sep_by, output",
    [
        ("350:100", ":", 350 / 100),
        ("1,000:276", ":", 1000 / 276),
        ("345.0/44", "/", 345 / 44),
    ],
)
def test_parse_ratio_success(value, sep_by, output):
    assert math.isclose(strx.str_to_ratio(string=value, sep_by=sep_by), output)


def test_parse_ratio_failure_by_denominator_is_zero():
    with pytest.raises(ZeroDivisionError):
        strx.str_to_ratio("350:0")
