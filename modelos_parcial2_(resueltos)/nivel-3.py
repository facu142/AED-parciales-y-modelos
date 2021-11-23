# TODO: 1 - Determinar la cantidad de palabras que contienen 'll' más de una vez.
"""
bandera_l = False
bandera_ll = False
cantidad_palabras_ll = 0

texto = input('Ingrese un texto: ')

for car in texto:

    if car != ' ' and car != '.':
        if bandera_l and car in 'Ll':
            bandera_ll = True
        elif car in 'Ll':
            bandera_l = True
        else:
            bandera_l = False
    else:
        if bandera_ll:
            cantidad_palabras_ll += 1
        bandera_l = False
        bandera_ll = False

print(f'Cantidad de palabras con mas de un "ll" {cantidad_palabras_ll}')

"""

"""
texto = input('Ingrese el texto: ')

for car in texto:
    if car != ' ' and car != '.':
        
        

    else:

"""

# TODO: 2 - Determinar la cantidad de palabras que comienzan con 'le' y terminan en 'to'.


"""
cantidad_letras_palabra = 0
primera_letra_l = False
segunda_letra_e = False
letra_t = True
cant_palabras_le_to = 0

texto = input('Ingrese el texto: ')

for car in texto:
    if car != ' ' and car != '.':

        cantidad_letras_palabra += 1

        if car == 'l' and cantidad_letras_palabra == 1:
            primera_letra_l = True
        elif car == 'e' and cantidad_letras_palabra == 2:
            segunda_letra_e = True

        if letra_t and car == 'o':
            termina_to = True
        elif car == 't':
            letra_t = True
        else:
            letra_t = False
            termina_to = False

    else:
        if primera_letra_l and segunda_letra_e and termina_to:
            cant_palabras_le_to += 1

        primera_letra_l = False
        segunda_letra_e = False
        termina_to = False
        letra_t = False
        cantidad_letras_palabra = 0

print(f"cantidad de palabras 'le'...'to': {cant_palabras_le_to}")
"""

# TODO: 3 - Determinar la cantidad de palabras que terminan con 'io' y tienen más de 3 letras.


"""
termina_io = False
letra_i = False
cantidad_letras_palabra = 0
texto = input('Ingrese el texto: ').lower()
cantidad_palabras_io_3_letras = 0

for car in texto:
    if car != ' ' and car != '.':
        cantidad_letras_palabra += 1

        if letra_i and car == 'o':
            termina_io = True
        elif car == 'i':
            letra_i = True
        else:
            letra_i = False
            termina_io = False
    else:
        if termina_io and cantidad_letras_palabra > 3:
            cantidad_palabras_io_3_letras += 1
        cantidad_letras_palabra = 0
        letra_i = False
        termina_io = False

print(f'Cantidad palabras de mas de 3 letras y termian en io: {cantidad_palabras_io_3_letras}')

"""

# TODO: 7 - Determinar cuantas palabras incluyeron '10' después de la mitad.

"""
posicion_10 = 0
cant_palabras = 0
cant_letras_palabra = 0
letra_1 = False
cant_palabras_10_desp_mitad = 0

texto = input('Ingrese el texto: ')

for car in texto:
    if car != ' ' and car != '.':
        cant_letras_palabra += 1

        if car == '1':
            letra_1 = True
        elif car == '0' and letra_1:
            posicion_10 = cant_letras_palabra
            letra_1 = False
        else:
            letra_1 = False

    else:
        cant_palabras += 1
        if 0 < posicion_10 and (cant_letras_palabra // 2) <= posicion_10:
            cant_palabras_10_desp_mitad += 1

        letra_1 = False
        posicion_10 = 0
        cant_letras_palabra = 0


print(f'Palabras con 10 despues de la mitad: {cant_palabras_10_desp_mitad} ')
"""



