from os import system
system('cls')

from data_stark import lista_personajes

def extraer_iniciales(nombre_heroe:str):
    '''
    parametros: recibe un string que representa el nombre del heroe
    brief:  en base al string recibido formatea el nombre y 
            los convierte en solo iniciales
    return: retorna las inciales del heroe
    '''
    if nombre_heroe == '':
        print('N/A')
    else:
        nombre_heroe = nombre_heroe.replace('the ', '')
        nombre_heroe = nombre_heroe.replace('-', ' ')
        nombre_limpio = nombre_heroe.split(' ')
        lista_iniciales = []
        for nombre in nombre_limpio:
            lista_iniciales.append(nombre[0].capitalize())
        nombre_formateado = '.'.join(lista_iniciales)
        return nombre_formateado

def definir_iniciales_nombre(heroe:dict):
    '''
    parametros: recibe un diccionario que representa todo el heroe
    brief: utiliza las iniciales de 'extraer_iniciales'
            y agrega una clave al diciconario con las iniciales
    return: deuelve true si se pudo agregar la nueva clave y false en caso que no
    '''
    if type(heroe) == dict and 'nombre' in heroe:
        iniciales = extraer_iniciales(heroe['nombre'])
        heroe['iniciales'] = iniciales
        return True
    else:
        return False

def agregar_inciales_nombre(lista:list):
    '''
    parametros:recibe la lista de superheroes
    brief: recorre la lista y en base a la funcion 'definir_iniciales_nombre' 
    devuelve true o false
    return: devuelve true si se pudo recorrer la lista exitosamente agregando las iniciales y false en caso contrario
    '''
    if type(lista) == list and len(lista) > 0:
        for heroe in lista:
            iniciales = definir_iniciales_nombre(heroe)
            if iniciales == False:
                print('El origen de datos no contiene el formato correcto')
                finalizacion = False
                break
            else:
                finalizacion = True
    else:
        finalizacion = False
    return finalizacion



def stark_imprimir_nombres_con_iniciales(lista:list):
    '''
    parametros: recibe la lista de heroes
    brief: recorre la lista y usa 'agregar_iniciales_nombre' para acceder a la nueva clave con las iniciales
            e imprimir el nombre formateado
    return: no retorna nada
    '''
    if type(lista) == list and len(lista) > 0:
        for heroe in lista:
            agregar_inciales_nombre(lista)
            print(f"* {heroe['nombre']} ({heroe['iniciales']})")


def generar_codigo_heroe(id_heroe: int, genero_heroe:str):
    '''
    parameters: recibe el id_heroe-->entero, genero_heroe-->str que sea F M o NB
    brief: en base a los parametros recibidos genera un codigo de maximo 10 caracteres con el siguiente formato
            F-00000001
    return: retorna el codigo si se pudo hacer y 'N/A' si no paso las validaciones
    '''
    if type(id_heroe) == int and genero_heroe != '' and (genero_heroe == 'M' or genero_heroe == 'F' or genero_heroe == 'NB'):
        id_heroe = str(id_heroe)
        if genero_heroe == 'NB':
            id_heroe = id_heroe.zfill(7)
        else:
            id_heroe = id_heroe.zfill(8)
        codigo_heroe = f'{genero_heroe}-{id_heroe}'
        return codigo_heroe
    else:
        return 'N/A'


def agregar_codigo_heroe(heroe:dict, id_heroe:int):
    '''
    parameters: recibe un diccionario que representa el heroe y un numero entero que representa el id
    brief: utiliza 'generar_codigo_heroe' para generar el codigo, pasando por validaciones
    return: retorna true si pudo pasar las validaciones y generar el codigo y false en caso contrario
    '''
    codigo_heroe = generar_codigo_heroe(id_heroe, 'F')
    if len(heroe) > 0 and len(codigo_heroe) == 10:     
        heroe['codigo_heroe'] = codigo_heroe
        return True
    else:
        return False


def stark_generar_codigos_heroes(lista:list):
    '''
    parameters: recibe la lista de personajes
    brief: recorre la lista y asigna un id a cada heroe en base a su posicion utilizando 'agregar_codigo_heroe'
    return: no retorna nada, solo imprime la cantidad de codigos generados, el primero y el ultimo
    '''
    contador = 0
    bandera_codigo = False
    if len(lista) != 0:
        for heroe in lista:
            if type(heroe) == dict and 'genero' in heroe:
                id_heroe = (lista.index(heroe))+1
                agregar_codigo_heroe(heroe, id_heroe)
                contador += 1  
                bandera_codigo = True
            else:
                print('el origen de datos no contiene el formato correcto')
        if bandera_codigo == True:
            print(f"Se generaron {contador} codigos")
            print(f"El codigo del primer heroe es {lista[0]['codigo_heroe']}")
            print(f"El codigo del último heroe es {lista[contador-1]['codigo_heroe']}")
    else:
        print('el origen de datos no contiene el formato correcto')


