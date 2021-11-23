"""
Turno 3 - Enunciado 4 (T3E4) (Copie el enunciado siguiente como comentario al inicio de su archivo principal de código
fuente)

Una empresa de construcción, mantenimiento  y reparaciones mantiene información sobre los distintos servicios que debe
realizar. Por cada servicio se registran los datos siguientes: número de identificación del servicio (un número entero),
descripción del servicio (una cadena), importe a facturar por el servicio, tipo de servicio (un valor entre 0 y 24
incluidos, por ejemplo: 0: pintura, 1: ampliación, etc.) y forma de pago (un número entero entre 0 y 4 incluidos, para
indicar (por ejemplo): 0: contado, 1: tarjeta de crédito, etc.) Se pide definir un tipo registro Servicio con los
campos que se indicaron, y un programa completo con menú de opciones para hacer lo siguiente:

1- Cargar los datos de n registros de tipo Servicio en un arreglo de registros (cargue n por teclado). Valide los campos
que sea necesario. Puede cargar los datos manualmente, o puede generarlos aleatoriamente (pero si hace carga manual,
TODA la carga debe ser manual, y si la hace automática entonces TODA debe ser automática).  El arreglo debe crearse de
forma que siempre quede ordenado de menor a mayor, según el número de identificación de los servicios y para hacer
esto debe aplicar el algoritmo de inserción ordenada con búsqueda binaria. Se considerará directamente incorrecta la
solución basada en cargar el arreglo completo y ordenarlo al final, o aplicar el algoritmo de inserción ordenada pero
con búsqueda secuencial.

2- Mostrar el arreglo creado en el punto 1, a razón de  un registro por línea, pero muestre solo los registros cuyo tipo
 de servicio sea mayor o igual al valor tip que se carga por teclado.

3- Usando el arreglo creado en el punto 1, determine la cantidad de servicios de cada posible tipo por cada posible
forma pago (o sea, 25 * 5 contadores en una matriz de conteo). Muestre solo los resultados que sean diferentes de cero
 pero mayores que un valor d que se carga por teclado.

4- A partir del arreglo, crear un archivo de registros en el cual se copien los datos de todos los servicios cuyo
importe a facturar sea menor a un valor x que se carga por teclado.

5- Mostrar el archivo creado en el punto anterior, a razón de un registro por línea en la pantalla. Agregar al final
del listado una línea adicional, que indique el promedio de los importes a facturar de todos los registros que se
mostraron.


"""

# Facundo Montenegro 90329 1k3

import os
import pickle
import registro

NOMBRE_ARCHIVO = 'servicios.bin'


def mostrar_menu():
	print('******* MENU OPCIONES *******')
	print('1- Cargar servicios en arreglo')
	print('2- Mostrar servicios de tipo mayor o igual a..')
	print('3- Mostrar cantidad por tipo y forma de pago')
	print('4- Crear archivo')
	print('5- Mostrar datos del archivo')
	print('6- Salir')


def add_in_order_numero(servicios, nuevo_servicio):
	izq = 0
	der = len(servicios) - 1
	pos = len(servicios)

	while izq <= der:
		c = (izq + der) // 2
		if servicios[c].numero == nuevo_servicio.numero:
			pos = c
			break
		if nuevo_servicio.numero < servicios[c].numero:
			der = c - 1
		else:
			izq = c + 1

	if izq > der:
		pos = izq

	servicios[pos:pos] = [nuevo_servicio]


def cargar_servicios(n):
	servicios = []

	for i in range(n):
		nuevo_servicio = registro.crear_registro_aleatorio()
		add_in_order_numero(servicios, nuevo_servicio)

	return servicios


def mostrar_servicios(servicios, tipo_minimo):
	print('\n**** Listado de servicios ****\n')
	for servicio in servicios:
		if servicio.tipo >= tipo_minimo:
			print(servicio)
	print()


def crear_matriz(filas, columnas):
	return [[0] * columnas for f in range(filas)]


def contar_por_tipo_y_pago(mat, servicios):
	for servicio in servicios:
		mat[servicio.tipo][servicio.forma_pago] += 1


def mostrar_matriz(mat, minimo):
	print('\n******* CANTIDAD POR TIPO Y FORMA DE PAGO *******\n')

	for f in range(len(mat)):
		for c in range(len(mat[0])):
			if mat[f][c] != 0 and mat[f][c] > minimo:
				print(f'TIPO:{f} | FORMA DE PAGO: {c} => {mat[f][c]}')

	print()


def crear_archivo(nombre_archivo, servicios, importe_maximo):
	cont = 0
	archivo = open(nombre_archivo, 'wb')
	for servicio in servicios:
		if servicio.importe < importe_maximo:
			cont += 1
			pickle.dump(servicio, archivo)

	print(f'\nSe ha creado el archivo {nombre_archivo} con {cont} registros\n')
	archivo.close()


def mostrar_archivo(nombre_archivo):
	if os.path.exists(nombre_archivo):
		archivo = open(nombre_archivo, 'rb')
		tam = os.path.getsize(nombre_archivo)
		cont_servicios = 0
		acumulador_importe = 0

		print('***** Listado de servicios del archivo *****')

		while archivo.tell() < tam:
			servicio = pickle.load(archivo)
			print(servicio)
			acumulador_importe += servicio.importe
			cont_servicios += 1

		print(f'\nPromedio importe: {round((acumulador_importe / cont_servicios), 2)}\n')

		archivo.close()
	else:
		print(f'\nNo existe el archivo {nombre_archivo}\n')


def principal():
	servicios = []

	mostrar_menu()
	opc = int(input('Ingrese la opcion: '))

	while opc != 6:
		if opc == 1:

			n = int(input('Cantidad servicios a generar: '))

			servicios = cargar_servicios(n)
			print(f'\nSe han cargado los {n} servicios\n')

		elif opc == 2:
			if len(servicios) != 0:
				tip = int(input('Mostrar servicios de tipo mayor o igual a: '))
				mostrar_servicios(servicios, tip)
			else:
				print('\nDebe cargar los servicios primero\n')
		elif opc == 3:
			if len(servicios) != 0:
				mat = crear_matriz(filas=25, columnas=5)
				contar_por_tipo_y_pago(mat, servicios)
				d = int(input('Valor minimo a mostrar: '))
				mostrar_matriz(mat, minimo=d)
			else:
				print('\nDebe cargar los servicios primero\n')
		elif opc == 4:
			if len(servicios) != 0:
				x = int(input('Ingrese el importe maximo: '))

				crear_archivo(NOMBRE_ARCHIVO, servicios, importe_maximo=x)
			else:
				print('\nDebe cargar los servicios primero\n')
		elif opc == 5:
			mostrar_archivo(NOMBRE_ARCHIVO)
		else:
			print('Ingrese una opcion correcta')

		mostrar_menu()
		opc = int(input('Ingrese la opcion: '))


if __name__ == '__main__':
	principal()
