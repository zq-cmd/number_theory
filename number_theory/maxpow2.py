import functools


@functools.lru_cache
def maxpow2(x: int) -> int:
    if x >= 2:
        return 1 + maxpow2(x / 2)
    return 0
