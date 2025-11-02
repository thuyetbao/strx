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

Here's a list of common first argument names used in string manipulation functions across popular R packages like **stringr**, **stringi**, **base R**, and others. These names typically refer to the input text or character vector:

Common the `string` argument names in Python String Functions

| Argument Name                         | Description                                             | Common In                                                    |
| ------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------ |
| `s`                                   | Short for "string"                                      | Used in textbooks, tutorials, and simple functions           |
| `text`                                | Semantic clarity for textual input                      | Common in NLP libraries like `spaCy`, `nltk`, `transformers` |
| `string`                              | Explicit and descriptive                                | Seen in custom utilities and some standard functions         |
| `input`                               | Generic input name                                      | Used in pipelines or abstract functions                      |
| `value`                               | Used when the string is part of a larger data structure | Pandas, data validation libraries                            |
| `sentence` / `paragraph` / `document` | Context-specific                                        | NLP and document processing libraries                        |
| `string`                              | A single string or vector of strings                    | `stringr`, `stringi`                                         |
| `strings`                             | Plural form, sometimes used for multiple inputs         | Less common                                                  |
| `text`                                | Generic label for textual input                         | Some custom or NLP packages                                  |
| `texts`                               | Plural form, used in corpus or NLP contexts             | `quanteda`, `tm`                                             |
| `x`                                   | Generic input, often used in base R functions           | `base R`, `gsub`, `grep`                                     |
| `input`                               | Used in more abstract or pipeline functions             | Custom or tidyverse-style                                    |

Some use `string` or `stringr` to represented single or arrray of string

### **Signature Comparison**

| Signature | Pros                            | Cons                                  |
| --------- | ------------------------------- | ------------------------------------- |
| `string`  | Easy to understand              | Not support array or single string    |
| `strings` | Support array of strings        | Not support single string             |
| `stringr` | Support array and single string | Not support legacy string type (`txt` |
| `text`    | Easy to understand              | Not support array or single string    |
| `texts`   | Support array of strings        | Not support single string             |
| `txt`     | Legacy type                     | Not support array or single string    |

## **Function Design**

### For `str_to_number` function

#### For decimenal

https://en.wikipedia.org/w/index.php?title=Decimal_separator&useskin=monobook#Digit_grouping

https://docs.oracle.com/cd/E19455-01/806-0169/overview-9/index.html

Radix point
In mathematics and computing, a radix point or radix character is a symbol used in the display of numbers to separate the integer part of the value from its fractional part. In English and many other languages (including many that are written right-to-left), the integer part is at the left of the radix point, and the fraction part at the right of it.[25]

A radix point is most often used in decimal (base 10) notation, when it is more commonly called the decimal point (with deci- indicating base 10). In English-speaking countries, the decimal point is usually a small dot (.) placed either on the baseline, or halfway between the baseline and the top of the digits (·)[26][a] In many other countries, the radix point is a comma (,) placed on the baseline.[26][a]

These conventions are generally used both in machine displays (printing, computer monitors) and in handwriting. It is important to know which notation is being used when working in different software programs. The respective ISO 31-0 standard defines both the comma and the small dot as decimal markers, but does not explicitly define universal radix marks for bases other than 10.

Fractional numbers are rarely displayed in other number bases, but, when they are, a radix character may be used for the same purpose. When used with the binary (base 2) representation, it may be called "binary point".

For ease of reading, numbers with many digits (e.g. numbers over 999) may be divided into groups using a delimiter,[30] such as comma (,), dot (.), half-space or thin space (" "), space (" "), underscore (\_; as in maritime "21_450"),[citation needed] or apostrophe ('). In some countries, these "digit group separators" are only employed to the left of the decimal separator; in others, they are also used to separate numbers with a long fractional part. An important reason for grouping is that it allows rapid judgement of the number of digits, via telling at a glance ("subitizing") rather than counting (contrast, for example, 100 000 000 with 100000000 for one hundred million).

https://en.wikipedia.org/wiki/Decimal_separator#:~:text=Radix%20point,-In%20mathematics%20and&text=In%20English%2Dspeaking%20countries%2C%20the,%2C)%20placed%20on%20the%20baseline.

Propose:

```
strx.str_to_number(string="1,000,000,000", radix=point.DECIMAL)
```
