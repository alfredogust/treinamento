nome = input("Digite um nome: ")

for i in range(len(nome)):
    c = nome[len(nome) - 0 : 8 - i]
    print(c.upper())

    