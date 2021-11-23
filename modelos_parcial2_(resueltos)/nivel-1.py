# Codigo


# TODO: 1 - Determinar la cantidad de palabras del texto.
"""
cont_palabras = 0
texto = input('Ingrese el texto: ')

for car in texto:
    if car != ' ' and car != '.':
        pass
    else:
        cont_palabras += 1
print(f'La cantidad de palabras es {cont_palabras}')

"""

# TODO: 2 - Determinar el promedio de letras por palabra.
"""
# inicializacion de contadores, acumuladores y banderas

contador_letras = 0
contador_palabras = 0
texto = input('Ingrese el texto ')
for caracter in texto:
    if caracter != ' ' and caracter != '.':
        contador_letras += 1
    else:
        contador_palabras += 1
promedio = contador_letras/contador_palabras
print('Promedio: ',promedio)

"""
# TODO: 3 - Determinar promedio de vocales por palabra
"""
texto = input("Ingrese un texto:")
texto = texto.lower()
cant_vocales = 0
cant_palabras = 0
for caracter in texto:
    if caracter == " " or caracter == ".":
        cant_palabras += 1
    else:
        if caracter in "aeiouáéíóú":
            cant_vocales += 1

promedio = cant_vocales / cant_palabras
print(promedio)

"""
# TODO: 4 - Determinar el promedio de consonantes por palabra.
"""
cont_palabra = 0
cont_consonantes_palabra = 0
cont_letras = 0
prom_consonantes = 0

texto = input('Ingrese el texto: ')

for car in texto:
    if car != ' ' and car != '.':

        cont_letras += 1

        if car in 'qwrtypsdfghjklñzxcvbnmQWRTYPSDFGHJKLÑZXCVBNM':
            cont_consonantes_palabra += 1
    else:
        cont_palabra += 1

prom_consonantes = cont_consonantes_palabra / cont_palabra


print(f'El promedio de consonantes por palabra es {prom_consonantes} ')

"""
#TODO: 5 - Determinar la cantidad de palabras que incluyeron alguna letra e.
"""
contador_palabras = 0
contador_palabras_e = 0
bandera_e = False

texto = input('Ingrese el texto: ')
texto = texto.lower()

for caracter in texto:
    if caracter != ' ' and caracter != '.':
        if caracter == 'e':
            bandera_e = True
    else:
        contador_palabras += 1
        if bandera_e:
            contador_palabras_e += 1
        bandera_e = False
print('Cantidad de palabras con alguna letra E: ', contador_palabras_e)
"""

# TODO: 6-Porcentaje de palabras que tuvieron alguna consonante
"""

texto = input("Ingrese un texto:")
contador_palabras = 0
texto = texto.lower()
palabras_con = 0
tiene_con = False

for caracter in texto:
    if caracter != " " and caracter != ".":
        if caracter in "qwrtypsdfghjklñzxcvbnmQWRTYPSDFGHJKLÑZXCVBNM":
            tiene_con = True
    else:
        contador_palabras += 1
        if tiene_con:
            palabras_con += 1
        tiene_con = False
porcentaje = (palabras_con * 100) / contador_palabras
print("Porcentaje:", porcentaje)

"""
