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


    def __rshift__(self, value: int):
        output_buf = list(self)
        the_len = len(self)

        if value < 0:
            raise(ValueError("negative shift count"))

        for i, c in enumerate(self):
            output_buf[(i + value) % the_len] = c

        return Twine("".join(output_buf))


    def __lshift__(self, value: int):
        output_buf = list(self)

        if value < 0:
            raise(ValueError("negative shift count"))

        for i, c in enumerate(self):
            output_buf[i - value] = c

        return Twine("".join(output_buf))


    def __invert__(self):
        output_buf = Twine("")

        for i in self:
            if i.isupper():
                output_buf += i.lower()
            else:
                output_buf += i.upper()

        return output_buf


    def sqrt(self):
        return Twine(self[:int(math.sqrt(len(self)))])
