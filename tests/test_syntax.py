#!/bin/python3

# Global
import sys
import os
import re

# Path
sys.path.append(os.path.abspath(os.curdir))

# External
import pytest

# Internal
import strx


@pytest.mark.parametrize(
    "func, kwargs",
    [
        (strx.str_length, None),
        (strx.str_sub, {"start": 0, "end": None}),
        (strx.str_trim, None),
        (strx.str_reverse, None),
        (strx.str_detect, {"pattern": re.compile(r"\d+")}),
        (strx.str_snakecase, None),
        (strx.str_remove, {"pattern": re.compile(r"\d+")}),
        (strx.str_replace, {"pattern": re.compile(r"\d+"), "replacement": ""}),
        (strx.str_replace_all, {"pattern": re.compile(r"\d+"), "replacement": ""}),
        (strx.str_pad, {"width": 10, "side": "right", "pad": "0"}),
        (strx.str_split, {"delimiter": ","}),
        (strx.str_count, {"pattern": re.compile(r"\d+")}),
        (strx.str_which, {"pattern": re.compile(r"\d+")}),
        (strx.str_sort, {"descending": True}),
        (strx.str_unique, None),
        (strx.str_dup, {"times": 2}),
        (strx.str_c, {"sep": ","}),
        (strx.str_extract, {"pattern": re.compile(r"\d+")}),
        (strx.str_extract_all, {"pattern": re.compile(r"\d+")}),
        (strx.str_to_upper, None),
        (strx.str_to_lower, None),
        (strx.str_to_title, None),
        (strx.str_to_number, {"radix": "DOT"}),
        (strx.str_to_ratio, {"sep_by": ":"}),
        (strx.str_normalize, {"form": "NFC"}),
    ],
)
def test_failure_on_failure_input_on_argument_string(func, kwargs):
    failure_input = 9090909
    with pytest.raises(TypeError) as excinfo:
        if kwargs is None:
            func(string=failure_input)
        else:
            func(string=failure_input, **kwargs)
    assert "Required value of type 'str'" in str(excinfo.value)
