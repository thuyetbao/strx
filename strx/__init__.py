#!/bin/python3

from .method import (
    str_length,
    str_sub,
    str_to_upper,
    str_to_lower,
    str_trim,
    str_reverse,
    str_detect,
    str_snakcase,
    str_remove,
    str_replace,
    str_replace_all,
    str_pad,
    str_split,
    str_count,
    str_which,
    str_sort,
    str_unique,
    str_dup,
    str_c,
    str_extract,
    str_extract_all,
)

from .convert import (
    str_to_number,
    str_to_ratio,
)

from .normalize import (
    str_normalize,
)

from .compose import (
    str_md5_surrogate_key,
)

__all__ = [
    "str_length",
    "str_sub",
    "str_to_upper",
    "str_to_lower",
    "str_trim",
    "str_reverse",
    "str_detect",
    "str_snakcase",
    "str_remove",
    "str_replace",
    "str_replace_all",
    "str_pad",
    "str_split",
    "str_count",
    "str_which",
    "str_sort",
    "str_unique",
    "str_dup",
    "str_c",
    "str_extract",
    "str_extract_all",
    "str_to_number",
    "str_to_ratio",
    "str_normalize",
    "str_md5_surrogate_key",
]

__version__ = "0.1.2"
