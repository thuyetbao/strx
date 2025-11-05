#!/bin/python3

# Global
import re
import unicodedata
from typing import Literal


# Unicode General Punctuation: https://en.wikipedia.org/wiki/General_Punctuation
_UNICODE_GENERAL_PUNCTUATION = {
    ord("‘"): ord("'"),
    ord("’"): ord("'"),
    ord("–"): ord("-"),
    ord("—"): ord("-"),
    ord(" "): ord(" "),
    ord("“"): ord('"'),
    ord("”"): ord('"'),
}


def str_normalize(string: str, form: Literal["NFC", "NFD", "NFKC", "NFKD"] = "NFKC") -> str:
    """Normalize string

    Methodology
    -----------
    List of apply element:
    1) Normalize with form format
    2) Translate string with table of punctuation. See: _UNICODE_GENERAL_PUNCTUATION
    3) Remove multiple component into single component, which:
        - colon (:)
        - comma (,)
        - space ( )
    5) Strip both for context

    Usage
    -----
    >>> str_normalize("The quick brown fox jumps over the lazy dog.")
    'The quick brown fox jumps over the lazy dog.'
    >>> str_normalize("“The quick brown fox jumps over the lazy dog.”")
    'The quick brown fox jumps over the lazy dog.'
    """

    if not isinstance(string, str):
        raise TypeError(f"Required value of type 'str', got {type(string).__name__!r}.")

    stmt = unicodedata.normalize(form, string)
    stmt = stmt.translate(_UNICODE_GENERAL_PUNCTUATION)
    stmt = re.sub(r"\,{2,}", ",", stmt)
    stmt = re.sub(r"\:{2,}", ":", stmt)
    stmt = re.sub(r"\s{2,}", " ", stmt)
    stmt = stmt.strip()

    return stmt