def sanitizar_entero (numero_str:str):
    '''
    parameters: un string que representa un numero
    brief: quita los espacios en blanco, analiza el string recibido y retorna un valor en cada caso
    return: devuelve el numero entero, 
        -1 si no es numero, 
        -2 si es negativo y 
        -3 si es cualquier otra cosa(0 o vacio). 
    '''
    numero_str = numero_str.strip()
    if not numero_str or numero_str == '0':
        return -3
    
    if not numero_str.isdigit():
        if '-' in numero_str[0]:
            return -2
        elif '.' in numero_str :
            numero = int(float(numero_str))
            return numero
        else:
            return -1
    
    else:
        numero = int(float(numero_str))
        return numero



def sanitizar_flotante (numero_str:str):
    '''
    parameters: un string que representa un numero
    brief: quita los espacios en blanco, analiza el string recibido y retorna un valor en cada caso
    return:devuelve el numero flotante, 
            -1 si no es numero, 
            -2 si es negativo y 
            -3 si es cualquier otra cosa(0 o vacio). 
    '''
    numero_str = numero_str.strip()
    if not numero_str or numero_str == '0':
        return -3
    
    if not numero_str.isdigit():
        if '-' in numero_str[0]:
            return -2
        elif '.' in numero_str :
            numero = float(numero_str)
            return numero
        else:
            return -1
    
    else:
        numero = float(numero_str)
        return numero


def sanitizar_string(valor_str: str, valor_por_defecto='-'):
    '''
    parameters: valor_str --> string y valor_por_defecto --> string opcional
    brief:analiza el valor_str y retorna su valor(sin /) en minusculas o un numero en caso que no sea un string
    return: retorna valor_por_defecto en lower() si valor_str esta vacio
            retorna valor_str en lower y si tiene una / la reemplaza por un espacio
            retorna 'n/a' si valor_str no es todo alfabetico      
    '''
    valor_str = valor_str.strip()

    if valor_str == '' and len(valor_por_defecto) > 0:
        return valor_por_defecto.lower()
    
    if '/' in valor_str:
        valor_str = valor_str.replace('/', ' ')

    if valor_str.isalpha():
        return valor_str
    
    if not valor_str.isalpha():
        if ' ' in valor_str:
            return valor_str.lower()
        else:
            return 'N/A'
    

def sanitizar_dato(heroe:dict, clave:str, tipo_dato:str):
    '''
    parameters: heroe-->representa un heroe en la lista, clave: altura/peso, tipo_dato--> tipo de dato a sanitizar
    brief: sanitiza el dato pasado por parametro
    return: devuelve True si se pudo realizar y false en caso contrario
    '''
    tipo_dato = tipo_dato.lower()
    if tipo_dato == 'string' or tipo_dato == 'entero' or tipo_dato == 'flotante':
        if clave in heroe:
            if tipo_dato == 'flotante':
                dato = sanitizar_flotante(heroe[clave])
                if type(dato) == float:
                    return True
                
            elif tipo_dato == 'entero':
                dato = sanitizar_entero(heroe[clave])
                if type(dato) == int:
                    return True
            else:
                dato = sanitizar_string(heroe[clave])
                if type(dato) == str:
                    return True
        else:
            print('La clave especificada no existe en el héroe')
            return False
    else:
        print('Error, tipo de dato no reconocido')
        return False


def stark_normalizar_datos(lista:list):
    if len(lista)>0:
        for heroe in lista:
            altura = sanitizar_dato(heroe, 'altura', 'flotante')  
            peso = sanitizar_dato(heroe, 'peso', 'flotante')
            color_ojos = sanitizar_dato(heroe, 'color_ojos', 'string')
            color_pelo = sanitizar_dato(heroe, 'color_pelo', 'string')
            fuerza = sanitizar_dato(heroe, 'fuerza', 'entero')
            inteligencia = sanitizar_dato(heroe, 'inteligencia', 'string')
            if altura == True and peso == True and color_ojos == True and color_pelo == True and fuerza == True and inteligencia == True:
                print('datos del heroe normalizados')
        
    else:
        print('error, lista de heroes vacia')


def generar_inidices_nombres(lista:list):
    '''
    parameters: recibe la lista de heroes
    brief: recorre la lista y genera otra lista con cada elemnto de todos los nombres de los heroes
    return: retorna la nueva lista con los elementos de cada nombre de los heroes
    '''
    if len(lista) > 0:
        lista_elementos_nombres = []
        for heroe in lista:
            if type(heroe) == dict and 'nombre' in heroe:
                elementos_nombre = heroe['nombre'].split(' ')
                for elemento in elementos_nombre:
                    lista_elementos_nombres.append(elemento)
        return lista_elementos_nombres
    else:
        print('el origen de datos no contiene el formato correcto')


def stark_imprimir_indice_nombre(lista:list):
    lista_elementos_nombres = generar_inidices_nombres(lista)
    lista_nombres_con_guion = '-'.join(lista_elementos_nombres)
    print(lista_nombres_con_guion)


