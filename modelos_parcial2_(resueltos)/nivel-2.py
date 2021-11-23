# TODO:  1 - Determinar la cantidad de palabras que comienzan con la primera letra de todo el texto.
'''

cantidad_letras = 0
cantidad_palabras_prim_letra = 0
contiene_primera_letra = False
cantidad_palabras = 0
primera_letra = None
cantidad_letras_palabra = 0

texto = input("Ingrese un texto: ")

for car in texto:
    if car != ' ' and car != '.':
        cantidad_letras += 1
        cantidad_letras_palabra += 1

        if car == primera_letra and cantidad_letras_palabra == 1:
            contiene_primera_letra = True
        if cantidad_letras == 1:
            primera_letra = car

    else:
        if contiene_primera_letra:
            cantidad_palabras_prim_letra += 1
        contiene_primera_letra = False
        cantidad_letras_palabra = 0

print(f'La cantidad de palabras que comienzan con la primera letra del texto es {cantidad_palabras_prim_letra}')
'''
# TODO: 2 - Determinar la porcentaje de palabras que incluyeron la primera letra de todo el texto.
'''
contador_letras = 0
contador_palabras = 0
contador_palabras_incluye = 0
primera_letra_texto = None
incluye_primera_letra = False

texto = input('Ingrese el texto: ')

for caracter in texto:
    if caracter != ' ' and caracter != '.':
        contador_letras += 1
        if contador_letras == 1:
            primera_letra_texto = caracter

        if caracter == primera_letra_texto:
            incluye_primera_letra = True

    else:
        contador_palabras += 1
        if incluye_primera_letra:
            contador_palabras_incluye += 1
        incluye_primera_letra = False

porcentaje = contador_palabras_incluye * 100 / contador_palabras
print(f'Porcentaje: {porcentaje}')
'''
# TODO: 3 - Determinar la cantidad de palabras que terminan con la primera letra de todo el texto.

"""
cont_letras_palabra = 0
cant_letras_total = 0
ultima_letra_palabra = None
primera_letra_texto = None
cont_palabras_terminan_primera = 0
texto = input('Ingrese el texto: ')

for car in texto:
    if car != ' ' and car != ' ':
        cont_letras_palabra += 1
        cant_letras_total += 1

        if cant_letras_total == 1:
            primera_letra_texto = car

        ultima_letra_palabra = car

    else:
        if ultima_letra_palabra == primera_letra_texto:
            cont_palabras_terminan_primera += 1

print(f'La cantidad de letras que terminan con la letra {ultima_letra_palabra} es {cont_palabras_terminan_primera}')

"""

# TODO: 4 - Determinar la cantidad de palabras que incluyeron la silaba 'de'.

"""
tiene_d = False
tiene_de = False
cantidad_palabras_de = 0

texto = input("Ingrese un texto:")

for car in texto:
    if car != ' ' and car!= '.':
        if 'd' == car:
            tiene_d = True
        elif tiene_d and 'e' == car:
            tiene_de = True
        else:
            tiene_d = False
    else:
        if tiene_de:
            cantidad_palabras_de += 1
        tiene_de = False
        tiene_d = False

print(f'La cantidad de palabras con de es {cantidad_palabras_de}')

"""
# TODO: 5 - Determinar la cantidad de palabras que presentan la letra 'rr'.


"""
tiene_rr = False
cantidad_palabras_rr = 0
tiene_r = False

texto = input("Ingrese un texto: ")

for car in texto:
    if car != " " and car != ".":

        if tiene_r and car == "r":
            tiene_rr = True
        elif car == "r":
            tiene_r = True
        else:
            tiene_r = False
    else:
        if tiene_rr:
            cantidad_palabras_rr += 1
        tiene_rr = False
        tiene_r = False

print( f'La cantidad de palabras con rr es  {cantidad_palabras_rr} ')
"""

# TODO:  6 - Determinar la cantidad de palabras que comienzan con 'la'.


"""
comienzan_la = False
palabras_la = 0
cantidad_letras_palabra = 0
comienza_l = False
segunda_letra_a = False

texto = input("Ingrese un texto:")
texto = texto.lower()
for car in texto:
    if car != " " and car != ".":
        cantidad_letras_palabra += 1

        if cantidad_letras_palabra == 1 and car == "l":
            comienza_l = True
        if cantidad_letras_palabra == 2 and car == 'a':
            segunda_letra_a = True

    else:
        cantidad_letras_palabra = 0
        if comienza_l and segunda_letra_a:
            palabras_la += 1
        comienzan_l = False
        segunda_letra_a = False
print(f'La cantidad de palabras que comienzan con la es {palabras_la}')

"""

