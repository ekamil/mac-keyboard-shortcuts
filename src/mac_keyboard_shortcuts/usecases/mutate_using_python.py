import importlib.machinery
import importlib.util
from pathlib import Path

from mac_keyboard_shortcuts.types.aliases import HotKeyEntries, HKMutator
from mac_keyboard_shortcuts.utils.plist_reading import parse_plist_data
from mac_keyboard_shortcuts.utils.plist_writing import plist_writer, format_for_writing


def import_script(
    python_file: Path,
) -> HKMutator:
    loader = importlib.machinery.SourceFileLoader(
        "plist_mutator", str(python_file.absolute())
    )
    spec = importlib.util.spec_from_loader("plist_mutator", loader)
    if not spec:
        raise RuntimeError(f"Can't import file at {str(python_file)}")
    plist_mutator = importlib.util.module_from_spec(spec)
    loader.exec_module(plist_mutator)
    return plist_mutator.main  # type:ignore[no-any-return]


def mutate_impl(
    python_file: Path,
    plist_path: Path,
    dry_run: bool,
    validate: bool,
) -> None:
    mutator_function: HKMutator = import_script(python_file)
    with plist_writer(
        str(plist_path.absolute()),
        backup=True,
        replace=not dry_run,
        validate=validate,
        print_diff=dry_run or validate,
    ) as raw_plist_data:
        parsed = parse_plist_data(raw_plist_data)  # type:ignore[arg-type]
        parsed: HotKeyEntries = mutator_function(parsed)
        # Override the original dict
        format_for_writing(
            parsed,
            raw_plist_data,  # type:ignore[arg-type]
        )
