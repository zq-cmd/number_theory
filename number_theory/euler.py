from .primp import primp
from typing import List, Tuple
import functools

def count_prim(x: int, y: int) -> int:
    if primp(y) and x % y == 0:
        return count_prim(x // y, y) + 1
    return 0

def split_number(x: int, cur: int = 2) -> List [Tuple]:
    if x < cur:
        return []
    tmp = count_prim(x, cur)
    if tmp > 0:
        return [(cur, tmp)] + split_number(x // (cur ** tmp), cur + 1)
    return split_number(x, cur + 1)

def euler(x: int) -> int:
    return functools.reduce(lambda x, y: x * y,
                            (i[0] ** (i[1] - 1) * (i[0] - 1) for i in split_number(x)))
