# SAD

## **Overview**

//

## Topics

### The centralized agrument name

The first arguments should be

### 🐍 Common First Argument Names in Python String Functions

| Argument Name                         | Description                                             | Common In                                                    |
| ------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------ |
| `s`                                   | Short for "string"                                      | Used in textbooks, tutorials, and simple functions           |
| `text`                                | Semantic clarity for textual input                      | Common in NLP libraries like `spaCy`, `nltk`, `transformers` |
| `string`                              | Explicit and descriptive                                | Seen in custom utilities and some standard functions         |
| `input`                               | Generic input name                                      | Used in pipelines or abstract functions                      |
| `value`                               | Used when the string is part of a larger data structure | Pandas, data validation libraries                            |
| `sentence` / `paragraph` / `document` | Context-specific                                        | NLP and document processing libraries                        |

- **Package conflicts** can arise when two packages define `str_*` functions with different argument names or expectations.
- For example, `stringr::str_detect(string, pattern)` expects `string` as the first argument, while other packages might use `x` or `text`.

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

Here's a list of common first argument names used in string manipulation functions across popular R packages like **stringr**, **stringi**, **base R**, and others. These names typically refer to the input text or character vector:

### 🧵 Common First Argument Names in `str_*` and Related Functions

| Argument Name | Description                                     | Common In                                            |
| ------------- | ----------------------------------------------- | ---------------------------------------------------- |
| `string`      | A single string or vector of strings            | `stringr`, `stringi`                                 |
| `strings`     | Plural form, sometimes used for multiple inputs | Less common                                          |
| `text`        | Generic label for textual input                 | Some custom or NLP packages                          |
| `texts`       | Plural form, used in corpus or NLP contexts     | `quanteda`, `tm`                                     |
| `x`           | Generic input, often used in base R functions   | `base R`, `gsub`, `grep`                             |
| `input`       | Used in more abstract or pipeline functions     | Custom or tidyverse-style                            |
| `pattern`     | Sometimes used as first argument in base R      | `grep`, `grepl`, `sub`, `gsub` (though often second) |
