"""
Autor: Wiktor Lechowicz
Ten skrypt sluzy do obliczania wartosci iloczynu skalarnego 2 wektorow
"""

a = [1, 2, 12, 4]
b = [2, 4, 2, 8]


def product(a, b):
    p = 0
    for i in range(len(a)):
        p += a[i] * b[i]
    return p


print(product(a, b))
