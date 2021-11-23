"""

Facundo Montenegro 90329 -1k3

Turno 03 – Enunciado 02 [T3E2]:

Desarrolle un programa completo en Python, controlado por menú de opciones, que incluya las siguientes opciones:

1.)    Ingrese las tres notas obtenidas por un alumno en sus trabajos prácticos. Calcular y mostrar el promedio.
Además, mostrar su calificación final, teniendo en cuenta que si el promedio es menor a 4 su calificación es
"Insuficiente"; si el promedio es un valor mayor o igual a 4 pero menor a 7 su calificación es "Aprobado",
y si el promedio es mayor o igual a 7 entonces su calificación es “Sobresaliente”.

2.)    Ingresar una secuencia de números, a razón de un número por vuelta de ciclo. La carga de dicha secuencia
finaliza cuando se ingresa un cero. Se deberá determinar y mostrar la cantidad de números comprendidos entre 10 y 30
inclusive, y además el valor promedio de los números comprendidos en el intervalo ya mencionado.

3.)    Terminar el programa.


"""

print('Menu de opciones')
print('1- Notas Trabajo practico')
print('2- Secuencia de numeros ')
print('3- Salir')

opc = int(input('Ingrese una opcion: '))

while opc != 3:
    if opc == 1:

        calificacion = None

        nota_1 = int(input('Ingrese la nota #1: '))
        nota_2 = int(input('Ingrese la nota #2: '))
        nota_3 = int(input('Ingrese la nota #3: '))

        promedio = (nota_1 + nota_2 + nota_3) / 3

        if promedio < 4:
            calificacion = 'Insuficiente'
        elif promedio >= 4 and promedio < 7:
            calificacion = 'Aprobado'
        elif promedio >= 7:
            calificacion = 'Sobresaliente'

        print(f'El promedio es {round(promedio,2)}')
        print(f'Su calificacion es {calificacion}')

    elif opc == 2:

        numero = int(input('Ingrese un numero :  '))

        cont_numeros_intervalo = 0
        cont_numeros_cargados = 0
        sumatoria_numeros_intervalo = 0

        while numero != 0:

            cont_numeros_cargados += 1

            if numero <= 30 and numero >= 10:
                sumatoria_numeros_intervalo += numero
                cont_numeros_intervalo += 1

            numero = int(input('Ingrese un numero (con 0 corta) :  '))

        promedio_intervalo = sumatoria_numeros_intervalo / cont_numeros_intervalo

        print(f'Cantidad de numeros cargados: {cont_numeros_cargados}')
        print(f'Cantidad de numeros entre 10 y 30 inclusive: {cont_numeros_intervalo}')
        print(f'El valor promedio de los numeros en el intervalo es {promedio_intervalo}')

    else:
        print('Por favor, ingrese una opcion valida')

    print('Menu de opciones')
    print('1- Notas Trabajo practico')
    print('2- Secuencia de numeros ')
    print('3- Salir  ')

    opc = int(input('Ingrese una opcion: '))

print('Fin del programa')
