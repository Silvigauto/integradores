from os import system
system('cls')
from data_stark import lista_personajes

def imprimir_nombre_superheroe(lista:list, genero:str):
    if genero == "M":
        for heroe in lista:
            if heroe['genero'] == 'M':
                print(heroe['nombre'])
    if genero == "F":
        for heroe in lista:
            if heroe['genero'] == 'F':
                print(heroe['nombre'])

def encontrar_altura_minima(lista:list, genero:str):
    flag_primero = True
    for heroe in lista:
        if heroe['genero'] == genero:
            altura_parseada = float(heroe['altura'])
            if flag_primero == True or altura_parseada < altura_minima :
                altura_minima = altura_parseada
                flag_primero = False
    return altura_minima

def imprimir_altura_minima(lista:list, genero:str):
    altura_minima = encontrar_altura_minima(lista, genero)
    for heroe in lista:
        altura_parseada = float(heroe['altura'])
        if altura_parseada == altura_minima:
            print(f"{heroe['nombre']}")

def encontrar_altura_maxima(lista:list, genero:str):
    flag_primero = True
    for heroe in lista:
        if heroe['genero'] == genero:
            altura_parseada = float(heroe['altura'])
            if flag_primero == True or altura_parseada > altura_maxima :
                altura_maxima = altura_parseada
                flag_primero = False
    return altura_maxima

def imprimir_altura_maxima(lista:list, genero:str):
    altura_maxima = encontrar_altura_maxima(lista, genero)
    for heroe in lista:
        altura_parseada = float(heroe['altura'])
        if altura_parseada == altura_maxima:
            print(f"{heroe['nombre']}")

def encontrar_altura_superheroe(lista:list, genero:str, caracteristica:str):
    if caracteristica == 'minima':
        imprimir_altura_minima(lista, genero)
    if caracteristica == 'maxima':
        imprimir_altura_maxima(lista, genero)

def calcular_promedio_altura(lista:list, genero:str):
    contador_altura = 0
    acumulador_altura = 0
    for heroe in lista:
        if heroe['genero'] == genero: 
            altura_parseada = float(heroe['altura'])
            contador_altura += 1
            acumulador_altura += altura_parseada
    promedio = acumulador_altura/contador_altura
    print(f'Altura promedio: {promedio}')

def setear_superheroes_caracteristica(lista:list, caracteristica:str):
    lista_caracteristica = []
    for heroe in lista:
        lista_caracteristica.append(heroe[caracteristica])
    lista_caracteristica_seteada = set(lista_caracteristica)
    return lista_caracteristica_seteada

def contar_superheroe_caracteristica(lista:list, caracteristica:str):
    lista_caracteristica_seteada = setear_superheroes_caracteristica(lista, caracteristica)
    print(caracteristica)
    for tipo in lista_caracteristica_seteada:
        contador = 0
        for heroe in lista:
            if heroe[caracteristica] == tipo:
                if tipo == '':
                    tipo = 'no tiene'
                    contador += 1
                else:
                    contador += 1               
        print(f'{tipo} | {contador}')

def listar_por_tipo(lista:list, caracteristica:str):
    lista_tipo = setear_superheroes_caracteristica(lista, caracteristica)
    print(f"***{caracteristica}***")
    for tipo in lista_tipo:
        if tipo == '':
            print('----No tiene----')
        else:
            print(f'----{tipo}----')
        for heroe in lista:
            if heroe[caracteristica] == tipo:
                    print(heroe['nombre'])
        
