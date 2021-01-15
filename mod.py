from .gcd import gcdn

class mod:

    def __init__(self, mod, num):
        self.mod = mod
        self.num = num % self.mod

    def __str__(self):
        return f'{self.num} mod {self.mod}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, int):
            return self.num == other % self.mod
        if isinstance(other, mod) and other.mod == self.mod:
            return self.num == other.num
        raise ValueError

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if isinstance(other, int):
            return self.num < other % self.mod
        if isinstance(other, mod) and other.mod == self.mod:
            return self.num < other.num
        raise ValueError

    def __gt__(self, other):
        return not (self == other or self < other)

    def __le__(self, other):
        return not self > other

    def __ge__(self, other):
        return not self < other

    def __add__(self, other):
        if isinstance(other, int):
            return mod(self.mod, self.num + other)
        if isinstance(other, mod) and other.mod == self.mod:
            return mod(self.mod, self.num + other.num)
        raise ValueError

    def __neg__(self):
        return mod(self.mod, -self.num)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if isinstance(other, int):
            return mod(self.mod, self.num * other)
        if isinstance(other, mod) and other.mod == self.mod:
            return mod(self.mod, self.num * other.num)
        raise ValueError

    def __truediv__(self, other):
        if isinstance(other, int):
            tmp = other % self.num
        elif isinstance(other, mod) and other.mod == self.mod:
            tmp = other.num
        else:
            raise ValueError
        if tmp == 0:
            raise ZeroDivisionError
        res = gcdn(tmp, self.mod)
        if res[2] != 1:
            raise ZeroDivisionError
        return self * mod(self.mod, res[3])
