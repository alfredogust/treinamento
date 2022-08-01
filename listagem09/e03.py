class Retangulo:
    def __init__(self,comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def mudar_valor_comprimento(self,novo_comprimento):
        self.comprimento = novo_comprimento

    def mudar_valor_largura(self, nova_largura):
        self.largura = nova_largura

    def retornar_valor_lados(self):
        print(f'{self.comprimento}cm, {self.largura}cm')

    def calcular_area(self):
        area = self.largura * self.comprimento
        print(f'{area}m quadrados')
        return area


    def calcular_perimetro(self):
        perimetro = 2*self.largura + 2*self.comprimento

        return perimetro


r1 = Retangulo(4,10)

print(r1.__dict__)
r1.retornar_valor_lados()
r1.calcular_area()
r1.calcular_perimetro()

r1.mudar_valor_comprimento(3)
r1.mudar_valor_largura(12)
print(r1.__dict__)
r1.retornar_valor_lados()
r1.calcular_area()
r1.calcular_perimetro()

x = float(input('selecione o comprimento do local:' ))
y = float(input('selecione a largura do local:' ))

local = Retangulo(x,y)

print (f'serão necessários {local.calcular_area()}m quadrado(s) de piso e {local.calcular_perimetro()}m de rodapés para suprir o local')
