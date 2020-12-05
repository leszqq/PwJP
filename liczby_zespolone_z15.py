"""
Autor: Wiktor Lechowicz
Klasa do operacji na liczbach zespolonych
"""
import math as m


class MyComplex:
    def __init__(self, real, imag):
        self.r = real
        self.i = imag

    def abs(self):
        return MyComplex(m.sqrt(self.r ** 2 + self.i ** 2), 0)

    def phase(self):
        if self.r != 0:
            return MyComplex(m.atan2(self.i / self.r), 0)
        else:
            return MyComplex(0, 0)

    def conjugate(self):
        return MyComplex(self.r, -self.i)

    def __add__(self, other):
        return MyComplex(self.r + other.r, self.i + other.i)

    def __sub__(self, other):
        return MyComplex(self.r - other.r, self.i - other.i)

    def __mul__(self, other):
        return MyComplex(self.r*other.r - self.i*other.i, self.r*other.i + self.i*other.r)

    def __truediv__(self, other):
        try:
            return self*MyComplex(other.r, -other.i)*MyComplex(1/(other.r**2 + other.i**2), 0)
        except ZeroDivisionError:
            print("Zero division error")
            return MyComplex(10E20, 10E20)

    def __str__(self):
        if self.i < 0:
            return "{} -j{}".format(self.r, -self.i)
        else:
            return "{} +j{}".format(self.r, self.i)
