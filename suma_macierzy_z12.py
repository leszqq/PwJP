"""
Autor: Wiktor Lechowicz
Ten skrypt służy do sumowania macierzy 128x128
"""

import random as r


# sumowanie
def my_matrix_sum(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        v_cnt = len(m1)
        c_cnt = len(m1[0])
        m_s = []
        for m in range(v_cnt):
            m_s.append([])
            for n in range(c_cnt):
                m_s[m].append(m1[m][n])

        for m in range(v_cnt):
            for n in range(c_cnt):
                m_s[m][n] = m_s[m][n] + m2[m][n]
        return m_s
    else:
        print("Niezgodne wymiary macierzy")
        return


# generowanie macierzy m wierszy na n kolumn, m = n = 128
m = n = 10
matrix1 = []
matrix2 = []
for i in range(m):
    matrix1.append([])
    matrix2.append([])
    for j in range(n):
        matrix1[i].append(r.randint(-100, 100))
        matrix2[i].append(r.randint(-100, 100))

# test
matrix_sum = my_matrix_sum(matrix1, matrix2)
# wyniki mozna wyswietlic w scientific mode 
