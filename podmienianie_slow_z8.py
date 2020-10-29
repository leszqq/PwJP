"""
Autor: Wiktor Lechowicz

Skrypt podmienia w wejsciowym ciagu tekstowym slowa: i => oraz, oraz => i, nigdy => prawie nigdy, dlaczego => czemu
"""
import re


def repl(match_obj):
    for k in dictionary:
        if match_obj.group(0) == k:
            return dictionary[k]


pattern = r"(\bi\b)|(\bi\b)|(\boraz\b)|(\b[Nn]igdy\b)|(\bdlaczego\b)"
dictionary = {"i": "oraz",
              "oraz": "i",
              "nigdy": "prawie nigdy",
              "dlaczego": "czemu"}

text = " " + input("Podaj ciag tekstowy: ") + " "
text = re.sub(pattern, repl, text, flags=re.IGNORECASE)


print("Tekst po podmienieniu slow: \"sie\", \"i\", \"oraz\", \"nigdy\", \"dlaczego\": \n" + text)