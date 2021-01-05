"""
Autor: Wiktor Lechowicz
Ten skrypt sluzy do obliczania pierwiastkow rownania kwadratowego
argumenty skryptu : a, b, c. y = ax^2 + bx + c
"""
import cmath as cm
import sys
# odczyt argumentow
try:
    n, a, b, c = sys.argv
except:
    print("input error")
a, b, c = float(a), float(b), float(c)
# obliczanie pierwiastkow
sqr_D = complex(cm.sqrt(b**2 - 4*a*c))
if(sqr_D != 0):
    x_0 = complex((- b - sqr_D)/(2*a))
    x_1 = complex((- b + sqr_D)/(2*a))
else:
    x_0 = x_1 = complex(-b/(2*a))

print("Pierwiastki rownania to: "+ str(x_0.real) +" j"+ str(x_0.imag) +", "+ str(x_1.real) +" j"+ str(x_1.imag))