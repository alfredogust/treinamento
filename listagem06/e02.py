#coding: utf-8

listaNumerosReais = []
print("Informe os 10 numeros reais")

for i in range(10):
 listaNumerosReais.append(float(input('Numero '+ str(i+1) + ':\n')))
listaNumerosReais.reverse()
print(listaNumerosReais)
