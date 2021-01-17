from .mod import mod
import functools


@functools.lru_cache
def primp(x: int) -> bool:
    return x == 2 or mod(x, 2)**(x - 1) == 1
