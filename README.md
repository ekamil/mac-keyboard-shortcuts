# Mac Keyboard Shortcuts

[![PyPI](https://img.shields.io/pypi/v/mac-keyboard-shortcuts.svg)][pypi_]
[![Status](https://img.shields.io/pypi/status/mac-keyboard-shortcuts.svg)][status]
[![Python Version](https://img.shields.io/pypi/pyversions/mac-keyboard-shortcuts)][python version]
[![License](https://img.shields.io/pypi/l/mac-keyboard-shortcuts)][license]

[![Read the documentation at https://mac-keyboard-shortcuts.readthedocs.io/](https://img.shields.io/readthedocs/mac-keyboard-shortcuts/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/ekamil/mac-keyboard-shortcuts/workflows/Tests/badge.svg)][tests]
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi_]: https://pypi.org/project/mac-keyboard-shortcuts/
[status]: https://pypi.org/project/mac-keyboard-shortcuts/
[python version]: https://pypi.org/project/mac-keyboard-shortcuts
[read the docs]: https://mac-keyboard-shortcuts.readthedocs.io/
[tests]: https://github.com/ekamil/mac-keyboard-shortcuts/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/ekamil/mac-keyboard-shortcuts
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

Reads, modifies and writes the plist with keyboard shortcuts.

Kudos to all the people who compiled data sources I'm using here:

- [Gist with at least some hotkey actions](https://gist.github.com/mkhl/455002#file-ctrl-f1-c-L12)
- [Keycodes](https://gist.github.com/jimratliff/227088cc936065598bedfd91c360334e)
- [Modifiers - all combinations](https://gist.github.com/stephancasas/74c4621e2492fb875f0f42778d432973)

## Features

- Print, diff, and update Mac hotkeys
- Works as a CLI utility and as a library

## Requirements

- Mac, only tested on Sonoma

## Installation

You can install _Mac Keyboard Shortcuts_ via [pip] from [PyPI]:

```console
$ pip install mac-keyboard-shortcuts
```

## Usage

Please see [Command-line Reference] or [API Usage Examples] for details.

## Contributing

Contributions are very welcome. For inspiration look at [file an issue|issues].
Especially the action codes and the logic around modifier masks needs attention.

To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_Mac Keyboard Shortcuts_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.

[@cjolowicz]: https://github.com/cjolowicz
[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[file an issue]: https://github.com/ekamil/mac-keyboard-shortcuts/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/ekamil/mac-keyboard-shortcuts/blob/main/LICENSE
[contributor guide]: https://github.com/ekamil/mac-keyboard-shortcuts/blob/main/CONTRIBUTING.md
[command-line reference]: https://mac-keyboard-shortcuts.readthedocs.io/en/latest/cli-usage.html
[api usage examples]: https://mac-keyboard-shortcuts.readthedocs.io/en/latest/api-usage.html
