"""
Autor: Wiktor Lechowicz

Skrypt usuwa z wejsciowego ciagu tekstowego slowa: sie, i, oraz, nigdy, dlaczego
"""
import re

patterns = {"\\b[Ss]ie\\b", r"\bi\b", r"\boraz\b", r"\b[Nn]igdy\b", r"\b[Dd]laczego\b"}

text = " " + input("Podaj ciag tekstowy: ") + " "

for p in patterns:
    text = re.sub(p, "", text)

text = re.sub(r"\s+", " ", text)

print("Tekst po usunieciu slow: \"sie\", \"i\", \"oraz\", \"nigdy\", \"dlaczego\": \n" + text)