#print('Pode digitar seu nome com letras maiúsculas, minúsculas ou mistas.')
#nome = ("alfredo").upper()
nome = input("Digite seu nome: ").upper()
inverteNome = nome[::-1]
print('{} ---> {}'.format(nome, inverteNome))

