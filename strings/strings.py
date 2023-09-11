'''
1.Contar letras: Crea una función que tome una cadena
de texto como argumento y
cuente el número de letras que contiene.
2.Eliminar caracteres: Crea una función que tome una
cadena de texto y un carácter como argumentos, y
elimine todas las ocurrencias de ese carácter en la
cadena.
3.Contar palabras: Crea una función que tome una
cadena de texto como argumento y
cuente el número de palabras que contiene.
Suponga que las palabras están separadas por un
espacio.
4.Reemplazar palabras: Crea una función que tome una
cadena de texto, una palabra y otra palabra como
argumentos, y reemplace todas las ocurrencias de la
primera palabra por la segunda en la cadena.
5.Buscar patrón: Crea una función que tome dos cadenas
de texto como argumentos: una cadena principal y un
patrón. La función debe encontrar todas las ocurrencias
del patrón en la cadena principal y devolver una lista con
las posiciones donde se encontró el patrón.
'''
from os import system
system('cls')

#1.Contar letras: Crea una función que tome una cadena de texto como argumento y 
# cuente el número de letras que contiene.

def contar_letras(cadena_texto):
    cantidad_letras = len(cadena_texto)
    print(cantidad_letras)

#2.Eliminar caracteres: Crea una función que tome una cadena de texto y 
# un carácter como argumentos, y elimine todas las ocurrencias de ese carácter en la
# cadena.

def eliminar_caracteres(cadena_texto, caracter_a_eliminar):
    cadena_texto = cadena_texto.replace(caracter_a_eliminar, '')
    print(cadena_texto)

'''
#forma mas complicada
# def eliminar_caracteres(cadena_texto, caracter_a_eliminar):
#     cadena_texto_limpia = []
#     for caracter in cadena_texto:
#         if caracter != caracter_a_eliminar:
#             cadena_texto_limpia.append(caracter)
#     print("".join(cadena_texto_limpia))
'''

#3.Contar palabras: Crea una función que tome una cadena de texto como argumento y
# cuente el número de palabras que contiene. Suponga que las palabras están 
# separadas por un espacio.

def contar_palabras(cadena_texto):
    cadena_texto = cadena_texto.split(' ')
    print(len(cadena_texto))


#4.Reemplazar palabras: Crea una función que tome una cadena de texto, una palabra 
# y otra palabra como argumentos, y reemplace todas las ocurrencias de la
# primera palabra por la segunda en la cadena.

def reemplazar_palabras(cadena_texto, primera_palabra, segunda_palabra):
    cadena_reemplazada = cadena_texto.replace(primera_palabra, segunda_palabra)
    print(cadena_reemplazada)

#5.Buscar patrón: Crea una función que tome dos cadenas de texto como argumentos: 
# una cadena principal y un patrón. La función debe encontrar todas las ocurrencias
# del patrón en la cadena principal y devolver una lista con
# las posiciones donde se encontró el patrón.

def buscar_patron(cadena_principal, patron):
    for caracter in cadena_principal:
        if caracter == patron:
            print(cadena_principal.index(patron))

buscar_patron('hhola mundos', 'o')