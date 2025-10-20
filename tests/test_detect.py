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
    "string, pattern",
    [
        ("350:100", re.compile(r"\d+")),
        ("There are 10 persons", re.compile(r"\d+")),
        ("First match with F", re.compile(r"^F", re.I)),
        ("There are exist date on year 2022", re.compile(r"\d{4}$")),
    ],
)
def test_true_detect(string, pattern):
    assert strx.str_detect(string, pattern) is True


@pytest.mark.parametrize(
    "string, pattern",
    [
        ("Not exist any number", re.compile(r"\d+")),
        ("- Failed first character, need to be +", re.compile(r"^\+")),
    ],
)
def test_failed_detect(string, pattern):
    assert strx.str_detect(string, pattern) is False
