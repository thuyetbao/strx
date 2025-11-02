#!/bin/python3

# Global
import re
from typing import Union
import string as lib_string


def str_length(string: str) -> int:
    return len(string)


def str_sub(string: str, start: int, end: Union[int, None] = None) -> str:
    return string[start:end]


def str_trim(string: str) -> str:
    return string.strip()


def str_reverse(string: str) -> str:
    """Reversed any string

    Args
    ----
    string (str): The string to reverse

    Return
    ------
    (str): Reversed string

    Usage
    -----
    >>> str_reverse("element")
    "tnemele"
    """
    return string[::-1]


def str_detect(string: str, pattern: str) -> bool:
    return bool(re.search(pattern, string))


def str_snakcase(string: str) -> str:
    """Snake case component

    Args
    ----
    string (str): The target string to applied method

    Return
    ------
    str: the string after baking.
    """
    string = re.sub(r"\s{1,}", "_", string)
    string = string.lower()
    while string[-1] in lib_string.punctuation:
        string = string[:-1]

    return string


def str_remove(string: str, pattern: str) -> str:
    return re.sub(pattern, "", string, count=1)


def str_replace(string: str, pattern: str, replacement: str) -> str:
    return re.sub(pattern, replacement, string, count=1)


def str_replace_all(string: str, pattern: str, replacement: str) -> str:
    return re.sub(pattern, replacement, string)


def str_pad(string: str, width: int, side: str = "right", pad: str = " ") -> str:
    padded = []
    if len(string) >= width:
        padded.append(string)
    else:
        pad_len = width - len(string)
        if side == "left":
            padded.append(pad * pad_len + string)
        elif side == "right":
            padded.append(string + pad * pad_len)
        elif side == "both":
            left = pad_len // 2
            right = pad_len - left
            padded.append(pad * left + string + pad * right)
    return padded[0]


def str_split(string: str, delimiter: str) -> list[str]:
    return string.split(delimiter)


def str_count(string: str, pattern: str) -> int:
    return len(re.findall(pattern, string))


def str_which(string: str, pattern: str) -> int:
    return next((i for i, s in enumerate(string) if re.search(pattern, s)), None)


def str_sort(string: str, descending: bool = False) -> str:
    return "".join(sorted(string, reverse=descending))


def str_unique(string: str) -> str:
    return "".join(dict.fromkeys(string))


def str_dup(string: str, times: int) -> str:
    return string * times


def str_c(string: str, sep: str = "") -> str:
    return sep.join(string)


def str_extract(string: str, pattern: str) -> Union[str, None]:
    match = re.search(pattern, string)
    return match.group(0) if match else None


def str_extract_all(string: str, pattern: str) -> list[str]:
    return re.findall(pattern, string)
