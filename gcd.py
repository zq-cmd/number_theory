import random

def gcd(x: int, y: int) -> int:
    if x < 0:
        x = -x
    if y < 0:
        y = -y
    if x > y:
        x, y = y, x
    if x == 0:
        return y
    return gcd(y % x, x)

def gcdn(x: int, y: int, tx: any = None, ty: any = None,
         txa: int = 1, txb: int = 0, tya: int = 0, tyb: int = 1)\
         -> (int, int, int, int, int):
    if x < 0:
        x = -x
    if y < 0:
        y = -y
    if x > y:
        x, y = y, x
    if not isinstance(tx, int):
        tx = x
    if not isinstance(ty, int):
        ty = y
    if tx == 0:
        return (x, y, ty, tya, tyb)
    tmp = ty // tx
    return gcdn(x, y, ty - tmp * tx, tx, tya - tmp * txa, tyb - tmp * txb, txa, txb)

def random_gcdn(max_seed :int = 1000) -> (int, int, int, int, int):
    x, y = random.randint(1, 1000), random.randint(1, 1000)
    return gcdn(x, y)
