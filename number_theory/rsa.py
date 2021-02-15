from .mod import mod
from .gcd import gcd
from .msqrt import msqrt
from .primp import primp

import random


def rsa_en(x: mod, k: int) -> mod:
    return x**k


def rsa_de(x: mod, k: int, eu: int) -> mod:
    return msqrt(x, k, eu)


def rsa_gen():
    ran_gen = lambda: random.randint(10, 100)
    a, b, k = ran_gen(), ran_gen(), ran_gen()
    while not primp(a):
        a = ran_gen()
    while not primp(b):
        b = ran_gen()
    eu = (a - 1) * (b - 1)
    while gcd(k, eu) != 1:
        k = ran_gen()
    return a, b, k
