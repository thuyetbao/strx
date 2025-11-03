#!/bin/python3

# Global
import sys
import os

sys.path.append(os.path.abspath(os.curdir))

# External
import pytest

# Internal
import strx


@pytest.mark.parametrize("value, output", [("1,000,000.00", float(1000000)), ("1000000.00", float(1000000)), ("23,2345,12", float(23234512))])
def test_easy_seperator(value, output):
    assert strx.str_to_number(value, radix="DECIMAL") == output


@pytest.mark.parametrize("value, output", [("231.800.000,00", 231800000)])
def test_diff_seperator(value, output):
    assert strx.str_to_number(value, radix="COMMA") == output


def test_fail_multiple_decimal():
    with pytest.raises(ValueError):
        strx.str_to_number("19242.00.00", radix="DECIMAL")


@pytest.mark.parametrize(
    "value, expected_result",
    [
        ("350:100", 350 / 100),
        ("1,000:276", 1000 / 276),
    ],
)
def test_output_desired(value, expected_result):
    assert strx.str_to_ratio(string=value) == expected_result


@pytest.mark.parametrize(
    "value",
    [
        (None),
        ("10.9,000:276"),
        (["9000.0.0000", 2]),
    ],
)
def test_failed_parse(value):
    assert strx.str_to_ratio(string=value) is None
