from .mod import mod
from .primp import primp
from .prootp import prootp

import random


def elgamal_en(x: mod, g: mod, a: mod) -> (mod, mod):
    r = random.randint(10, 100)
    return (g**r, x * a**r)


def elgamal_de(x: mod, y: mod, k: mod) -> mod:
    return y / (x**k)


def elgamal_gen() -> (mod, mod, mod):
    ran_gen = lambda: random.randint(10, 100)
    p = ran_gen()
    while not primp(p):
        p = ran_gen()
    g = mod(p, ran_gen())
    while not prootp(g):
        g = mod(p, ran_gen())
    k = mod(p - 1, ran_gen())
    return p, g, k
