You can run external Python code as a plugin from _mac_keyboard_shortcuts_ CLI. This allows you to just pipx install and
then call the command-line utility instead of writing executable code (granted, that's not too big of a difference).

The example below would do nothing but disable one single shortcut.
**Important: yield all the shortcuts you wish to have, this is not a partial function**

Consult {class}`mac_keyboard_shortcuts.api.Actions` and {class}`mac_keyboard_shortcuts.api.HotKeyEntry`.

1. Put the code below somewhere, the file should be named like a valid Python module

```{literalinclude} /examples/execute_module/code.py
---
language: python
---
```

2. Run the CLI like this:

```shell
mac-keyboard-shortcuts mutate --dry-run --validate ./docs/examples/execute_module/code.py
```
