class Carro(object):


	def __init__(self, consumo):
		self.consumo = consumo
		self.combustivel = 0

	# Define o método mover
	def mover(self,km):
		consumo = self.consumo * km
		self.combustivel -= consumo


	def gasolina(self):
		return self.combustivel


	def abastecer(self, combustivel):
		self.combustivel += combustivel


def main():
	carrinho = Carro(10)
	carrinho.abastecer(100)
	carrinho.mover(3)
	print (carrinho.gasolina())

import unittest

class TestCarro(unittest.TestCase):

	def setUp(self):
		self.carro = Carro(10)


	def test_verifica_se_abasteceu_100(self):
		self.carro.abastecer(100)
		abastece = 100
		self.assertEquals(abastece, self.carro.gasolina())

	def test_move_3_resta_70_de_gasolina(self):
		self.carro.abastecer(100)
		move = 3
		self.carro.mover(3)
		self.assertEquals(70, self.carro.gasolina())

if __name__ == '__main__':
	main()
	unittest.main()
