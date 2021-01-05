"""
Autor: Wiktor Lechowicz

Skrypt do konwersji plikow z formatu jpeg do png
"""
from PIL import Image

try:
    path = input("Podaj sciezke pliku do konwersji")
    im = Image.open(path)
    im.save(path[:path.index('.')] + ".png")
except:
    print("BLAD")



