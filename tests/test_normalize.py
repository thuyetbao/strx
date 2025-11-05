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
    "value, form, output",
    [
        ("The quick brown fox jumps over the lazy dog.", "NFKC", "The quick brown fox jumps over the lazy dog."),
        ("“The quick brown fox jumps over the lazy dog.”", "NFKC", '"The quick brown fox jumps over the lazy dog."'),
    ],
)
def test_parse_number_success(value, form, output):
    assert strx.str_normalize(value, form=form) == output
