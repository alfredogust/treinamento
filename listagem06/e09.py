#coding: utf-8

vetorA = []
soma = 0


for numero in range(0, 10):
    vetorA.append(int(input("Digite um nÃºmero: ")))
    soma = soma + (vetorA[len(vetorA)-1]**2)


print("A soma dos quadrados dos elementos do vetor Ã© " + str(soma))
