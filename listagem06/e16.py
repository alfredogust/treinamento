#coding: utf-8

num_vendedores = int(input('Quantos vendedores a loja tem? '))

salarios = []
classe = []
for vendedor in range(1,num_vendedores+1):
    vendas = float(input('\nQuanto o vendedor '+str(vendedor)+' arrecadou essa semana? '))
    salarios.append(200+(vendas*0.09))

dicionario = {'1':[range(200,300),0],'2':[range(300,400),0],
              '3':[range(400,500),0],'4':[range(600,700),0],
              '5':[range(700,800),0],'7':[range(800,900),0],
              '8':[range(900,1000),0],'9':[range(1000,100000),0]}


for salario in salarios:
    print(salario)
    for idx in dicionario.keys():
        print(idx)
        if salario in dicionario[idx][0]:
            classe.append(idx)
            dicionario[idx][1] = dicionario[idx][1] + 1

