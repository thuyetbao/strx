<div align="center">
  <a href="https://github.com/thuyetbao/strx.git">
    <img src="docs/assets/images/banner.png" alt="Package Banner" height="200" width="100%">
  </a>
</div>

<div align="center">
  <h3>StrX</h3>
  <p><b>Consistent API for string workloads</b></p>
</div>

<div align="center">
  <a href="https://github.com/thuyetbao/strx.git" target="_blank">
    <img src="https://img.shields.io/pypi/v/strx.svg?logo=pypi" alt="Package Version">
  </a>
</div>

<div align="center">
  <a href="https://www.python.org/" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/strx.svg?logo=python" alt="Supported Python Version">
  </a>
  <br>
  <a href="https://pre-commit.com/" target="_blank">
    <img src="https://img.shields.io/badge/pre--commit-enabled-teal?logo=pre-commit" alt="pre-commit enabled">
  </a>
  <a href="https://pre-commit.com/" target="_blank">
    <img src="https://img.shields.io/badge/pep8-enabled-teal?logo=python" alt="PEP8 enabled">
  </a>
  <a href="https://github.com/features/actions" target="_blank">
    <img src="https://img.shields.io/badge/cicd-github--action-teal?logo=github-actions" alt="Github Action">
  </a>
  <br>
  <a href="https://codecov.io/gh/thuyetbao/strx" >
    <img src="https://codecov.io/gh/thuyetbao/strx/graph/badge.svg?token=M8KZX4XFSZ" alt="Codecov Coverage">
  </a>
</div>

---

### **strx** features

- Consistent API: All functions start with `str_*` prefix and take a `string` as the first argument

- Strict type checking: All functions use precise type hints to ensure safety and early error detection.

<!-- - Comprehensive test suite with 100% coverage and zero errors -->

### **Installation**

Install package from PyPI distribution [`strx`](https://pypi.org/project/strx/)

```bash
pip install strx
```

### **Usage**

Import into the script

```py
import strx
```

For general string manipulation

```py
strx.str_snakecase
strx.str_reverse
strx.str_pad
strx.str_length
strx.str_sub
strx.str_trim
strx.str_count
strx.str_sort
strx.str_unique
strx.str_dup
```

For string pattern matching

```py
strx.str_detect
strx.str_remove
strx.str_replace
strx.str_replace_all
strx.str_split
strx.str_which
strx.str_extract
strx.str_extract_all
```

Join strings

```py
strx.str_concat("strx", "is", "awesome", sep=" ")
"strx is awesome"
```

Convert string to different cases, such as upper, lower, title

```py
strx.str_to_upper("strx")
"STRX"
strx.str_to_lower("STRX")
"strx"
strx.str_to_title("strx")
"Strx"
```

Convert string into numeric (float, int) and ratio

```py
strx.str_to_number("1,000,000.00", radix=".", delimiter=",")
1000000.0

strx.str_to_number("1.000.000,00", radix=",", delimiter=".")
1000000.0

strx.str_to_number("1_000_000,00", radix=",", delimiter="_")
1000000.0

strx.str_to_ratio("350:100")
3.5
```

**Documentation**:

Documentation document at folder [docs/](/docs/)

**Code Storage**:

Repository: [GitHub > Repository:`strx`](https://github.com/thuyetbao/strx)

**Releases**:

Releases: [GitHub > Repository:`strx` > Releases](https://github.com/thuyetbao/strx/releases)
