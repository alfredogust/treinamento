#coding: utf-8

listaChar = []
consoantes = 0
print("Informe os caracteres: \n")

for i in range(10):
  listaChar.append((input('Caracter  '+ str(i+1) + ':\n')))
  char = listaChar[i]
  if(char not in ('a', 'e', 'i', 'o', 'u')):
    consoantes += 1
print(f"O número de consoantes é: \n{consoantes}")
