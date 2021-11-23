import os
import pickle
import registro

NOMBRE_ARCHIVO = 'medicamentos.bin'


def mostrar_menu():
	print('1- Cargar medicamentos')
	print('2- Mostra vector')
	print('3- Crear archivo')
	print('4- Mostrar archivo')
	print('5- ')
	print('6- ')
	print('7- Salir')


def add_in_order_numero(medicamentos, nuevo_medicamento):
	izq = 0
	der = len(medicamentos) - 1
	pos = len(medicamentos)

	while izq <= der:
		c = (izq + der) // 2
		if medicamentos[c].numero == nuevo_medicamento.numero:
			pos = c
			break
		if medicamentos[c].numero < nuevo_medicamento.numero:
			der = c - 1
		else:
			izq = c + 1

	if izq < der:
		pos = izq

	medicamentos[pos:pos] = [nuevo_medicamento]


def cargar_vector(n):
	medicamentos = []
	for i in range(n):
		nuevo_medicamento = registro.crear_registro_aleatorio()
		add_in_order_numero(medicamentos, nuevo_medicamento)

	return medicamentos


def mostrar_vector(medicamentos):
	print('\nListado de medicamentos\n')
	for medicamento in medicamentos:
		print(medicamento)
	print()


def crear_archivo(nombre_archivo, medicamentos):
	importe_max = int(input('Importe maximo a facturar: '))
	archivo = open(nombre_archivo, 'wb')

	for medicamento in medicamentos:
		if medicamento.tipo == 1 or medicamento.tipo == 0 and medicamento.importe < importe_max:
			pickle.dump(medicamento, archivo)

	archivo.close()


def mostrar_archivo(nombre_archivo):
	if os.path.exists(nombre_archivo):
		archivo = open(nombre_archivo, 'rb')
		tam = os.path.getsize(nombre_archivo)

		print('\nLista de medicamentos en el archivo\n')
		while archivo.tell() < tam:
			medicamento = pickle.load(archivo)
			print(medicamento)

		archivo.close()
	else:
		print(f'no existe el archivo con el nombre {nombre_archivo}')


def principal():
	medicamentos = []

	mostrar_menu()
	opc = int(input('Ingrese la opcion: '))

	while opc != 7:
		if opc == 1:
			n = int(input('Cantidad de medicamtos a crear: '))
			medicamentos = cargar_vector(n)
		elif opc == 2:
			mostrar_vector(medicamentos)
		elif opc == 3:
			crear_archivo(NOMBRE_ARCHIVO, medicamentos)
		elif opc == 4:
			mostrar_archivo(NOMBRE_ARCHIVO)
		elif opc == 5:
			pass
		elif opc == 6:
			pass
		else:
			print('Ingrese una opcion correcta')

		mostrar_menu()
		opc = int(input('Ingrese la opcion: '))


if __name__ == '__main__':
	principal()
