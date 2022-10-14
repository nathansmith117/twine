from random import randint
import math

class Twine(str):

    def __init__(self, value):
        pass


    def pull_the_twine(self) -> tuple:
        pull_at = randint(1, len(self))
        return (Twine(self[:pull_at]), Twine(self[pull_at:]))


    def __add__(self, value):
        return Twine(str(self) + value)


    def __mul__(self, value: int):
        return Twine(str(self) * value)


    def __truediv__(self, value: int):
        return Twine(self[:len(self) // value])


    def __pow__(self, value: int):
        start_len = len(self)
        res = str(self)

        for n in range(value - 1):
            res *= start_len

        return Twine(res)


    def sqrt(self):
        return Twine(self[:int(math.sqrt(len(self)))])
