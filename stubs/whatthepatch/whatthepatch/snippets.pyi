from collections.abc import Sequence
from typing import Pattern

def remove(path: str) -> None: ...
def findall_regex(items: Sequence[str], regex: Pattern) -> list[int]: ...
def split_by_regex(items: Sequence[str], regex: Pattern) -> list[Sequence[str]]: ...
def which(program: str) -> str | None: ...
