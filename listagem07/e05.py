#coding: utf-8

n1 = input('Digite sua nota: ')
n2 = input('Digite sua 2° nota: ')

nota = (n1 + n2) / 2

if nota >= 7 and nota < 10:
    print ('Você foi Aprovado!!')
elif nota >= 10:
    print ('Você foi Aprovado com Distinção!!')
else:
    print ('Infelizmente você foi reprovado')
