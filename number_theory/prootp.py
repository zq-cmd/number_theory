from .mod import mod
from .primp import primp


def prootp(x: mod) -> bool:
    if not primp(x.mod):
        return False
    for i in filter(lambda y: (x.mod - 1) % y == 0, range(1, x.mod - 1)):
        if x**i == 1:
            return False
    return True
