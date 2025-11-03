#!/bin/python3

# Global
from typing import Literal
from _constant import RadixPoint


radixNameLiteral = Literal["DECIMAL", "COMMA", "THIN_SPACE", "SPACE", "UNDERSCORE", "APOSTROPHE", "HALF_SPACE", "FULL_SPACE"]
radixSymbolLiteral = Literal[".", ",", " ", " ", "_", "'", ":", ":", "/"]


def str_to_upper(string: str) -> str:
    return string.upper()


def str_to_lower(string: str) -> str:
    return string.lower()


def str_to_number(string: str, radix: radixNameLiteral | radixSymbolLiteral = "DECIMAL") -> float:
    """String to number

    Args
    ----
    string (str): The string like the number try to convert
    decimal_seperator (str, optional): Seperator for decimal part. Default to ",".
    thousand_seperator (str, optional): Seperator for whole number part. Default to ".".

    Return
    ------
    float: The parsing number based on the string

    Usage
    -----
    >>> import strx
    >>> strx.str_to_number("1,000,000.00", radix="DECIMAL")
    1000000.0
    """
    on_radix = RadixPoint.search(keyword=radix)
    value = string.replace(on_radix.decimal_point, ".").replace(on_radix.thousand_point, "")
    return float(value)


def str_to_ratio(string: str, sep_by: str = ":") -> float:
    """Parse string into ratio rate

    Args
    ----
    string (str): string to convert

    Return
    ------
    Return the parsed ratio as a float if successful, otherwise None if there is an error when trying to cast or calculate,
        such as ZeroDivisionError or if the number of elements in the list can't be parsed (greater than 2).

    Usage
    -----
    >>> import strx
    >>> strx.str_to_ratio("350:100")
    3.5
    >>> strx.str_to_ratio("1,000:276")
    3.6231884057971016
    """

    comp = string.split(sep_by)
    if len(comp) != 2:
        raise ValueError(f"Can not parse ratio from string components, need 2 elements but exist {len(comp)} elements: [{string}]")

    # Excluded spaces
    comp = [ele.strip() if isinstance(ele, str) else ele for ele in comp]

    try:
        x0 = str_to_number(comp[0], radix="DECIMAL") if isinstance(comp[0], str) else comp[0]
        x1 = str_to_number(comp[1], radix="DECIMAL") if isinstance(comp[1], str) else comp[1]
        ressult = x0 / x1
    except Exception:
        raise ValueError(f"Error when cast ratio of [{comp[0]}, {comp[1]}]")
    else:
        return ressult
