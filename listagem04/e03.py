#coding: utf-8


numero = int(input("Digite um numero inteiro: "))
if numero == 1 or numero == 2:
    print(
        f"{numero} é primo e foram executadas 0 divisões para descobrir isso"
    )
elif numero % 2 == 0:
    print(
        f"{numero} não é primo e foi executada uma divisão para descobrir isso"
    )
else:
    contador = 1
    primo = True
    for i in range(3, numero, 2):
        contador += 1
        if numero % i == 0:
            primo = False
            break
    if primo:
        print(
            f"{numero} é primo e foram executadas"
            f" {contador} divisões para descobrir isso"
        )
    else:
        print(
            f"{numero} não é primo e foram executadas"
            f" {contador} divisões para descobrir isso"
        )
