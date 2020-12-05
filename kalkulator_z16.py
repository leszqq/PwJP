# Autor: Wiktor Lechowicz
# Kalkulator dla liczb zespolonych
# Działanie do wykonania należy wpisać w terminalu w jednej linii
# np. (1 + j0.3)/abs(j3) + p(3 +j3) - conj(1 -j4.3)*2
# abs() - moduł
# p( ) - faza
# conj( ) - sprzężenie

import liczby_zespolone_z15 as c
import cmath  # dla testów
import re


def my_repl(m):
    if m.group(1) is not None:
        return "c.MyComplex(real=" + m.group(1) + ")"
    elif m.group(2) is not None:
        return "c.MyComplex(imag=" + m.group(2).replace('j', '') + ")"
    elif m.group(3) is not None:
        return "c.MyComplex.mod"
    elif m.group(4) is not None:
        return "c.MyComplex.p"
    elif m.group(5) is not None:
        return "c.MyComplex.conj"


print("# Kalkulator dla liczb zespolonych\n"
      "# Działanie do wykonania należy wpisać w terminalu w jednej linii.\n"
      "# litera j musi poprzedzać część urojoną\n"
      "# np. (1 + j0.3)/mod(j3) + p(3 +j3) - conj(1 -j4.3)*2\n"
      "# mod( ) - moduł\n"
      "# p( ) - faza\n"
      "# conj( ) - sprzężenie\n")

reg = re.compile(r"(\d+(?:\.\d+)?)|(j\d+(?:\.\d+)?)|(mod)|(p)|(conj)")

# test
# print(eval(reg.sub(my_repl, " 1 - j1 + 3 + mod(3 -j4)/(3) + j1*p(1 -4/j1)")))
# print(1 - complex(0, 1) + 3 + 5/3 + complex(0, 1) * cmath.phase(1 - 4 / complex(0, 1)))

while True:
    print(">>")
    print(eval(reg.sub(my_repl, input())))
    