def convertir_cm_a_mtrs(valor_cm:float):
    if type(valor_cm) == float and valor_cm > 0:
        valor_mts = valor_cm / 100
        return valor_mts
    else:
        return -1


def generar_separador(patron:str, largo:int, imprimir = True):
    '''
    parameters: patron--> lo que se va a imprimir(*), largo-> cuantas veces se imprimira, imprimir-> True/False
    brief: genera un separador de acuerdo al caracter y el largo
    return: devuelve n/a en caso de no pasar las validaciones (patron 1-2 caracteres max/largo tipo int)
            si imprimir == True -->  imprime y retorna
            si imprimir == False --> solo retorna
    '''
    if len(patron) > 0 and len(patron) < 3:
        if type(largo) == int and largo > 0 and largo < 236:
            separador = ''
            for i in range(largo):
                separador += patron
        else: 
            return 'N/A'
    else:
        return 'N/A'

    if imprimir == True:
        print(separador)
        return separador
    else:
        return separador


def generar_encabezado(titulo:str):
    '''
    parameters: titulo --> un string a imprimir
    brief: imprime el titulo recibido por parametro en mayuscula y entre separadores usando 
    la funcion 'generar_separador'
    return: no retorna nada, solo imprime
    '''
    separador = generar_separador('*', 100, False)
    encabezado = titulo.upper()
    print(f"{separador}\n{encabezado}\n{separador}")


def imprimir_ficha_heroe(heroe:dict):
    '''
    parameters: recibe el heroe sobre el cual realizara la ficha
    brief: formatea los datos para realizar una ficha, utilizando tambien 'generar_encabezado' para los titulos
        de cada seccion, 'extraer_iniciales' y 'generar_codigo_heroe'
    return: no retorna, solo imprime
    '''
    generar_encabezado('principal')
    nombre = heroe['nombre']
    iniciales = extraer_iniciales(nombre)
    identidad_secreta = heroe['identidad']
    consultora = heroe['empresa']
    codigo_heroe = generar_codigo_heroe(3, heroe['genero'])
    print(f'NOMBRE DEL HEROE: {nombre} {iniciales}\nIDENTIDAD SECRETA: {identidad_secreta}\nCONSULTORA: {consultora}\nCÓDIGO DE HÉROE: {codigo_heroe}')

    generar_encabezado('fisico') 
    altura_float = float(heroe['altura'])
    altura = convertir_cm_a_mtrs(altura_float)
    peso = heroe['peso']
    fuerza = heroe['fuerza']
    print(f'ALTURA: {altura:0.2}mts\nPESO: {peso:0.2}kg\nFUERZA: {fuerza}N')

    generar_encabezado('señas particulares')
    color_ojos = heroe['color_ojos']
    color_pelo = heroe['color_pelo']
    print(f'COLOR DE OJOS: {color_ojos}\nCOLOR DE PELO: {color_pelo}')


def stark_navegar_fichas(lista:list):
    '''
    paramters: recibe la lista de heroes
    brief: imprime la primera ficha y luego en base a las opciones imprime la del heroe anterior o posterior
    return: no retorna nada, solo imprime
    '''
    posicion = 0
    imprimir_ficha_heroe(lista[posicion])
    
    seguir = True
    while seguir:
        opcion = input(f'Ingrese una opcion:\n1.Ir a la izquierda\n2.Ir a la derecha\nS.Salir').lower()
        match opcion:
            case '1':
                if posicion == 0:
                    posicion = 23
                else:
                    posicion -= 1
                imprimir_ficha_heroe(lista[posicion])
            case '2':
                if posicion == 23:
                    posicion = 0
                else:
                    posicion += 1
                imprimir_ficha_heroe(lista[posicion])
            case 's':
                seguir = False
    print('saliste del menu')



def imprimir_menu():
    '''
    paramters: no recibe parametros
    brief: imprime el menu de opciones
    return: no retorna nada
    '''
    lista_opciones = [  '1.Imprimir la lista de nombres junto con sus iniciales',
                        '2.Generar codigos de heroes',
                        '3.Normalizar datos',
                        '4.Imprimir indice de nombres',
                        '5.Navegar fichas',
                        'S.Salir']
    for opcion in lista_opciones:
        print(opcion)




def stark_menu_prinicipal():
    '''
    parameters: no recibe parametros
    brief: imprime el menu usando 'imprimir_menu()' y pide una respuesta al usuario
    return: retorna la respuesta del usuario
    '''
    imprimir_menu()
    respuesta = input('Ingrese una opcion')
    return respuesta

'''
6.3. Crear la función 'stark_marvel_app_3' la cual recibirá como parámetro:
● lista_heroes: la lista de personajes
La función se encargará de la ejecución principal de nuestro programa.
Utilizar if/elif o match según prefiera (match solo para los que cuentan con

python 3.10+).
Debe informar por consola en caso de seleccionar una opción incorrecta y
volver a pedir el dato al usuario.
Reutilizar las funciones con prefijo 'stark_' donde crea correspondiente.
'''