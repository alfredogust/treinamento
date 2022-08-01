from random import randint


class Bichinho():
    def __init__(self, nome, fome, saude, idade):
        self.setNome(nome)
        self.setFome(fome)
        self.setSaude(saude)
        self.setIdade(idade)
def setNome(self, nome):
    self.nome = nome
def setFome(self, fome):
    self.fome = fome
def setSaude(self, saude):
    self.saude = saude
def setIdade(self, idade):
    self.idade = idade
def getNome(self):
    return self.nome
def getFome(self):
    return self.fome
def getSaude(self):
    return self.saude
def getIdade(self):
    return self.idade
def humor(self):
    return self.getFome() * self.getSaude()


def alimenta(self, quantidade):
    if (quantidade >= 0) and (quantidade <= 100):
        self.fome -= self.fome * (quantidade /100.0)
def brincar(self, quantidade):
    if (quantidade >= 0) and (quantidade <= 100):
        self.saude += self.saude * (quantidade / 100)
def str(self):
    return ("Nome: "  + str(self.getNome()) + ", Fome: " + str(self.getFome()) + ", Saude: " + str(self.getSaude()) + ", Idade: " + str(self.getIdade()))

a = Bichinho("Cachorro", randint(0,10),randint(0,10),5)
b = Bichinho("Gato", randint(0,10),randint(0,10),5)
c = Bichinho("Coelho", randint(0,10),randint(0,10),5)
fazenda = []
fazenda.append(a)
fazenda.append(b)
fazenda.append(c)

while True:
    print(":::: FAZENDA ::::")
    print("1. Alimentar todos os bichos")
    print("2. Brincar com todos os bichos")
    print("3. Ouvir todos os bichos")
    print("4. Sair")
    op = int(input())

if (op == 1):
    alimento = int(input("Alimentar todos com: "))
    for i in range(3):
        fazenda[i].alimenta(alimento)
elif(op ==2):
        brinquedo = int(input("Brincar todos com: "))
        for i in range(3):
            fazenda[i].brincar(brinquedo)
elif(op == 3):
    for i in range(3):
        print(fazenda[i].getNome() + ": " + str(fazenda[i].humor()))
elif(op == 4):
       ...
