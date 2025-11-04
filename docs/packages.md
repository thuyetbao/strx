# Packages

## **Overview**

The place to analysis/diagnose the packages with the same goals and related features

## **Comparison table**

The following tables is the list of packages related to `strx` package:

| Package    | Language | Description                                                   | Link                                   |
| ---------- | -------- | ------------------------------------------------------------- | -------------------------------------- |
| stringr    | R        | Package for string manipulation in R                          | <https://stringr.tidyverse.org/>       |
| snakecase  | R        | Fresh and straightforward approach on case conversion         | <https://github.com/Tazinho/snakecase> |
| tidystring | Python   | Easier string operations in Python, inspired by the tidyverse | <https://pypi.org/project/tidystring/> |

## **Functions workloads**

The following table is the list of functions compare to `strx` package:

| **`strx`**      | **`stringr`**   | **`tidystring`**  | **`snakecase`**             |
| --------------- | --------------- | ----------------- | --------------------------- |
| str_length      | str_length      | str_length        | —                           |
| str_sub         | str_sub         | str_sub           | —                           |
| str_trim        | str_trim        | str_trim          | —                           |
| str_reverse     | str_reverse     | —                 | —                           |
| str_detect      | str_detect      | str_detect        | —                           |
| str_snakecase   | to_snake_case   | —                 | to_snake_case / to_any_case |
| str_remove      | str_remove      | str_remove        | —                           |
| str_replace     | str_replace     | str_replace       | —                           |
| str_replace_all | str_replace_all | str_replace_all   | —                           |
| str_pad         | str_pad         | —                 | —                           |
| str_split       | str_split       | str_split         | —                           |
| str_count       | str_count       | str_count         | —                           |
| str_which       | str_which       | str_which         | —                           |
| str_sort        | str_sort        | str_sort          | —                           |
| str_unique      | str_unique      | —                 | —                           |
| str_dup         | str_dup         | str_dup           | —                           |
| str_c           | str_c           | str_concat        | —                           |
| str_extract     | str_extract     | str_extract       | —                           |
| str_extract_all | str_extract_all | str_extract_all   | —                           |
| str_to_number   | str_to_number   | —                 | —                           |
| --              | --              | str_wrap          | —                           |
| str_to_title    | --              | str_to_title      | —                           |
| str_to_upper    | toUpperCase     | str_to_upper      | —                           |
| str_to_lower    | toLowerCase     | str_to_lower      | —                           |
| --              | --              | str_locate        | —                           |
| --              | --              | str_locate_all    | —                           |
| --              | --              | str_match         | —                           |
| --              | --              | str_match_all     | —                           |
| --              | --              | str_glue          | —                           |
| --              | --              | str_order         | —                           |
| --              | --              | str_subset        | —                           |
| --              | --              | str_which         | —                           |
| --              | --              | str_squish        | —                           |
| --              | --              | str_flatten       | —                           |
| --              | --              | str_startswith    | —                           |
| --              | --              | str_endswith      | —                           |
| --              | --              | str_upper_cut     | —                           |
| --              | --              | str_search_apply  | —                           |
| --              | --              | str_dash_to_space | —                           |

## **Philosophy**

### **tidystring**

- Insprired with the `stringr` package and other related: `siuba`, `pyjanitor`

- Features can set with `pandas`, which required dependencies of `pandas` package
