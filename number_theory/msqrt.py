from .mod import mod
from .euler import euler


def msqrt(x: mod, y: int, eu :any = None) -> mod:
    if not isinstance(eu, int):
        eu = euler(x.mod)
    return x**((mod(eu, y)**-1).num)
