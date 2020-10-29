"""
Autor: Wiktor Lechowicz
Ten skrypt sluzy do sortowania liczb malejaco.
Selection sort
"""
import random as r
import sys

# random numbers
rnd_list = []
for i in range(50):
    rnd_list.append(r.randint(-1000, 1000))

print(rnd_list)


# pops minimum value from integer list
def pop_min(l):
    min_of = sys.maxsize
    min_index = 0
    for i in range(len(l)):
        if l[i] < min_of:
            min_of = l[i]
            min_index = i
    return l.pop(min_index)


sorted_list = []
for i in range(len(rnd_list.copy())):
    sorted_list.append(pop_min(rnd_list))

print(sorted_list)