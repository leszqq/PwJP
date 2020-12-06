# autor: Wiktor Lechowicz
# program implementujący funkcjonalność pamiętnika:
# zapis, odczyt i modyfikacja wpisów wraz z datą, ocena jakości wspomnienia x/10
# wpisy są zapisywane w pliku CSV

# nazwa
# data
# opis
# ocena
# odczyt i wyświetlanie wcześniej wprowadzonych danych

import csv
import os


def print_diary():
    with open(r"csv_json_pamietnik_database.csv") as f:
        try:
            reader = csv.reader(f, delimiter=';')
            next(reader)
            for row in reader:
                print("\n=================================================\n" +
                      "nazwa: " + row[0] +
                      "\ndata: " + row[1] +
                      "\nopis: " + row[2] +
                      "\nocena wspomnienia: " + row[3] + "\n")
        except IndexError:
            print("Brak wpisów")


def add_memory():
    try:
        with open(r"csv_json_pamietnik_database.csv", 'a', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow([str(input("podaj nazwę wpisu >>")),
                             str(input("podaj datę >>")),
                             str(input("podaj opis wspomnienia >>")),
                             str(input("podaj ocenę wspomnienia w skali od 1 do 10 >>"))])
    except Exception:
        print("nieznany błąd")


def delete_memory(name):
    l = list()
    try:
        with open(r"csv_json_pamietnik_database.csv") as fs:
            reader = csv.reader(fs, delimiter=';')
            for row in reader:
                l.append(row)

        with open(r"csv_json_pamietnik_temp.csv", 'w', newline='') as fd:
            writer = csv.writer(fd, delimiter=';')
            for row in l:
                if (row[0] != name):
                    writer.writerow(row)
    except Exception:
        print("nieznany błąd")

    os.remove("csv_json_pamietnik_database.csv")
    os.rename("csv_json_pamietnik_temp.csv", "csv_json_pamietnik_database.csv")


# usuwanie / dodawanie nowych wpisów
while True:
    print(
        "Dodaj nowe wspomnienie [+], usuń stare wspomnienie [-], zakończ program[q], wyświetl listę wspomnień [p]\n>>")
    inp = input()
    if inp == '+':
        add_memory()
    elif inp == '-':
        delete_memory(input("Podaj nazwe wpisu do usunięcia >> "))
        print("TODO")
    elif inp == 'p':
        print_diary()
    elif inp == 'q':
        break
