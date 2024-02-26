# Command line

```{eval-rst}
.. click:: mac_keyboard_shortcuts.__main__:main
    :prog: mac-keyboard-shortcuts
    :nested: full
```

## Note for mutate

The function mutating shortcuts have to conform to this signature:

```python
from typing import Iterable

from mac_keyboard_shortcuts.types.entry import HotKeyEntry


def main(entries: Iterable[HotKeyEntry]) -> Iterable[HotKeyEntry]:
    yield from entries

```

Type hints are optional.
