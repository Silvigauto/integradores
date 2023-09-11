from os import system
system('cls')
from funciones_01 import *

menu = ['1.nombre superheroe masculino', 
        '2.nombre superheroe femenino', 
        '3.nombre superheroe mas alto masc', 
        '4.nombre superheroe mas alto fem',
        '5.nombre superheroe mas bajo masc',
        '6.nombre superheroe mas bajo fem ',
        '7.promedio altura masc',
        '8.promedio altura fem',
        '9.cuantos superheroes tiene cada tipo de color de ojos',
        '10.cuantos superheroes tien cada de tipo de color de pelo',
        '11.cuantos superheroes tienen cada tipo de inteligencia',
        '12.agrupar superheroes por color de ojos',
        '13.agrupar superheroes por color de pelo',
        '14.agrupar superheroes por tipo de inteligencia',
        '15.Salir']

while True:
    for opcion in menu:
        print(opcion)
    respuesta = int(input("Elija una opcion"))
    match respuesta:
        case 1:
            imprimir_nombre_superheroe(lista_personajes, 'M')
        case 2:
            imprimir_nombre_superheroe(lista_personajes, 'F')
        case 3:
            encontrar_altura_superheroe(lista_personajes, 'M', 'maxima')
        case 4:
            encontrar_altura_superheroe(lista_personajes, 'F', 'maxima')
        case 5:
            encontrar_altura_superheroe(lista_personajes, 'M', 'minima')
        case 6:
            encontrar_altura_superheroe(lista_personajes, 'F', 'minima')
        case 7:
            calcular_promedio_altura(lista_personajes, 'M')
        case 8:
            calcular_promedio_altura(lista_personajes, 'F')
        case 9:
            contar_superheroe_caracteristica(lista_personajes, 'color_ojos')
        case 10:
            contar_superheroe_caracteristica(lista_personajes, 'color_pelo')
        case 11:
            contar_superheroe_caracteristica(lista_personajes, 'inteligencia')
        case 12:
            listar_por_tipo(lista_personajes, 'color_ojos')
        case 13:
            listar_por_tipo(lista_personajes, 'color_pelo')
        case 14:
            listar_por_tipo(lista_personajes, 'inteligencia')
        case 15:
            break
        

