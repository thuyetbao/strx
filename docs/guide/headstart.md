# Headstart

## **Overview**

The headstart for developers to develop the project.

## **Development**

### **Prerequisite**

- Python version `>=3.12.x`

- `hatch` for build package

- `make` for automate command in bash

- `gh` is a GitHub CLI program to manage release documentation

- [GitHub CLI](https://github.com/cli/cli)

- Maintainer priviledges: READ/WRITE/ADMIN to control the package

### **Development Process**

- Clone the package at [GitHub repository]

```bash
git clone https://github.com/thuyetbao/strx.git strx
```

- Create virtual environment and activate

```bash
make venv && source venv/script/active
# pre-commit installed at .git\hooks\pre-commit
```

- Install dev-mode requirement

```bash
make install
```

- Install the config of `pre-commit`

```bash
pre-commit install
# pre-commit installed at .git\hooks\pre-commit
```

- Implement logic within the `/strx/**` directory

- Write your test at `tests/**` and test locally

To test the package locally, execute the following command locally:

```bash
# Rull all
hatch run test

# Run specific test
hatch run test tests/path-to-specific-tests/test.py

# Run only last failed case
hatch run test --last-failed
```

- Create a Pull Request (PR) and write changelogs

- Once the review is complete, the PR is merged and the version is published

### **Internal Documentation**

Serve the documentation

You can serve the documentation locally with the following command:

```bash
hatch run docs
```

The documentation will be available on port 6789 at URL [http://0.0.0.0:6789](http://0.0.0.0:6789).

### **Release**

Release is intended for maintainers.

- [0] [Optional] Check version of requirement tools

```bash
gh version
# gh version 2.35.0 (2023-09-19)
# https://github.com/cli/cli/releases/tag/v2.35.0
```

- Validate implement progess. Code is good (passed ruff check) and satified tests (both unit/integrate/e2e/perforamce)

- Validate the sematic version layer. Bump for changes. Version of package is not confict or following `semver`

```bash
declare TARGETED_VERSION=x.x.x
hatch version $TARGETED_VERSION;
```

- Merge, validate, clean and updated CHANGELOG, TODO, README,...

- Using Github CLI to manage release

```bash
gh release create <TAG/>
# ? Title (optional) Release Adjustment Model
# ? Release notes Write using generated notes as template
# ? Is this a prerelease? Yes
# ? Submit? Save as draft
# https://github.com/thuyetbao/strx/releases/tag/untagged-af1c7983fa8bfa2eb6d0
```

Ref:

- [1] [Managing Releases in a repository](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository?tool=cli)
