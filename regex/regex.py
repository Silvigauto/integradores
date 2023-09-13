import re

'''
1.Verificar correo electrónico: Crea una función que tome una cadena de texto como 
argumento y verifique si se trata de una dirección de correo electrónico válida. 
Una dirección de correo electrónico válida debe tener un formato como 
"usuario@dominio.com".

2.Eliminar dígitos: Crea una función que tome una cadena de texto y 
elimine todos los dígitos que contiene.

3.Validar formato de fecha: Crea una función que tome una cadena de texto 
como argumento y verifique si se trata de una fecha válida en formato 
"dd/mm/aaaa".

4.Reemplazar formato de fecha: Crea una función que tome una cadena de texto
que contiene una fecha en formato "dd/mm/aaaa" y  la reemplace por 
la misma fecha en formato "mm/dd/aaaa".

5.Validar número de teléfono: Escribe una expresión regular que valide un 
número de teléfono con el siguiente formato: 
"+54 9 11 1234-5678". 
La expresión regular debe aceptar números de teléfono con el código de país 
"+54", seguido de un espacio, el dígito 9, otro espacio, el código de área de dos dígitos,
un espacio, el número de teléfono de ocho dígitos separado por un guión en la mitad.

6.Validar CUIL: Escribe una expresión regular que valide un CUIL con el siguiente 
formato: 
"20-12345678-1". 
La expresión regular debe aceptar CUILS que comiencen con "20" 
seguido de un guión, ocho dígitos y otro guión, seguido del último dígito que 
es un verificador.

'''

#1.Verificar correo electrónico: Crea una función que tome una cadena de texto como 
# argumento y verifique si se trata de una dirección de correo electrónico válida. 
# Una dirección de correo electrónico válida debe tener un formato como 
# "usuario@dominio.com".

def verificar_correo_electronico(cadena_texto):
    if re.findall('@', cadena_texto):
        print('se encontro el arroba')
    else:
        print('esto no es un correo electronico')

#verificar_correo_electronico('hola')
#print('hola')  
