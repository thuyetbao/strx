# SAD

## **Overview**

The `strx` package is designed as a lightweight, extensible toolkit for structured string processing and transformation. It provides a unified interface for handling common string-related tasks such as normalization, conversion, parsing, and formatting, with a strong focus on reliability.

The core philosophy behind `strx` is to treat string manipulation as a predictable, type-safe operation. By combining Python’s type hints, clear error handling, and registry-based extensibility (e.g., locale-aware numeric parsing), `strx` aims to improve code clarity, reduce parsing errors, and standardize string handling across diverse use cases such as finance, localization, and data ingestion.

## **Key components**

### Function namepsace

The namespace of functions is inspried by many packages outside there like `stringr` package (in R languguage), `snakecase` package and another alternatives

The namespace try to make with very consistent API like following

```py
import strx

# Convert to transform
strx.str_to_lower
strx.str_to_upper

# Convert to numeric types
strx.str_to_number
strx.str_to_ratio
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

The `str_to_number` function converts formatted numeric strings into floating-point values.
It is designed to handle locale-specific conventions for decimal (radix) and thousand (delimiter) separators in a consistent and extensible manner.

Different locales and formatting styles use varying symbols to separate decimal and digit groups.
To correctly interpret these formats, the function must explicitly identify:

- **Radix point (`radix`)** — the symbol that separates the integer and fractional parts of a number. Common examples include `"."` (dot) or `","` (comma).

  Example:

  ```txt
  1000000000.00
          ↑
          Radix point separating integer and fractional parts
  ```

- **Delimiter (`delimiter`)** — the symbol used to group digits within the integer part for readability (e.g., thousands, millions).
  Typical delimiters include `","`, `"."`, `" "`, `" "`, `"_"`, or `"’"`. For example: `1,000,000` or `21_450`.

Earlier implementations used parameters named `decimal_separator` and `thousand_separator`.
While functional, this approach was error-prone and difficult to maintain, as developers often confused which symbol applied to which part.

Example of ambiguity:

```python
import strx

strx.str_to_number("1,000,000.00", decimal_separator=".", thousand_separator=",")   # ✅ Works
strx.str_to_number("1,000,000.00", decimal_separator=".", thousand_separator=".")   # ❌ Fails – ambiguous usage
```

Such naming made the logic harder to debug and the cause of conversion failures less transparent.

To simplify configuration and reduce human error, `strx` introduces a clearer terminology and stricter validation system:

- Replace `decimal_separator` and `thousand_separator` with standardized parameters:

  - `radix` → defines the decimal separator (radix point).
  - `delimiter` → defines the digit grouping separator.

The function validates that both symbols are distinct to prevent incorrect parsing.

Example:

```python
strx.str_to_number("1,000,000.00", radix="DOT", delimiter="COMMA")
```

If the `radix` and `delimiter` conflict, the function raises a descriptive `ValueError`, explicitly indicating the cause.

Based on differents countries conventions, the `radix` and `delimiter` can be:

![Wikipedia – World conventions on decimal separators](assets/images/wikipedia-world-conventions-on-decimal-seperators.png)

The `strx` package provides a global constant, `LOCALE_STYLES`, to support various locales. This constant is a dictionary that maps a locale string to its corresponding radix and delimiter. For example, `LOCALE_STYLES["en_US"]` would return a dictionary with the radix set to `"."` and the delimiter set to `","`.

**Reference**:

<https://en.wikipedia.org/w/index.php?title=Decimal_separator&useskin=monobook#Digit_grouping>

<https://docs.oracle.com/cd/E19455-01/806-0169/overview-9/index.html>

<https://en.wikipedia.org/wiki/Decimal_separator#:~:text=Radix%20point,-In%20mathematics%20and&text=In%20English%2Dspeaking%20countries%2C%20the,%2C)%20placed%20on%20the%20baseline.>