# TODO:  7 - Determinar el porcentaje de palabras que contienen 'si' y 'no'.

"""
def calcular_porcentaje(subtotal, total):
    porcentaje = (subtotal * 100) / total
    return porcentaje


letra_s = False
tiene_si = False
letra_n = False
tiene_no = False

cant_palabras = 0
cant_palabras_si_no = 0

texto = input('Ingrese el texto: ')

for car in texto:
    if car != ' ' and car != '.':
        if letra_s and car == 'i':
            tiene_si = True
        elif car == 's':
            letra_s = True
        else:
            letra_s = False

        if letra_n and car == 'o':
            tiene_no = True
        elif car == 'n':
            letra_n = True
        else:
            letra_n = False
    else:
        cant_palabras += 1
        if tiene_si and tiene_no:
            cant_palabras_si_no += 1

        tiene_si = False
        tiene_no = False
        letra_n = False
        letra_s = False

porcentaje_palabras_si_no = calcular_porcentaje(cant_palabras_si_no,cant_palabras)

print(f'Porcentaje de palabras que incluyen "si" y "no" : {porcentaje_palabras_si_no}%')
"""

# TODO: 8 - Determinar la cantidad de palabras que contienen 'h' pero dentro de la palabra es decir no puede ser
#  ni la primera ni la última letra de la palabra.

"""
contiene_h = False
cantidad_letras_palabra = 0
no_empieza_con_h = False
ultima_letra_palabra = None
cantidad_palabras_sin_h = 0

texto = input('Ingrese el texto: ')

for car in texto:
    if car != ' ' and car != '.':
        cantidad_letras_palabra += 1

        if cantidad_letras_palabra == 1 and car != 'h':
            no_empieza_con_h = True

        ultima_letra_palabra = car

        if car in 'Hh':
            contiene_h = True

    else:
        if no_empieza_con_h and ultima_letra_palabra != 'h' and contiene_h:
            cantidad_palabras_sin_h += 1

        no_empieza_con_h = False
        cantidad_letras_palabra = 0
        contiene_h = False

print(f'Cantidad de palabras que contienen h y no empiezan o terminan con h: {cantidad_palabras_sin_h}')
"""

# TODO: 9 - Determinar la cantidad de palabras que incluyeron la sílaba 'en' 2 veces.

"""
contiene_en = 0
cantidad_palabras_en_2veces = 0
contiene_e = False

texto = input('Ingrese el texto: ')

for car in texto:
    if car != ' ' and car != '.':

        if car == 'e':
            contiene_e = True
        elif contiene_e and car == 'n':
            contiene_en += 1
        else:
            contiene_e = False

    else:
        if contiene_en == 2:
            cantidad_palabras_en_2veces += 1
        contiene_en = 0
        contiene_e = False

print(f'La cantidad de palabras que incluyen la silaba "en" es  {cantidad_palabras_en_2veces}')
"""
# TODO: 10 - Determinar la cantidad de palabras que comienzan con la letra 'll'.

"""
cont_letras_palabra = 0
primera_letra_l = False
segunda_letra_l = False
cont_palabras_ll = 0

texto = input('Ingrese el texto: ')

for car in texto:
    if car != ' ' and car != '.':
        cont_letras_palabra += 1
        if cont_letras_palabra == 1 and car == 'l':
            primera_letra_l = True
        if cont_letras_palabra == 2 and car == 'l':
            segunda_letra_l = True

    else:
        if primera_letra_l and segunda_letra_l:
            cont_palabras_ll += 1

        cont_letras_palabra = 0
        primera_letra_l = False
        segunda_letra_l = False

print(f'Cantidad palabras que empiezan con "ll": {cont_palabras_ll} ')
"""

# TODO: 11 - Determinar la cantidad de palanbras que comienzan con 'la'.

"""

cont_letras_palabra = 0
primera_letra_l = False
segunda_letra_a = False
cont_palabras_la = 0

texto = input('Ingrese el texto: ')

for car in texto:
    if car != ' ' and car != '.':
        cont_letras_palabra += 1
        if cont_letras_palabra == 1 and car == 'l':
            primera_letra_l = True
        if cont_letras_palabra == 2 and car == 'a':
            segunda_letra_a = True

    else:
        if primera_letra_l and segunda_letra_a:
            cont_palabras_la += 1

        cont_letras_palabra = 0
        primera_letra_l = False
        segunda_letra_a = False

print(f'Cantidad palabras que empiezan con "la": {cont_palabras_la} ')
"""

