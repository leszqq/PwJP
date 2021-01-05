#!/usr/bin/python3
"""
Autor: Wiktor Lechowicz

Skrypt realizuje rekurencyjne przejscie drzewa katalogow i wypisanie plikow,
ktore znajduja sie w miejscu okreslonym w zmiennej path
"""

import os

tab_count = 0
path = "/home/wiktor/python_files"	# przykladowa sciezka


#funkcja wypisuje pliki w aktualnej lokacji, lub wywoluje sama siebie dla folderow


def list_files(directory):
	global tab_count
	for i in os.listdir(directory):
		if os.path.isdir(directory + "//" + i):
			print(tab_count*"  " + directory + "/" + i)
			tab_count += 1
			list_files(directory + "/" + i)
		else:
			print("  "*tab_count + i)
	tab_count -= 1


list(path)
