from random import randint
import math


class Twine(str):

    def __init__(self, value):
        pass


    def pull_the_twine(self) -> tuple:
        pull_at = randint(1, len(self))
        return (self[:pull_at], self[pull_at:])


    def __add__(self, value):
        return Twine(str(self) + value)


    def __mul__(self, value: int):
        return Twine(str(self) * value)


    def __truediv__(self, value: int):
        the_len = len(self)
        chars_per_section = the_len // value

        return Twine(self[:chars_per_section])


    def __pow__(self, value: int):
        str_value = str(self)
        start_len = len(self)

        for c in range(value - 1):
            str_value *= start_len

        return Twine(str_value)


    def sqrt(self):
        return Twine(self[:int(math.sqrt(len(self)))])
