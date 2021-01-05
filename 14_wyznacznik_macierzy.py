"""
Autor: Wiktor Lechowicz
Ten skrypt umozliwia obliczenia wyznacznika macierzy dowolnego stopnia.
Przez macierz rozumie sie liste list
Algorytm na podstawie definicji z podreczniku openAGH
"""
import random as r

# zwraca macierz m z wyciętym i-tym wierszem i pierwszą(zerową w indeksowaniu pythona) kolumną
def my_sub_matrix(m ,i):
    ms = []
    for row in range(len(m)):
        ms.append([])
        for col in range(1, len(m)):
           ms[row].append(m[row][col])

    ms.pop(i)
    return ms


def my_det(m):
    if len(m) == len(m[0]):
        s = len(m)
        if s == 1:
            return m[0][0]
        else:
            det = 0
            for i in range(s):
                det += ((-1)**i)*m[i][0]*my_det(my_sub_matrix(m, i))
            return det
    else:
        print("Macierz nie jest kwadratowa")

# generacja macierzy
s = 4
matrix = []
for i in range(s):
    matrix.append([])
    for j in range(s):
        matrix[i].append(r.randint(-10, 10))

# test
for r in matrix:
    print(r)
print("det = "+  str(my_det(matrix)))