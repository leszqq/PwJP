#!/usr/bin/python3
"""
Autor: Wiktor Lechowicz

Ten skrypt zlicza liczbe plikow w katalogu /dev.
Zostal przetestowany przy uzyciue WSL2
"""

import os
print("liczba plikow w katalogu /dev: " + str(len(os.listdir('/dev'))))
