"""
Segundo Parcial de AED - Enunciado General.

Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en una variable de tipo
cadena de caracteres. El texto finaliza con ‘.’ y se supone que el usuario cargará el punto para indicar el final del
texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe incluir
al menos una función simple con parámetros y retorno de resultado, debe procesar el texto caracter a caracter (a
razón de uno por vuelta de ciclo), y debe hacer lo siguiente sin usar un menú de opciones:

b.)      Ítems a desarrollar.

Turno 03 – Enunciado 04 [T3E4]

Determinar la cantidad de palabras que tienen dos o más vocales pero no contienen una "s" (minúscula o mayúscula).
Por ejemplo, en el texto “Los estudiantes rinden el parcial.” hay 2 palabras que cumplen con la condición ("rinden" y
"parcial").

Determinar el porcentaje de palabras (con respecto al total de palabras de texto) que finalizan en una consonante (
minúscula o mayúscula). Por ejemplo, en el texto: "El cielo es celeste." hay 4 palabras en total, y sólo 2 ("El" y
"es") tienen una consonante como última letra. Por lo tanto, el porcentaje pedido es del 50%.

Determinar cuántas palabras contienen (pero sin empezar con él) al último caracter de la primera palabra del texto (
en minúscula o en mayúscula si es letra). Por ejemplo, en el texto: "Bienvenidos son los alumnos." la primera palabra
finaliza con 's' y hay entonces 2 palabras que contienen a esa letra sin comenzar con ella ("los" y "alumnos"). La
palabra "son" contiene una "s", pero comienza con ella, y por lo tanto no debe ser contada. Por "caracteres",
se entiende "cualquier tipo de símbolo, sea este un dígito, una letra, o cualquier otro que pueda aparecer".

Determinar la cantidad de palabras que contienen la expresión "mi" (con cualquiera de sus letras en minúscula o en
mayúscula) pero de forma que la palabra COMIENCE con esa expresión. Por ejemplo en el texto: “Mis amigos son miles.“,
las palabras "Mis" y "miles" cumplen con la condición. Notar que "amigos" contiene "mi" pero no al inicio y por lo
tanto no debe ser contada.

"""


def calcular_porcentaje(subtotal, total):
    porcentaje = (subtotal * 100) / total
    return porcentaje


def es_vocal(caracter):
    return caracter in 'AEIOUaeiouÁÉÍÓÚáéíóú'


def es_consonante(caracter):
    return caracter in 'qwrtypsdfghjklñzxcvbnmQWRTYPSDFGHJKLÑZXCVBNM'


def principal():
    tiene_s = False
    cont_vocales_palabra = 0
    cont_palabras_2_vocales_sin_s = 0
    cont_palabras_finalizan_consonante = 0

    finaliza_consonante = False
    cont_palabras = 0

    ultimo_caracter = None
    ultima_letra_primera_palabra = None
    cont_letras_palabra = 0
    contiene_ultimo_car_primera_palabra = False
    cont_palabras_contienen_ultimo_car = 0

    primera_letra_m = False
    segunda_letra_i = False
    cont_palabras_mi = 0

    texto = input('Ingrese el texto: ')
    texto.lower()

    for car in texto:
        if car != ' ' and car != '.':
            cont_letras_palabra += 1
            if es_vocal(car):
                cont_vocales_palabra += 1
            if car in 'sS':
                tiene_s = True

            if es_consonante(car):
                finaliza_consonante = True
            else:
                finaliza_consonante = False

            if cont_letras_palabra != 1 and car == ultima_letra_primera_palabra:
                contiene_ultimo_car_primera_palabra = True

            if cont_letras_palabra == 1 and car in 'mM':
                primera_letra_m = True
            if cont_letras_palabra == 2 and car in 'iI':
                segunda_letra_i = True

            ultimo_caracter = car

        else:

            cont_palabras += 1

            if cont_vocales_palabra >= 2 and not tiene_s:
                cont_palabras_2_vocales_sin_s += 1

            if finaliza_consonante:
                cont_palabras_finalizan_consonante += 1

            if cont_palabras == 1:
                ultima_letra_primera_palabra = ultimo_caracter

            if contiene_ultimo_car_primera_palabra:
                cont_palabras_contienen_ultimo_car += 1

            if primera_letra_m and segunda_letra_i:
                cont_palabras_mi += 1

            tiene_s = False
            cont_vocales_palabra = 0
            finaliza_consonante = False
            cont_letras_palabra = 0
            contiene_ultimo_car_primera_palabra = False
            primera_letra_m = False
            segunda_letra_i = False

            if car == '.':
                break

    porc_palabras_finaliza_consonante = calcular_porcentaje(cont_palabras_finalizan_consonante, cont_palabras)
    porc_palabras_finaliza_consonante = round(porc_palabras_finaliza_consonante, 2)
    print(f'1- Cantidad de palabras con dos o mas vocales y sin "s": {cont_palabras_2_vocales_sin_s}')
    print(f'2- Porcentaje de palabras que finalizan con consonante: {porc_palabras_finaliza_consonante} %')
    print(f'3- Cantidad palabras que contienen (pero sin empezar con él) "{ultima_letra_primera_palabra}": '
          f'{cont_palabras_contienen_ultimo_car} ')
    print(f'4- Cantidad de palabras que comienzan con "mi" {cont_palabras_mi} ')


if __name__ == '__main__':
    principal()
