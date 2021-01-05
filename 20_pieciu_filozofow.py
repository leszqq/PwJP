# autor: Wiktor Lechowicz
# Problem pieciu filozofow

import threading
from random import randint
from time import sleep


class Philo(threading.Thread):

    def __init__(self, name, l_fork, r_fork):
        threading.Thread.__init__(self)
        self.name = name
        self.l_fork = l_fork
        self.r_fork = r_fork

    def run(self):
        while True:
            self.think()
            sleep(randint(10, 100)/10)
            self.eat()

    def think(self):
        print(self.name, "myśli")

    def eat(self):
        print(self.name, "jest głodny")
        self.l_fork.acquire()
        self.r_fork.acquire()
        print(self.name, "je")
        sleep(randint(100, 100000)/10000)
        print(self.name, "skończył jeść")
        self.l_fork.release()
        self.r_fork.release()


forks = [threading.Lock() for i in range(5)]
philos = [Philo("Filozof " + str(i), forks[i], forks[(i + 1) % 5]) for i in range(5)]

for p in philos:
    p.start()
