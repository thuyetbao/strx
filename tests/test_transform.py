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
    "value, output",
    [
        ("The quick brown fox jumps over the lazy dog.", 44),
    ],
)
def test_length(value, output):
    assert strx.str_length(string=value) == output


@pytest.mark.parametrize(
    "value, output",
    [
        ("The quick brown fox jumps over the lazy dog.", "The quick brown fox jumps over the lazy dog."),
    ],
)
def test_trim(value, output):
    assert strx.str_trim(string=value) == output


@pytest.mark.parametrize(
    "value, output",
    [
        ("The quick brown fox jumps over the lazy dog.", "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG."),
    ],
)
def test_upper(value, output):
    assert strx.str_to_upper(string=value) == output


@pytest.mark.parametrize(
    "value, output",
    [
        ("The quick brown fox jumps over the lazy dog.", "the quick brown fox jumps over the lazy dog."),
    ],
)
def test_lower(value, output):
    assert strx.str_to_lower(string=value) == output


@pytest.mark.parametrize(
    "value, output",
    [
        ("The quick brown fox jumps over the lazy dog.", "The Quick Brown Fox Jumps Over The Lazy Dog."),
    ],
)
def test_title(value, output):
    assert strx.str_to_title(string=value) == output


@pytest.mark.parametrize(
    "value, output",
    [
        ("The quick brown fox jumps over the lazy dog.", ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."]),
    ],
)
def test_split(value, output):
    assert strx.str_split(string=value, delimiter=" ") == output


@pytest.mark.parametrize(
    "value, output",
    [
        ("The quick brown fox jumps over the lazy dog.", "the_quick_brown_fox_jumps_over_the_lazy_dog"),
    ],
)
def test_snakecase(value, output):
    assert strx.str_snakecase(string=value) == output


# @pytest.mark.parametrize(
#     "value, width, side, pad, output",
#     [
#         ("The quick brown fox jumps over the lazy dog.", 44, "right", " ", "The quick brown fox jumps over the lazy dog."),
#         ("The quick brown fox jumps over the lazy dog.", 44, "left", " ", " The quick brown fox jumps over the lazy dog."),
#         ("The quick brown fox jumps over the lazy dog.", 44, "both", " ", "  The quick brown fox jumps over the lazy dog.  "),
#     ],
# )
# def test_pad(value, width, side, pad, output):
#     assert strx.str_pad(string=value, width=width, side=side, pad=pad) == output


@pytest.mark.parametrize(
    "value, pattern, output",
    [
        ("The quick brown fox jumps over the lazy dog.", "fox", 1),
    ],
)
def test_count(value, pattern, output):
    assert strx.str_count(string=value, pattern=pattern) == output


# @pytest.mark.parametrize(
#     "value, pattern, output",
#     [
#         ("The quick brown fox jumps over the lazy dog.", "fox", 6),
#     ],
# )
# def test_which(value, pattern, output):
#     assert strx.str_which(string=value, pattern=pattern) == output


# @pytest.mark.parametrize(
#     "value, descending, output",
#     [
#         ("The quick brown fox jumps over the lazy dog.", False, "brown dog fox jumps lazy over quick The"),
#         ("The quick brown fox jumps over the lazy dog.", True, "The quick brown fox jumps over the lazy dog."),
#     ],
# )
# def test_sort(value, descending, output):
#     assert strx.str_sort(string=value, descending=descending) == output


# @pytest.mark.parametrize(
#     "value, output",
#     [
#         ("The quick brown fox jumps over the lazy dog.", "Thequickbrownfoxjumps-overthelazydog"),
#     ],
# )
# def test_unique(value, output):
#     assert strx.str_unique(string=value) == output


@pytest.mark.parametrize(
    "value, times, output",
    [
        (
            "The quick brown fox jumps over the lazy dog.",
            3,
            "The quick brown fox jumps over the lazy dog.The quick brown fox jumps over the lazy dog.The quick brown fox jumps over the lazy dog.",  # noqa: E501
        ),
    ],
)
def test_dup(value, times, output):
    assert strx.str_dup(string=value, times=times) == output


# @pytest.mark.parametrize(
#     "value, sep, output",
#     [
#         ("The quick brown fox jumps over the lazy dog.", "-", "The-quick-brown-fox-jumps-over-the-lazy-dog"),
#     ],
# )
# def test_c(value, sep, output):
#     assert strx.str_c(string=value, sep=sep) == output
