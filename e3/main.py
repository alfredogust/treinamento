nome = input("Digite um nome: ")

for i in range(len(nome)):
    c = nome[len(nome) - 1 - i]
    print(c.upper())