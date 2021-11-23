import random

letras = 'abcdefghijklmnopqrstuvwxyz'


class Servicio:
	def __init__(self, numero, descripcion, importe, tipo, forma_pago):
		self.numero = numero
		self.descripcion = descripcion
		self.importe = importe
		self.tipo = tipo
		self.forma_pago = forma_pago

	def __str__(self):
		return f'NUMERO:{self.numero}; DESCRIPCION:{self.descripcion}; IMPORTE:{self.importe}; TIPO:{self.tipo} FORMA DE PAGO:{self.forma_pago} '


def crear_registro_aleatorio():
	numero = random.randint(1, 999)
	descripcion = random.choice(letras)
	importe = round(random.uniform(1000, 10000), 2)
	tipo = random.randint(0, 24)
	forma_pago = random.randint(0, 4)

	return Servicio(numero, descripcion, importe, tipo, forma_pago)
