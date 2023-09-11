from os import system
system("cls")
from data_stark import *


def imprimir_nombre_superheroe():
#B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
    for personaje in lista_personajes:
        print(personaje["nombre"])

def imprimir_nombre_altura():
#C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
    for personaje in lista_personajes:
        print(f"Nombre: {personaje['nombre']} Altura: {personaje['altura']}")

def encontrar_heroe_mas_alto():
#D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
    flag_primero = True
    for personaje in lista_personajes:
        altura_parseada = float(personaje['altura'])
        if flag_primero == True or altura_parseada > altura_maxima:
            altura_maxima = altura_parseada
            nombre_altura_maxima = personaje['nombre']
            flag_primero = False
    print(f"altura maxima: {altura_maxima} ")

# #calcular si hay otra altura maxima
    for personaje in lista_personajes:
        altura_parseada = float(personaje['altura'])
        if altura_parseada == altura_maxima and personaje['nombre'] != nombre_altura_maxima:
            print(f"Se ha encontrado otra altura maxima")

def encontrar_heroe_mas_bajo():
# #E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
    flag_primero = True
    for personaje in lista_personajes:
        altura_parseada = float(personaje['altura'])
        if flag_primero == True or altura_parseada < altura_minima:
            altura_minima = altura_parseada
            nombre_altura_minima = personaje['nombre']
            flag_primero = False
    print(f"La altura minima es {altura_minima}")
    for personaje in lista_personajes:
        altura_parseada = float(personaje['altura'])
        if altura_parseada == altura_minima and personaje['nombre'] != nombre_altura_minima:
            print("Se ha encontrado otra altura minima")
        
def calcular_promedio():
#F. Recorrer la lista y determinar la altura promedio de los superhéroes(PROMEDIO)
    contador_altura = 0
    acumulador_altura = 0

    for personaje in lista_personajes:
        altura_parseada = float(personaje['altura'])
        acumulador_altura += altura_parseada
        contador_altura += 1

    promedio_altura = acumulador_altura/contador_altura
    print(f"El promedio de altura es{promedio_altura}")

#G. Informar cual es el Nombre del superhéroe asociado a cada uno de los
#indicadores anteriores (MÁXIMO, MÍNIMO)

def encontrar_altura_maximo_nombre():
#MAXIMO
    flag_primero = True
    for personaje in lista_personajes:
        altura_parseada = float(personaje['altura'])
        if flag_primero == True or altura_parseada > altura_maxima:
            altura_maxima = altura_parseada
            nombre_altura_maxima = personaje['nombre']
            flag_primero = False
    print(f"altura maxima: {altura_maxima} y corresponde a {nombre_altura_maxima} ")

    #calcular si hay otra altura maxima
    for personaje in lista_personajes:
        altura_parseada = float(personaje['altura'])
        if altura_parseada == altura_maxima and personaje['nombre'] != nombre_altura_maxima:
            print(f"Se ha encontrado otra altura maxima y corresponde a {personaje['nombre']}")

def encontrar_altura_minima_nombre():
# #MINIMO
    flag_primero = True
    for personaje in lista_personajes:
        altura_parseada = float(personaje['altura'])
        if flag_primero == True or altura_parseada < altura_minima:
            altura_minima = altura_parseada
            nombre_altura_minima = personaje['nombre']
            flag_primero = False
    print(f"La altura minima es {altura_minima} y corresponde a {nombre_altura_minima}")
    for personaje in lista_personajes:
        altura_parseada = float(personaje['altura'])
        if altura_parseada == altura_minima and personaje['nombre'] != nombre_altura_minima:
            print(f"Se ha encontrado otra altura minima y corresponde a {personaje['nombre']}")

def encontrar_superheroe_mas_pesado():
#H. Calcular e informar cual es el superhéroe más y menos pesado.
#MAS PESADO 
    flag_primero = True
    for personaje in lista_personajes:
        peso_parseado = float(personaje['peso'])
        if flag_primero == True or peso_parseado > peso_maximo:
            peso_maximo = peso_parseado
            nombre_peso_maximo = personaje['nombre']
            flag_primero = False
    print(f"El peso maximo es {peso_maximo} y corresponde a {nombre_peso_maximo}")
    for personaje in lista_personajes:
        peso_parseado = float(personaje['peso'])
        if peso_parseado == peso_maximo and personaje['nombre'] != nombre_peso_maximo:
            print(f"Se ha encontrado otro peso maximo")

def encontrar_superheroe_menos_pesado():
#MENOS PESADO
    flag_primero = True
    for personaje in lista_personajes:
        peso_parseado = float(personaje['peso'])
        if flag_primero == True or peso_parseado < peso_minimo:
            peso_minimo = peso_parseado
            nombre_peso_minimo = personaje['nombre']
            flag_primero = False
    print(f"El peso minimo es {peso_minimo} y corresponde a {nombre_peso_minimo}")
    for personaje in lista_personajes:
        peso_parseado = float(personaje['peso'])
        if peso_parseado == peso_minimo and personaje['nombre'] != nombre_peso_minimo:
            print(f"Se ha encontrado otro peso minimo")


menu = ['1.Mostrar nombre de cada superheroe', 
        '2.Mostrar nombre de cada superheore con su altura',
        '3.Mostrar superheroe mas alto',
        '4.Mostrar superheroe mas bajo',
        '5.Calcular altura promedio de los superheroes',
        '6.Mostrar altura maxima con nombre', 
        '7.Mostrar altura minima con nombre', 
        '8.Mostrar superheroe mas pesado',
        '9.Mostrar superheroe menos pesado',
        '10.Salir']

while True:
    for opcion in menu:
        print(opcion)
    opcion = int(input("Ingrese una opcion"))
    match opcion:
        case 1:
            imprimir_nombre_superheroe()
        case 2:
            imprimir_nombre_altura()
        case 3:
            encontrar_heroe_mas_alto()
        case 4:
            encontrar_heroe_mas_bajo()
        case 5:
            calcular_promedio()
        case 6:
            encontrar_altura_maximo_nombre()
        case 7:
            encontrar_altura_minima_nombre()
        case 8:
            encontrar_superheroe_mas_pesado()
        case 9:
            encontrar_superheroe_menos_pesado()
        case 10:
            break