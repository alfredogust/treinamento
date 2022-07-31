#coding: utf-8


print("1- File Duplo\n2- Alcatra\n3- Picanha\n\n")
tipo = int(input("Digite o tipo: "))
quantidade = int(input("Digite a quantidade comprada: "))
resposta = int(input("A compra será realizada com cartao Tabajara? 1p/ SIM - 2p/ NAO: "))

if tipo == 1:
    nome = "File Duplo"
    if quantidade <= 5:
        preco = quantidade * 4.90
    else:
        preco = quantidade * 5.80

if tipo == 2:
    nome = "Alcatra"
    if quantidade <= 5:
        preco = quantidade * 5.90
    else:
        preco = quantidade * 6.80

if tipo == 3:
    nome = "Picanha"
    if quantidade <= 5:
        preco = quantidade * 6.90
    else:
        preco = quantidade * 7.80

if resposta == 1:
    r = "SIM"

    desconto = ((preco * 5) /100)
    total = preco - desconto
else:
    r = "NAO"
    total = preco

print("\n***************************CUPOM FISCAL**************************************")
print("* Carne.......................................................... %s " %nome)
print("* Quantidade..................................................... %d KG " %quantidade)
print("* Preço......................................................... %2.f R$ " %preco)
print("* Cartao Tabajara................................................ %s " %r)
print("* Total com desconto............................................ %2.f R$ " %total)
print("******************************************************************************")
