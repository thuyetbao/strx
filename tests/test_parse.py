#!/bin/python3

# Global
import sys
import os

sys.path.append(os.path.abspath(os.curdir))

# External
import pytest

# Internal
import strx


@pytest.mark.parametrize("str, output", [("1,000,000.00", float(1000000)), ("1000000.00", float(1000000)), ("23,2345,12", float(23234512))])
def test_easy_seperator(str, output):
    assert strx.str_to_number(str, decimal_seperator=".", thousand_seperator=",") == output


@pytest.mark.parametrize("str, output", [("231.800.000,00", 231800000)])
def test_diff_seperator(str, output):
    assert strx.str_to_number(str, decimal_seperator=",", thousand_seperator=".") == output


def test_fail_multiple_decimal():
    with pytest.raises(ValueError):
        strx.str_to_number("19242.00.00", decimal_seperator=".", thousand_seperator=",")


@pytest.mark.parametrize(
    "val, expected_result",
    [
        ("350:100", 350 / 100),
        ("1,000:276", 1000 / 276),
        ([1, 2], 0.5),
        (["1", "2"], 0.5),
        (("1", "3"), 1 / 3),
        ((2, "3"), 2 / 3),
        (("10,000 : 200"), 10000 / 200),
        (("15,300", " 60 "), 15300 / 60),
        (("3 ", " 1"), 3.0),
    ],
)
def test_output_desired(val, expected_result):
    assert strx.str_to_ratio(x=val) == expected_result


@pytest.mark.parametrize(
    "val",
    [
        (None),
        ("10.9,000:276"),
        (["9000.0.0000", 2]),
        ([(1, 2, 1), 30]),
        ((3, 4, 5)),
    ],
)
def test_failed_parse(val):
    assert strx.str_to_ratio(x=val) is None
