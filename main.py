import re
import csv
import pandas as pd

def validarHeader(line):
    headers = []
    reHeader = re.compile(r"[a-zA-Z]+") #Regex utilizado para validar headers
    for word in line:
        #Validamos las palabras dentro de la linea que contiene los headers
        headerName = reHeader.match(word).group(0)
        headers.append(headerName)
    return headers

def validarContenido(line):
    pass

with open('BL-Flickr-Images-Book.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)

noColumns = len(data[0])

#Validacion de header con regex
# ...
for row in data:
    headers = validarHeader(row)
    if len(headers) == noColumns:
        break

print(headers)

#Validacion de contenido de columna
# ...


