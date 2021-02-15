import functools


@functools.lru_cache
def primp(x: int) -> bool:
    for i in range(2, int(x ** (1/2)) + 1):
        if x % i == 0:
            return False
    return True
