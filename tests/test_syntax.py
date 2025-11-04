#!/bin/python3

# Global
import sys
import os

# Path
sys.path.append(os.path.abspath(os.curdir))

# External
import pytest

# Internal
import strx


@pytest.mark.parametrize(
    "func",
    [
        strx.str_length,
        # strx.str_sub,
        strx.str_trim,
        strx.str_reverse,
        # strx.str_detect,
        strx.str_snakecase,
        # strx.str_remove,
        # strx.str_replace,
        # strx.str_replace_all,
        # strx.str_pad,
        # strx.str_split,
        # strx.str_count,
        # strx.str_which,
        strx.str_sort,
        strx.str_unique,
        # strx.str_dup,
        strx.str_c,
        # strx.str_extract,
        # strx.str_extract_all,
        strx.str_to_upper,
        strx.str_to_lower,
        strx.str_to_title,
        strx.str_to_number,
        strx.str_to_ratio,
        strx.str_normalize,
    ],
)
def test_type_error_for_non_string_inputs(func):
    with pytest.raises(TypeError) as excinfo:
        func(123)
    assert "Required value of type 'str'" in str(excinfo.value)
