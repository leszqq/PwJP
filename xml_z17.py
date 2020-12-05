# Autor: Wiktor Lechowicz
# parsowanie pliku xml_file.xml
# po modyfikacji plik jest zapisywany pod nazwą xml_file_up.xml

import xml

# parser DOM
from xml.dom.minidom import parse
import xml.dom.minidom

# open XML doc
f = xml.dom.minidom.parse("xml_file.xml")
col = f.documentElement

users = col.getElementsByTagName("user")

users[0].setAttribute("id", "3")

with open("xml_file_up.xml", "w") as file:
    file.write(f.toxml())
#
