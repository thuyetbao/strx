#!/bin/python3

# Global
from typing import Literal, Callable
from ._constant import EnumurationRadix, EnumurationDelimiter


radixPointLiteral = Literal["DOT", "COMMA", ".", ","]
delimiterLiteral = Literal["DOT", "COMMA", "THIN_SPACE", "HALF_SPACE", "FULL_SPACE", "UNDERSCORE", "APOSTROPHE", ".", ",", "", " ", " ", "_", "'"]


LOCALE_STYLES = {
    # --- English-based locales ---
    "en_US": {"radix": "DOT", "delimiter": "COMMA"},  # 1,000,000.50
    "en_GB": {"radix": "DOT", "delimiter": "COMMA"},
    "en_CA": {"radix": "DOT", "delimiter": "COMMA"},
    "en_AU": {"radix": "DOT", "delimiter": "COMMA"},
    "en_IN": {"radix": "DOT", "delimiter": "COMMA"},  # 1,00,000.00 (Indian pattern)
    # --- European locales ---
    "fr_FR": {"radix": "COMMA", "delimiter": "SPACE"},  # 1 000 000,50
    "de_DE": {"radix": "COMMA", "delimiter": "DOT"},  # 1.000.000,50
    "es_ES": {"radix": "COMMA", "delimiter": "DOT"},  # 1.000.000,50
    "it_IT": {"radix": "COMMA", "delimiter": "DOT"},
    "nl_NL": {"radix": "COMMA", "delimiter": "DOT"},
    "pt_PT": {"radix": "COMMA", "delimiter": "DOT"},
    "sv_SE": {"radix": "COMMA", "delimiter": "SPACE"},
    "no_NO": {"radix": "COMMA", "delimiter": "SPACE"},
    "da_DK": {"radix": "COMMA", "delimiter": "DOT"},
    "fi_FI": {"radix": "COMMA", "delimiter": "SPACE"},
    "pl_PL": {"radix": "COMMA", "delimiter": "SPACE"},
    "cs_CZ": {"radix": "COMMA", "delimiter": "SPACE"},
    "hu_HU": {"radix": "COMMA", "delimiter": "SPACE"},
    "tr_TR": {"radix": "COMMA", "delimiter": "DOT"},
    # --- Asian locales ---
    "vi_VN": {"radix": "COMMA", "delimiter": "DOT"},  # 1.000.000,00
    "th_TH": {"radix": "DOT", "delimiter": "COMMA"},
    "ja_JP": {"radix": "DOT", "delimiter": "COMMA"},  # 1,000,000.50
    "ko_KR": {"radix": "DOT", "delimiter": "COMMA"},
    "zh_CN": {"radix": "DOT", "delimiter": "COMMA"},
    "zh_TW": {"radix": "DOT", "delimiter": "COMMA"},
    "id_ID": {"radix": "COMMA", "delimiter": "DOT"},  # 1.000.000,50
    # --- Middle Eastern / Arabic locales ---
    "fa_IR": {"radix": "COMMA", "delimiter": "DOT"},
    "he_IL": {"radix": "DOT", "delimiter": "COMMA"},
    # --- Latin American locales ---
    "es_MX": {"radix": "DOT", "delimiter": "COMMA"},
    "es_AR": {"radix": "COMMA", "delimiter": "DOT"},
    "pt_BR": {"radix": "COMMA", "delimiter": "DOT"},
    # --- African locales ---
    "en_ZA": {"radix": "DOT", "delimiter": "SPACE"},  # 1 000 000.50
    "fr_SN": {"radix": "COMMA", "delimiter": "SPACE"},
}


def str_to_upper(string: str) -> str:
    return string.upper()


def str_to_lower(string: str) -> str:
    return string.lower()


def str_to_number(
    string: str,
    radix: radixPointLiteral = "DOT",
    delimiter: Literal["auto"] | delimiterLiteral = "auto",
) -> float:
    """Convert string to number

    Args
    ----
    string (str): The string like the number try to convert
    radix (str, optional): Radix point that seperated the decimal part and fractional part. Default to dot (.).
    delimiter (str): Delimiter that seperated the whole number part. Default to "auto".

    Return
    ------
    float: The parsing number based on the string

    Usage
    -----

    Basic usage
    >>> str_to_number("1,000,000.00", radix="DOT")
    1000000.0
    >>> str_to_number("1_000_000.00", radix="DOT", delimiter="_")
    1000000.0
    >>> str_to_number("1_000_000.00", radix="DOT", delimiter="_")
    1000000.0

    For some default resolved locales. The registry default is supplied to easy use for various common countries.
    Supported values can be found on `list(LOCALE_STYLES)`

    >>> str_to_number("1.000.000,00", **LOCALE_STYLES["en_US"])
    1000000.0
    >>> str_to_number("1,000,000.00", **LOCALE_STYLES["vi_VN"])
    1000000.0
    """
    if not isinstance(string, str):
        raise TypeError(f"Required value of type 'str', got {type(string).__name__!r}.")

    on_radix = EnumurationRadix.search(keyword=radix)
    on_delimiter = EnumurationDelimiter.search(on_radix.delimiter if delimiter == "auto" else delimiter)

    if on_radix.point == delimiter:
        raise ValueError(f"The radix point cannot be the same as the delimiterGot radix={on_radix.name} ({on_radix.point}), delimiter={delimiter} ({on_delimiter.symbol})")

    value = string.strip().replace(on_delimiter.symbol, "").replace(on_radix.point, ".")
    return float(value)


def str_to_ratio(string: str, sep_by: str = ":", convert_func: Callable[..., float] = str_to_number) -> float:
    """Convert string to ratio

    Args
    ----
    string (str): String to convert
    sep_by (str, optional): Separator between numerator and denominator. Defaults to ":".
    convert_func (Callable, optional): Function to convert parts to float. Defaults to `str_to_number`.


    Return
    ------
    float: The parsed ratio

    Raises
    ------
    TypeError: If input is not a string.
    ValueError: If format is invalid or parts cannot be converted.
    ZeroDivisionError: If denominator is zero.

    Usage
    -----

    Default usage
    >>> str_to_ratio("350:100")
    3.5
    >>> str_to_ratio("1,000:276")
    3.6231884057971016

    With different separator
    >>> str_to_ratio("345.0/44", sep_by="/")
    7.75

    With different convert function
    >>> str_to_ratio("44:100", convert_func=float)
    3.5

    Fail to denominator is zero
    >>> str_to_ratio("350:0")
    Traceback (most recent call last):
      ...
    ZeroDivisionError: Cannot divide by zero in ratio '350:0'.
    """
    if not isinstance(string, str):
        raise TypeError(f"Required value of type 'str', got {type(string).__name__!r}.")

    parts = string.split(sep_by)
    if len(parts) != 2:
        raise ValueError(f"Invalid ratio format: expected exactly 2 parts separated by {sep_by!r}, but found {len(parts)} in {string!r}.")

    try:
        numerator, denominator = (convert_func(p.strip()) for p in parts)
    except Exception as exc:
        raise ValueError(f"Failed to convert ratio parts using {convert_func.__name__}: {exc}") from exc

    if denominator == 0:
        raise ZeroDivisionError(f"Cannot divide by zero in ratio {string!r}.")

    return numerator / denominator