# TODO: 12 - Determinar la posición de la palabra más larga del texto.

"""
posicion_larga = None
cantidad_letras_palabra = 0
cantidad_palabras = 0
cantidad_letras_palabra_larga = None
texto = input('Ingrese el texto: ')

for car in texto:
    if car != ' ' and car != '.':
        cantidad_letras_palabra += 1
    else:
        cantidad_palabras += 1
        if cantidad_palabras == 1:
            posicion_larga = 1
            cantidad_letras_palabra_larga = cantidad_letras_palabra

        if cantidad_letras_palabra > cantidad_letras_palabra_larga:
            posicion_larga = cantidad_palabras
            cantidad_letras_palabra_larga = cantidad_letras_palabra

        cantidad_letras_palabra = 0

print(f'Posicion: {posicion_larga} cantidad: {cantidad_letras_palabra_larga}')
"""

# TODO: 13 - Determinar la posición de la palabra más corta del texto.

"""
cont_letras_palabra_mas_corta= 0
posicion_palabra_mas_corta = 0
cont_letras_palabra = 0
cont_palabras = 0


texto = input('Ingrese el texto: ')

for car in texto:
    if car != ' ' and car != '.':
        cont_letras_palabra += 1

    else:
        cont_palabras += 1
        if cont_palabras == 1:
            posicion_palabra_mas_corta = cont_palabras
            cont_letras_palabra_mas_corta = cont_letras_palabra

        if cont_letras_palabra < cont_letras_palabra_mas_corta:
            posicion_palabra_mas_corta = cont_palabras
            cont_letras_palabra_mas_corta = cont_letras_palabra

        cont_letras_palabra = 0

print(f' Posicion palabra mas corta: {posicion_palabra_mas_corta} con {cont_letras_palabra_mas_corta} letras ')

"""

# TODO: 14 - Determinar la cantidad de palabras con vocales y consonantes alternadas.

"""

def es_vocal(letra):
    return letra in 'AEIOUaeiouÁÉÍOUáéíóú'


def es_consonantes(letra):
    return letra in 'QWRTYPSDFGHJKLÑZXCVBNMqwrtypsdfghjklñzxcvbnm'


cant_letras_palabra = 0
cant_palabras = 0
alternadas = True
bandera_vocal = False
bandera_consonantes = False
cont_palabras_alternadas = 0

texto = input('Ingrese el texto: ')

for car in texto:

    if car != ' ' and car != '.':
        cant_letras_palabra += 1

        if bandera_vocal and es_vocal(car) or bandera_consonantes and es_consonantes(car):
            alternadas = False
        elif es_vocal(car):
            bandera_vocal = True
            bandera_consonantes = False
        elif es_consonantes(car):
            bandera_consonantes = True
            bandera_vocal = False

    else:
        cant_palabras += 1
        if alternadas:
            cont_palabras_alternadas += 1

        bandera_vocal = False
        bandera_consonantes = False
        alternadas = True

print('Punto 14: ', cont_palabras_alternadas)
"""

# TODO: 15 - Determinar el porcentaje de las palabras que finalizaron en "on" sobre el total de palabras del texto.

"""
palabras_finalizo_on = 0
cantidad_palabras = 0
bandera_o = False
bandera_on = False
cantidad_letras = 0

texto = input('Ingrese el texto: ')

for car in texto:
    if car != ' ' and car != '.':
        bandera_on = False
        if car == 'o' or car == 'ó':
            bandera_o = True
        else:
            if bandera_o and car == 'n':
                bandera_on = True
            bandera_o = False
    else:
        if bandera_on:
            palabras_finalizo_on += 1
        bandera_on = bandera_o = False

print(f'cantidad de palabras que finalizaron con on {palabras_finalizo_on}')

"""

# TODO: 15 - Determinar el porcentaje de las palabras que finalizaron en "an" sobre el total de palabras del texto.

"""


def calcular_porcentaje(subtotal, total):
    return (subtotal * 100) / total

bandera_a = False
bandera_an = False
cantidad_an = 0
cantidad_palabras = 0

texto = input('Ingrese el texto: ')

for car in texto:
    if car != ' ' and car != '.':

        bandera_an = False

        if car in 'aA':
            bandera_a = True
        elif bandera_a and car in 'nN':
            bandera_an = True
        else:
            bandera_a = False
    else:
        cantidad_palabras += 1
        if bandera_an:
            cantidad_an += 1
        bandera_an = False
        bandera_a = False

porcentaje = calcular_porcentaje(cantidad_an, cantidad_palabras)

print(f'Porcentaje: {porcentaje}%')
"""
