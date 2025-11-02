#!/bin/python3

# Global
import re
import logging
from typing import Union


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
    >>> str_to_number("1,000,000.00", decimal_seperator=".", thousand_seperator=",")
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


def str_to_ratio(x: Union[str, list[Union[str, int]], tuple, None] = None) -> float | None:
    """Parse string into ratio rate

    Arguments
        x (str, list[Union[str, int]]): str, list need to parse into ratio

    Return
        float: ratio parsed, happy case.
        None when error when try to cast, or calculation.
        E.g: Zero Divided, number of elements of list can't parse (greater than 2)

    Usage
    >>> str_to_ratio("350:100")
    >>> str_to_ratio("1,000:276")
    >>> str_to_ratio([1, 2])
    >>> str_to_ratio(['1', '2'])
    >>> str_to_ratio(('1', '2'))

    # Special cases
    >>> str_to_ratio(('3 ', ' 1'))
    >>> str_to_ratio(('10,000 ', ' 200 '))
    """
    if x is None:
        return None

    _x: Union[list[str], list[Union[str, int]], tuple] = x.split(":") if isinstance(x, str) else x
    if len(_x) != 2:
        logging.exception(
            f"Can not parse ratio from string components, need 2 elements but exist {len(_x)} elements: [{','.join([_x] if isinstance(_x, str) else [str(e) for e in _x])}]"
        )
        return None

    # Excluded spaces
    _x = [i.strip() if isinstance(i, str) else i for i in _x]

    try:
        x0 = str_to_number(_x[0], decimal_seperator=".", thousand_seperator=",") if isinstance(_x[0], str) else _x[0]
        x1 = str_to_number(_x[1], decimal_seperator=".", thousand_seperator=",") if isinstance(_x[1], str) else _x[1]
        res = x0 / x1
    except Exception:
        logging.exception(f"Error when cast ratio of [{_x[0]}, {_x[1]}]")
        return None

    return res
