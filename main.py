import re
import csv
import pandas as pd

#Validacion de header por medio de regex
def validarHeader(line):
    headers = []
    reHeader = re.compile(r"[^,\s][^\,]*[^,\s]*") #Regex utilizado para validar headers
    '''
    Explicacion regex:
    Se hace match a cualquiera de los caracteres dentro de las comas delimitadoras
    '''
    for word in line:
        #Validamos las palabras dentro de la linea que contiene los headers
        headerName = reHeader.match(word).group(0)
        headers.append(headerName)
    return headers

#Validacion de contenido por medio de regex
def validarContenido(line):
    content = []
    reContent = re.compile(r'''(?:,|\n|^)("(?:(?:"")*[^"]*)*"|[^",\n]*|(?:\n|$))''') #Regex utilizado para validar el contenido
    '''
    Explicacion regex:
    (?:,|\n|^)      Revisa que los valores inicien al inicio del archivo o string,  
                    al final de la linea previa, o luego de una coma.  
    (               El contenido puede ser:
    "               (1.) Una cadena entre comillas dobles, comenzando con comillas ("),  
        (?:         contener cualquier numero de comillas dobles ("") o caracteres sin dobles comillas
        (?:"")*     en cualquier orden y cualquier cantidad de veces.
        [^"]*      
        )*         
    "               

    |               (2.) Un valor sin comillas dobles  

    [^",\n]*        conteniendo cualquier numero de caracteres que...
                    ...no sean comillas dobles, comas o una "newline" (\n)  

    |               (3. ) Una sola "newline" o caracter final de la cadena o archivo
                    utilizado para capturar valores vacios
    (?:\n|$)        al final de las diferentes lineas o archivo en caso que se lea directamente de este.
    )
    '''

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

mainDF = pd.DataFrame(content, columns=headers) #Los contenidos y headers validaos se ingresan dentro del dataframe

print(mainDF)

#Output dentro archivos de texto y .csv para validar resultados del dataframe
with open(r'output.txt', 'w+', encoding='utf-8') as f:
    dfAsString = mainDF.to_string(header=True, index=True)
    f.write(dfAsString)

mainDF.to_csv(r'output.csv', mode='w+', encoding='utf-8', header=True, index = False)

    

