salario = 1.000
ano = 1995
ano_atual = int(input("Digite em que ano estamos: "))
aumento = 1.5 / 100  # ? 1.5%

while ano < ano_atual:
    ano += 1
    salario *= 1 + aumento
    aumento *= 2

print(f"O salario em {ano} é de R$ {salario:.2f}")
