import re
import csv
import pandas as pd

#Validacion de header por medio de regex
def validarHeader(line):
    headers = []
    reHeader = re.compile(r"[a-zA-Z]+") #Regex utilizado para validar headers
    for word in line:
        #Validamos las palabras dentro de la linea que contiene los headers
        headerName = reHeader.match(word).group(0)
        headers.append(headerName)
    return headers

#Validacion de contenido por medio de regex
def validarContenido(line):
    content = []
    reContent = re.compile(r'''(?:,|\n|^)("(?:(?:"")*[^"]*)*"|[^",\n]*|(?:\n|$))''')
    for word in line:
        contentName = reContent.match(word).group(0)
        content.append(contentName)
    return content

#El .csv se coloca dentro de una lista
with open('BL-Flickr-Images-Book.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)

noColumns = len(data[0])
content = []

#Validacion de header con regex
for row in data:
    headers = validarHeader(row)
    if len(headers) == noColumns:
        break

del data[0]
#Validacion de contenido de columna
for row in data:
    try:
        content.append(validarContenido(row))
    except:
        print(row)



    

