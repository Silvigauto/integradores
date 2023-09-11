
from funciones_02 import *

def stark_marvel_app(lista):
    while True:
        opcion_usuario = stark_menu_principal()
        while opcion_usuario < 1 or opcion_usuario > 5:
            print('opcion incorrecta')
            opcion_usuario = stark_menu_principal()
        match opcion_usuario:
            case 1:
                stark_imprimir_nombres_heroes(lista)
            case 2:
                stark_imprimir_nombres_alturas(lista)
            case 3:
                stark_calcular_imprimir_heroe(lista, 'maximo', 'altura')
            case 4:
                stark_calcular_imprimir_promedio_altura(lista)
            case 5:
                break
            