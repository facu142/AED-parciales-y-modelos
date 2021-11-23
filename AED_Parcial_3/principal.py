"""
Turno 3 - Enunciado 1 (T3E1)

Una revista científica desea un programa para procesar los datos de los trabajos que le son enviados para su publicación.
Por cada Trabajo se tienen los siguientes datos: número de identificación del trabajo, título del trabajo, cantidad de
páginas, cantidad de autores, código de área temática del trabajo (un valor entre 0 y 9 ambos incluidos, de la forma
0: Inteligencia artificial, 1: Informática 2: Lenguajes de programación, etc.). Se desea almacenar la información
referida a los n trabajos en un arreglo de registros de tipo Trabajo (definir el tipo Trabajo y cargar n por teclado).

Se pide desarrollar un programa en Python controlado por un menú de opciones y que posea como mínimo dos módulos, que
permita gestionar las siguientes tareas:

1- Cargar el arreglo pedido con los datos de los n trabajos. Valide que el tipo de área temática de los trabajos sea
un valor entre 0 y 9 (ambos incluidos). Puede hacer la carga en forma manual,
 o puede generar los datos en forma automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea
 . Pero al menos una debe programar.

2- Mostrar todos los datos de los trabajos, en un listado ordenado de menor a mayor según el número de identificación
del trabajo.  Al final del listado mostrar una línea adicional, en la que se indique la cantidad promedio de páginas de
todas las obras que se mostraron.

3- Usando el arreglo creado en el punto 1, determine la cantidad de trabajos por cada área temática
(o sea, 10 contadores). Muestre sólo los resultados que correspondan a las áreas cuyo código de área temática sea un
número impar.

4- Determinar el trabajo que posea la mayor cantidad de autores y mostrar sus datos. Si existe más de un registro con
esa mayor cantidad de autores, mostrar sólo uno.

5- Determinar si existe un trabajo cuyo número de identificación sea igual a x, siendo x un valor que se carga por
teclado. Si existe mostrar todos sus datos, junto con el importe total a pagar para su publicación, sabiendo que por
cada página debe abonar 350 pesos. Si no existe, informar con un mensaje.


"""
__author__ = "Facundo Montenegro_90329[1k3]"

import registro


def mostrar_menu():
    print('1 - Cargar trabajos (aleatorios)')
    print('2 - Mostrar trabajos')
    print('3 - Mostrar cantidad de trabajos por area ')
    print('4 - Mostrar trabajo con mayor cantidad de autores')
    print('5 - Buscar trabajo por ID y calcular importe')
    print('6 - Salir')


def mostrar_trabajos(trabajos):
    print(registro.FORMATO.format('ID', '|', 'Titulo', '|', 'Paginas', '|', 'Autores', '|', 'Cod. Area'))
    for trabajo in trabajos:
        print(trabajo)


def ordenar_trabajos_por_id(trabajos):
    n = len(trabajos)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if trabajos[j].n_id < trabajos[i].n_id:
                trabajos[i], trabajos[j] = trabajos[j], trabajos[i]


def mostrar_cantidad_por_area(trabajos):
    vec_contador = [0] * 10

    for trabajo in trabajos:
        vec_contador[trabajo.codigo_area] += 1

    for i in range(len(vec_contador)):
        print(f'Area {i}: {vec_contador[i]}')


def obtener_trabajo_con_mas_autores(trabajos):
    trabajo_con_mas_autores = trabajos[0]

    for trabajo in trabajos:
        if trabajo.autores > trabajo_con_mas_autores.autores:
            trabajo_con_mas_autores = trabajo

    return trabajo_con_mas_autores


def buscar_trabajo_por_id(trabajos, n_id):
    for trabajo in trabajos:
        if trabajo.n_id == n_id:
            return trabajo


def principal():
    trabajos = []
    ordenado = False

    mostrar_menu()
    opc = int(input('Ingrese la opcion: '))

    while opc != 6:
        if opc == 1:
            n = int(input('Cantidad de trabajos: '))
            while n < 1:
                n = int(input('Ingrese un numero positivo: '))

            for i in range(n):
                nuevo_trabajo = registro.crear_trabajo_aleatorio()
                trabajos.append(nuevo_trabajo)
            print(f'Se han creado {n} trabajos! \n')

        elif opc == 2:

            if not ordenado:
                ordenar_trabajos_por_id(trabajos)
                ordenado = True
            mostrar_trabajos(trabajos)

        elif opc == 3:
            mostrar_cantidad_por_area(trabajos)
        elif opc == 4:

            trabajo_con_mas_autores = obtener_trabajo_con_mas_autores(trabajos)
            print('_' * 25, 'Tabajo con mas autores', '_' * 25)
            print(registro.FORMATO.format('ID', '|', 'Titulo', '|', 'Paginas', '|', 'Autores', '|', 'Cod. Area'))
            print(trabajo_con_mas_autores)

        elif opc == 5:

            x = int(input('ID a buscar: '))
            trabajo_encontrado = buscar_trabajo_por_id(trabajos, n_id=x)

            if trabajo_encontrado is not None:
                print(f'Se ha encontrado un trabajo con ID={x}')
                print(registro.FORMATO.format('ID', '|', 'Titulo', '|', 'Paginas', '|', 'Autores', '|', 'Cod. Area'))
                print(trabajo_encontrado)
                print(f'El importe a abonar es ${trabajo_encontrado.paginas * 350} ')
            else:
                print(f'No se ha encontrado trabajo con ID={x}')

        else:
            print('Ingrese una opcion correcta')

        mostrar_menu()
        opc = int(input('Ingrese la opcion: '))


if __name__ == '__main__':
    principal()
