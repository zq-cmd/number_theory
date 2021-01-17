import random

def pythagorean(u: int, v:int) -> (int, int, int):
    if u < 0:
        u = -u
    if v < 0:
        v = -v
    if u < v:
        u, v = v, u
    return (u ** 2 - v ** 2, 2 * u * v, u ** 2 + v ** 2)

def random_pyagorean(max_seed :int = 1000) -> (int, int ,int):
    u, v = random.randint(1, max_seed), random.randint(1, max_seed)
    return pythagorean(u, v)
