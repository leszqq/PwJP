"""
Autor: Wiktor Lechowicz

Ten skrypt pobiera od uzytkownika imie, nazwisko i rok urodzenia.
Dane powinny byc podane w jednej linii i powinny byc oddzielone przecinkiem
"""

print("Prosze podac imie, nazwisko i rok urodzenia (oddzielone przecinkiem):")
try:
    imie, nazwisko, rok = input().split(',')
    print("Sprawdzenie zapisanych danych:\n"
          "imie: " + imie + "\n"
          "nazwisko: " + nazwisko + "\n"
          "rok: " + rok)
except:
    print("Niepoprawny format wprowadzoncyh danych")

