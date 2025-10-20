#!/bin/python3

# Global
import re
import unicodedata


def str_normalize(string: str) -> str:
    elem = unicodedata.normalize("NFKC", string.strip())
    elem = re.sub(r"\s{2,}", " ", elem)
    elem = elem.replace("“", '"')
    elem = elem.replace("”", '"')
    return elem
