import contextlib
from typing import TypeVar, Generator

T = TypeVar("T")


@contextlib.contextmanager
def same(val: T) -> Generator[T, None, None]:
    yield val
