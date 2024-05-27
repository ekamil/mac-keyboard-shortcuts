Run the function `main` from the script below and it should

- kill system settings app
- disable all currently enabled and known hot keys
- enable a few key shortcuts (like ctrl+left)
- keep as-is hotkeys whose function we don't know

For definition of "known", see {class}`mac_keyboard_shortcuts.api.Actions`

```{literalinclude} /examples/minimal_with_alfred/code.py
---
language: python
---
```
