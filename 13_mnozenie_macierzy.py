"""
Autor: Wiktor Lechowicz
Ten skrypt wykonuje mnozenie macierzy o rozmiarach 8x8
"""

import random as r

# mnozenie
def my_matrix_mul(m1, m2):
    if len(m1[0]) == len(m2):
        c_cnt = len(m1)
        r_cnt = len(m2[0])
        m_m = []
        for m in range(r_cnt):
            m_m.append([])
            for n in range(c_cnt):
                cell = 0
                for i in range(len(m1[0])):
                    cell += m1[m][i] * m2[i][n]
                m_m[m].append(cell)
        return m_m
    else:
        print("Niepoprawne wymiary macierzy")
        return

# generacja macierzy
m = n = 8
matrix1 = []
matrix2 = []
for i in range(m):
    matrix1.append([])
    matrix2.append([])
    for j in range(n):
        matrix1[i].append(r.randint(-100, 100))
        matrix2[i].append(r.randint(-100, 100))

# test
mul_matrix = my_matrix_mul(matrix1, matrix2)
# wynik mozna sprawdzi w scientific mode