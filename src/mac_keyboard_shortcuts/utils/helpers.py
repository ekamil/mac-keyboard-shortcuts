import contextlib
from typing import TypeVar

T = TypeVar("T")


@contextlib.contextmanager
def same(val: T) -> T:
    yield val
