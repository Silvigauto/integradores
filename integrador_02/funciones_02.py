from os import system
system('cls')

#0
def stark_normalizar_datos(lista:list):
    if len(lista) != 0:
        flag_normalizado = False
        for heroe in lista:
            #los if separados?
            if type(heroe['altura']) != int or type(heroe['peso']) != int or heroe['fuerza'] != int:
                heroe['altura'] = float(heroe['altura'])
                heroe['peso'] = float(heroe['peso'])
                heroe['fuerza'] = float(heroe['fuerza'])
                flag_normalizado = True
        if flag_normalizado:
            print('datos normalizados')
    else:
        print('error, lista vacia')

#1.1   
def obtener_nombre(diccionario:dict):
    nombre = diccionario['nombre']
    nombre_formateado = f'Nombre: {nombre}'
    return nombre_formateado

#1.2
def imprimir_dato(string:str):
    print(string)

#1.3
def stark_imprimir_nombres_heroes(lista:list):
    if len(lista) != 0:
        for personaje in lista:
            nombre = obtener_nombre(personaje)
            imprimir_dato(nombre)
    else:
        return -1
    
#2
def obtener_nombre_y_dato(diccionario:dict, key:str):
    nombre = diccionario['nombre']
    dato = diccionario[key]
    string_formateado = f'Nombre: {nombre} | {key}: {dato}'
    return string_formateado

#3
def stark_imprimir_nombres_alturas(lista:list):
    if len(lista) != 0:
        for heroe in lista:
            nombre_y_altura = obtener_nombre_y_dato(heroe, 'altura')
            print(nombre_y_altura)
    else:
        return -1

#4.1
def calcular_max(lista:list, dato:str):
    flag_primero = True
    for heroe in lista:
        dato_parseado = float(heroe[dato])
        if flag_primero == True or dato_parseado > dato_maximo:
            dato_maximo = dato_parseado
            flag_primero = False
    for heroe in lista:
        dato_parseado = float(heroe[dato])
        if dato_maximo == dato_parseado:
            #como retornar mas de un valor sin usar lista?(caso que haya mas de un maximo)
            return heroe
        
#4.2
def calcular_min(lista:list, dato:str):
    flag_primero = True
    for heroe in lista:
        dato_parseado = float(heroe[dato])
        if flag_primero == True or dato_parseado < dato_minimo:
            dato_minimo = dato_parseado
            flag_primero = False
    for heroe in lista:
        dato_parseado = float(heroe[dato])
        if dato_minimo == dato_parseado:
            #como retornar mas de un valor sin usar lista?(caso que haya mas de un maximo)
            return heroe
        
#4.3
def calcular_max_min_dato(lista:list, tipo_calculo:str, dato:str):
    if tipo_calculo == 'maximo':
        heroe_dato = calcular_max(lista, dato)
    if tipo_calculo == 'minimo':
        heroe_dato = calcular_min(lista, dato)
    return heroe_dato

#4.4
def stark_calcular_imprimir_heroe(lista:list, tipo_calculo:str, dato:str):
    if len(lista) != 0:
        heroe = calcular_max_min_dato(lista, tipo_calculo, dato)
        imprimir_dato(obtener_nombre_y_dato(heroe, dato))

    else:
        return -1

#5.1
def sumar_dato_heroe(lista:list, dato:str):
    acumulador_dato = 0
    for heroe in lista:
        if type(heroe) == dict and len(heroe) != 0:
            dato_parseado = float(heroe[dato])
            acumulador_dato += dato_parseado
        else:
            print('diccionario vacio')
    return acumulador_dato

#5.2
def dividir(dividendo:float, divisor:float):
    if divisor != 0:
        dividendo = float(dividendo)
        divisor = float(divisor)
        division = dividendo/divisor
        return division
    else:
        return 0

#5.3
def calcular_promedio(lista:list, dato:str)->float:
    acumulador_dato = sumar_dato_heroe(lista, dato)
    contador = len(lista)
    promedio = acumulador_dato/contador
    return promedio

'''
PARA CHEQUEAR SI EL DATO EXISTE EN EL DICCIONARIO
for heroe in lista:
    if dato in heroe:
        print('existe la key')
    else:
        print('no exite')
'''

#5.4
def stark_calcular_imprimir_promedio_altura(lista:list):
    if len(lista) != 0:
        promedio_altura = calcular_promedio(lista, 'altura')
        imprimir_dato(promedio_altura)
    else:
        return -1

#6.1
def imprimir_menu():
    menu_opciones = ['1.',
                     '2.',
                     '3',
                     '4',
                     '5',
                     '6.Salir']
    for opcion in menu_opciones:
        imprimir_dato(opcion)

#6.2
def validar_entero(numero:str):
    return numero.isdigit()
    #devuelve True si TODOS los digitos son numericos
    #devuelve False si al menos un caracter no es numerico

#6.3
def stark_menu_principal():
    imprimir_menu()
    opcion_usuario = input('ingrese una opcion')
    opcion_usuario_validada = validar_entero(opcion_usuario)
    if opcion_usuario_validada:
        return int(opcion_usuario)
    else:
        return -1



