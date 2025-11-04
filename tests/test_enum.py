#!/bin/python3

# Global
import sys
import os

# Path
sys.path.append(os.path.abspath(os.curdir))

# External
import pytest

# Internal
import strx._constant as constant


def test_search_raises_value_error_for_invalid_keyword_radix():
    with pytest.raises(ValueError) as excinfo:
        constant.EnumurationRadix.search("INVALID")

    msg = str(excinfo.value)
    assert "Not exist radix point" in msg
    assert "INVALID" in msg


def test_search_raises_value_error_for_invalid_keyword_delimiter():
    with pytest.raises(ValueError) as excinfo:
        constant.EnumurationDelimiter.search("INVALID")

    msg = str(excinfo.value)
    assert "Not exist delimiter" in msg
    assert "INVALID" in msg
