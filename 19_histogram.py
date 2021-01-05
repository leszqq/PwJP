# autor: Wiktor Lechowicz
# wielowątkowe liczenie histogramu

import numpy as np
import matplotlib.pyplot as plt
import time
import math as m
import multiprocessing as mp
from itertools import repeat

NUM_OF_BARS = 30

# funkcja do obliczania histogramu
def my_hist(arr, minim, maxim, num_of_groups=10):
    hist_arr = np.ndarray(num_of_groups)
    for i in range(num_of_groups):
        hist_arr[i] = 0
    k = (maxim - minim) / num_of_groups
    for element in arr:
        hist_arr[m.ceil((element - minim) / k) - 1] += 1
    return hist_arr


# funkcja uruchamiająca funkcje do liczenia histogramu w wielu(4) procesach
def my_hist_multiprocess(arr, num_of_groups=10):
    minim = min(arr)
    maxim = max(arr)
    pool = mp.Pool()
    res = sum(pool.starmap(my_hist, zip(np.array_split(arr, m.ceil(len(arr)/4)), repeat(minim), repeat(maxim), repeat(num_of_groups))))
    res[0] += 1
    res[len(res) - 1] -= 1
    return res


if __name__ == '__main__':
    # testowy wektor liczb losowych
    r_arr = np.random.randn(1000) * 20 + 50

    plt.figure(1)
    plt.grid(True)
    t = time.time()
    plt.hist(r_arr, NUM_OF_BARS)
    plt.title("Histogram matplotlib.plt, czas obliczeń: " + str(time.time() - t) + " [s]")
    my_h = my_hist_multiprocess(r_arr, NUM_OF_BARS)

    plt.figure(2)
    plt.grid(True)
    t = time.time()
    plt.bar(np.linspace( min(r_arr), max(r_arr) - (max(r_arr) - min(r_arr))/NUM_OF_BARS, len(my_h)),
            my_h,
            width=(max(r_arr) - min(r_arr))/NUM_OF_BARS,
            color='g',
            align='edge')
    plt.title("Histogram implementowany, czas obliczeń: " + str(time.time() - t) + " [s]")
    plt.show()
