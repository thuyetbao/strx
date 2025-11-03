#!/bin/python3

# Global
import re


def str_to_upper(string: str) -> str:
    return string.upper()


def str_to_lower(string: str) -> str:
    return string.lower()


def str_to_number(string: str, decimal_seperator: str = ".", thousand_seperator: str = ",") -> float:
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
    >>> strx.str_to_number("1,000,000.00", decimal_seperator=".", thousand_seperator=",")
    """

    # Valid
    if decimal_seperator == thousand_seperator:
        raise ValueError(f"Seperator of decimal and thousand need to be differentGot decimal_seperator=thousand_seperator={decimal_seperator}")

    # Seperate
    _sep = re.split(r"\{ds}".format(ds=decimal_seperator), string, maxsplit=1)

    # Component
    whole_str = _sep[0]
    whole_num = re.sub(r"\{ts}".format(ts=thousand_seperator), "", whole_str)
    try:
        decimal_str = decimal_num = _sep[1]
    except IndexError:
        decimal_str = decimal_num = ""

    if re.search(r"\{ds}".format(ds=decimal_seperator), decimal_str) is not None:
        raise ValueError(f"Existing multiple seperator [`{decimal_seperator}`] on string=[{string}] lead to can't convert decimal part")

    num = whole_num + "." + decimal_num

    try:
        _tmp = float(num)
    except ValueError as exc:
        raise ValueError(f"Parse to float failed related on string=`{string}` by convert element from {str(exc)}")
    else:
        return _tmp


def str_to_ratio(string: str, sep_by: str = ":") -> float | None:
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
        x0 = str_to_number(comp[0], decimal_seperator=".", thousand_seperator=",") if isinstance(comp[0], str) else comp[0]
        x1 = str_to_number(comp[1], decimal_seperator=".", thousand_seperator=",") if isinstance(comp[1], str) else comp[1]
        ressult = x0 / x1
    except Exception:
        raise ValueError(f"Error when cast ratio of [{comp[0]}, {comp[1]}]")
    else:
        return ressult
