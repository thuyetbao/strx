# SAD

## **Overview**

`strx` is the package to support various tasks when working with strings.

## **Key components**

### Function namepsace

The namespace of functions is inspried by many packages outside there like `stringr` package (in R languguage), `snakecase` package and another alternatives

The namespace try to make with very consistent API like following

```py
import strx
strx.str_lower()
strx.str_upper()

# Convert to another types
strx.str_to_number()
strx.str_to_ratio()
```

### Agrument namepsace

The argument is the second design component to consider.

The first arguments should be:

- The represented of the processing string, text. It's can be in vector (Sequence, dict) types and maybe null.

- The pros/cons related to the type supporse to support: native `str` type and sequence type (list, set)

- Preferred the singular form without `s` or `es` that should be the same as the function name.

Here's a list of common first argument names used in string manipulation functions across popular R packages like **stringr**, **stringi**, **base R**, and others.
These names typically refer to the input text or character vector:

Common the `string` argument names in Python string functions

| Argument Name                         | Description                                                     | Common In                                                    |
| ------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------ |
| `s`                                   | Short for "string"                                              | Used in textbooks, tutorials, and simple functions           |
| `x`                                   | Generic input, often used in base R functions                   | `base R`, `gsub`, `grep`                                     |
| `text`                                | Semantic clarity for textual input                              | Common in NLP libraries like `spaCy`, `nltk`, `transformers` |
| `texts`                               | Plural form, used in corpus or NLP contexts                     | `quanteda`, `tm`                                             |
| `string`                              | Explicit and descriptive. A single string or vector of strings  | Seen in custom utilities and some standard functions         |
| `strings`                             | Plural form, sometimes used for multiple inputs                 | Less common, Custom or tidyverse-style                       |
| `input`                               | Generic input name, Used in more abstract or pipeline functions | Used in pipelines or abstract functions                      |
| `value`                               | Used when the string is part of a larger data structure         | Pandas, data validation libraries                            |
| `sentence` / `paragraph` / `document` | Context-specific                                                | NLP and document processing libraries                        |

## **Function Design**

### `str_to_number` function

At the beginning, the function is to convert string to number that consider 2 following cases, and seperated by the decimal and thousand seperator

- Decimal number: "." then thousand number: ","

- Decimal number: "," then thousand number: "."

But when in usage, the function is hard to remember which one is the decimal and which one is the thousand seperator and hard to debug when look through the codebase.

This lead to the error prones that hit when looking into the errors and try to captures by using languages like regex or others.

For examples,

```py
import strx
strx.str_to_number("1,000,000.00", decimal_seperator=".", thousand_seperator=",")
strx.str_to_number("1,000,000.00", decimal_seperator=".", thousand_seperator=".")       # <--- Failure case, raise ValueError but hard to see the cause
```

And based on this, we can see if we know decimal_seperator, we can get the correct thousand_seperator
So that, we change to the radix point

#### Decimenal

Radix point

In mathematics and computing, a radix point or radix character is a symbol used in the display of numbers to separate the integer part of the value from its fractional part. In English and many other languages (including many that are written right-to-left), the integer part is at the left of the radix point, and the fraction part at the right of it.

A radix point is most often used in decimal (base 10) notation, when it is more commonly called the decimal point (with deci- indicating base 10). In English-speaking countries, the decimal point is usually a small dot (.) placed either on the baseline, or halfway between the baseline and the top of the digits (·) In many other countries, the radix point is a comma (,) placed on the baseline.

These conventions are generally used both in machine displays (printing, computer monitors) and in handwriting. It is important to know which notation is being used when working in different software programs. The respective ISO 31-0 standard defines both the comma and the small dot as decimal markers, but does not explicitly define universal radix marks for bases other than 10.

Fractional numbers are rarely displayed in other number bases, but, when they are, a radix character may be used for the same purpose. When used with the binary (base 2) representation, it may be called "binary point".

For ease of reading, numbers with many digits (e.g. numbers over 999) may be divided into groups using a delimiter,[30] such as comma (,), dot (.), half-space or thin space (" "), space (" "), underscore (\_; as in maritime "21_450"),[citation needed] or apostrophe ('). In some countries, these "digit group separators" are only employed to the left of the decimal separator; in others, they are also used to separate numbers with a long fractional part. An important reason for grouping is that it allows rapid judgement of the number of digits, via telling at a glance ("subitizing") rather than counting (contrast, for example, 100 000 000 with 100000000 for one hundred million).

**Reference**:

<https://en.wikipedia.org/w/index.php?title=Decimal_separator&useskin=monobook#Digit_grouping>

<https://docs.oracle.com/cd/E19455-01/806-0169/overview-9/index.html>

<https://en.wikipedia.org/wiki/Decimal_separator#:~:text=Radix%20point,-In%20mathematics%20and&text=In%20English%2Dspeaking%20countries%2C%20the,%2C)%20placed%20on%20the%20baseline.>

Propose:

```py
strx.str_to_number(string="1,000,000,000", radix=point.DECIMAL)
```

```
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
```
