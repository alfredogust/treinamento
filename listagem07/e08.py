#coding: utf-8

import time

print('Bem vindo!')

time.sleep(0.8)
print('---------------------------------------------')
print('')

p1 = input('Digite o 1° preço: ')
p2 = input('Digite o 2° preço: ')
p3 = input('Digite o 3° preço: ')

def menor():
    if p1 < p2 and p1 < p3:
        menor = p1
    elif p2 < p1 and p2 < p3:
        menor = p2
    else:
        menor = p3
    return menor
print('O menor preço é:', menor())
