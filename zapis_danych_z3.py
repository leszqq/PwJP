"""
Autor: Wiktor Lechowicz

Ten skrypt realizuje funkcje zamka szyfrowego. Przy pierwszym uruchomieniu uzytkownik podaje kod dostepu,
ktory jest wymagany przy kolejnym uruchomieniu skryptu. Kod dostepu jest zapisywany w pliku tekstowym.
"""

try:
    file = open('zapis_danych_z3_kod.txt', 'r')
    password = file.read()
except:
    file = open('zapis_danych_z3_kod.txt', 'w+')                                                        # stworz plik jesli nie istnieje

    # zapis nowego kodu
    print('Kod nie zostal jeszcze ustalony lub plik z kodem zostal uszkodzony. Wpisz nowy kod dostepu: ')
    while(True):
        try:
            password = input()
            file.write(password)
            break
        except:
            print('Blednie wprowadzone dane, sprobuj ponownie:')

print("Podaj kod dostepu:")
try:
    if (input() == password):
        print("OK")
    else:
        print("kod bledny")
except:
    "Niepoprawny format wprowadzoncyh danych"


print(file.read())
