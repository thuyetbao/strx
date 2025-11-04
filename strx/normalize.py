#!/bin/python3

# Global
import re
import unicodedata


def str_normalize(string: str) -> str:
    if not isinstance(string, str):
        raise TypeError(f"Required value of type 'str', got {type(string).__name__!r}.")

    elem = unicodedata.normalize("NFKC", string.strip())
    elem = re.sub(r"\s{2,}", " ", elem)
    elem = elem.replace("“", '"')
    elem = elem.replace("”", '"')
    return elem
