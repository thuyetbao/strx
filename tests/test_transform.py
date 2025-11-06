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
    "value, start, end, output",
    [
        ("The quick brown fox jumps over the lazy dog.", 0, 3, "The"),
        ("The quick brown fox jumps over the lazy dog.", None, None, "The quick brown fox jumps over the lazy dog."),
        ("The quick brown fox jumps over the lazy dog.", 10, -29, "brown"),
    ],
)
def test_sub(value, start, end, output):
    assert strx.str_sub(string=value, start=start, end=end) == output


@pytest.mark.parametrize(
    "value, output",
    [
        ("", ""),
        ("element", "tnemele"),
        ("Hello, World!", "!dlroW ,olleH"),
    ],
)
def test_reverse(value, output):
    assert strx.str_reverse(string=value) == output


@pytest.mark.parametrize(
    "value, pattern, output",
    [
        ("Hello, World!", "o", "Hell, World!"),
        ("Hello, World!", "!", "Hello, World"),
        ("Hello, World!", "z", "Hello, World!"),
        ("", "a", ""),
        ("abcde", "bc", "ade"),
        ("abcde", "cd", "abe"),
        ("abcde", "ef", "abcde"),
        ("abcde", "g", "abcde"),
        ("12345", "2", "1345"),
        ("12345", "4", "1235"),
        ("12345", "6", "12345"),
        ("12345", "7", "12345"),
        ("12345", "8", "12345"),
        ("12345", "9", "12345"),
    ],
)
def test_remove(value, pattern, output):
    assert strx.str_remove(string=value, pattern=pattern) == output


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


@pytest.mark.parametrize(
    "value, width, side, pad, output",
    [
        ("abc", 10, "right", " ", "abc       "),
        ("abc", 10, "left", " ", "       abc"),
        ("abc", 10, "both", " ", "   abc    "),
        ("abc", 2, "right", " ", "abc"),
        ("abc", 2, "left", " ", "abc"),
        ("abc", 2, "both", " ", "abc"),
        ("12345", 6, "right", "0", "123450"),
        ("12345", 6, "left", "0", "012345"),
        ("12345", 6, "both", "0", "123450"),
        ("12345", 2, "right", "z", "12345"),
        ("12345", 2, "left", "z", "12345"),
        ("12345", 2, "both", "z", "12345"),
    ],
)
def test_pad(value, width, side, pad, output):
    assert strx.str_pad(string=value, width=width, side=side, pad=pad) == output


@pytest.mark.parametrize(
    "value, pattern, output",
    [
        ("The quick brown fox jumps over the lazy dog.", "fox", 1),
    ],
)
def test_count(value, pattern, output):
    assert strx.str_count(string=value, pattern=pattern) == output


@pytest.mark.parametrize(
    "value, pattern, output",
    [
        ("The quick brown fox jumps over the lazy dog.", " ", 3),
    ],
)
def test_which(value, pattern, output):
    assert strx.str_which(string=value, pattern=pattern) == output


@pytest.mark.parametrize(
    "value, descending, output",
    [
        ("0123456", False, "0123456"),
        ("0123456", True, "6543210"),
    ],
)
def test_sort(value, descending, output):
    assert strx.str_sort(string=value, descending=descending) == output


@pytest.mark.parametrize(
    "value, output",
    [
        ("kkkiw", "kiw"),
        ("0000123456789", "0123456789"),
    ],
)
def test_unique(value, output):
    assert strx.str_unique(string=value) == output


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


@pytest.mark.parametrize(
    "value, sep, output",
    [
        (
            ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."],
            " ",
            "The quick brown fox jumps over the lazy dog.",
        )
    ],
)
def test_concat(value, sep, output):
    assert strx.str_concat(*value, sep=sep) == output


def testfailure_not_is_interable_string_in_concat():
    with pytest.raises(ValueError):
        strx.str_concat([1, "value_is_string", 8], sep=" ")


@pytest.mark.parametrize(
    "value, pattern, replacement, output",
    [
        ("The quick brown fox jumps over the lazy dog.", "fox", "cat", "The quick brown cat jumps over the lazy dog."),
        ("The quick brown fox jumps over the lazy dog.", "dog", "cat", "The quick brown fox jumps over the lazy cat."),
        ("The quick brown fox jumps over the lazy dog.", "cat", "dog", "The quick brown fox jumps over the lazy dog."),
        ("", "fox", "cat", ""),
        ("abcde", "bc", "xy", "axyde"),
        ("abcde", "cd", "xy", "abxye"),
        ("12345", "2", "x", "1x345"),
        ("12345", "4", "x", "123x5"),
    ],
)
def test_replace(value, pattern, replacement, output):
    assert strx.str_replace(string=value, pattern=pattern, replacement=replacement) == output


@pytest.mark.parametrize(
    "value, pattern, replacement, output",
    [
        ("The quick brown fox jumps over the lazy dog.", "fox", "cat", "The quick brown cat jumps over the lazy dog."),
        ("The quick brown fox jumps over the lazy dog.", "dog", "cat", "The quick brown fox jumps over the lazy cat."),
        ("The quick brown fox jumps over the lazy dog.", "cat", "dog", "The quick brown fox jumps over the lazy dog."),
        ("", "fox", "cat", ""),
        ("abcde", "bc", "xy", "axyde"),
        ("abcde", "cd", "xy", "abxye"),
        ("12345", "2", "x", "1x345"),
        ("12345", "4", "x", "123x5"),
    ],
)
def test_replace_all(value, pattern, replacement, output):
    assert strx.str_replace_all(string=value, pattern=pattern, replacement=replacement) == output


@pytest.mark.parametrize(
    "value, pattern, output",
    [
        ("The quick brown fox jumps over the lazy dog.", "fox", "fox"),
        ("The quick brown fox jumps over the lazy dog.", "dog", "dog"),
        ("The quick brown fox jumps over the lazy dog.", "cat", None),
        ("", "fox", None),
        ("abcde", "bc", "bc"),
        ("12345", "2", "2"),
        ("12345", "4", "4"),
    ],
)
def test_extract(value, pattern, output):
    assert strx.str_extract(string=value, pattern=pattern) == output


@pytest.mark.parametrize(
    "value, pattern, output",
    [
        ("The quick brown fox jumps over the lazy dog.", "fox", ["fox"]),
        ("The quick brown fox jumps over the lazy dog.", "dog", ["dog"]),
        ("The quick brown fox jumps over the lazy dog.", "cat", []),
        ("", "fox", []),
        ("abcde", "bc", ["bc"]),
        ("12345", "2", ["2"]),
        ("12345", "4", ["4"]),
    ],
)
def test_extract_all(value, pattern, output):
    assert strx.str_extract_all(string=value, pattern=pattern) == output
