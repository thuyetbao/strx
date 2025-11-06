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
def test_normalize_with_default_form(value, form, output):
    assert strx.str_normalize(value, form=form, strip=True) == output


@pytest.mark.parametrize(
    "value, form, strip, output",
    [
        (" This included various type of space with space.              ", "NFKC", True, "This included various type of space with space."),
        ("    “This included various type of space with space”    ", "NFKC", False, ' "This included various type of space with space" '),
    ],
)
def test_normalize_with_different_strip(value, form, strip, output):
    assert strx.str_normalize(string=value, form=form, strip=strip) == output
