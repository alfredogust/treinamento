#coding: utf-8

from math import inf

maior = -inf
menor = inf
soma = 0
contador = 0
while True:
    temperatura = float(
        input("Digite a temperatura em Kelvin. Negativa para parar: ")
    )
    if temperatura < 0:
        break

    contador += 1
    soma += temperatura
    if temperatura < menor:
        menor = temperatura
    if temperatura > maior:
        maior = temperatura

print(f"A menor temperatura foi {menor}K")
print(f"A maior temperatura foi {maior}K")
print(f"A média das temperaturas foi {soma / contador:.3f}K")
