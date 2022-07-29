valor_divida = float(input("Digite o valor da dívida: "))
parcelas = 1
juros = 0
print(
    "|Valor da Dívida|Valor dos Juros|Quantidade de Parcelas|Valor da Parcela|"
)
while True:
    # ? A fórmula abaixo foi encontrada usando a equação da reta
    # ? y - y0 = m * (x - x0), com y = 15, y= = 10, x = 6 e x0 = 3
    # ? y -> Percentual de juros | x -> Quantidade de parcelas
    juros = (5 / 3) * parcelas + 5
    # ? Não é uma reta perfeita pois quando x=1, y=0
    if parcelas == 1:
        juros = 0

    valor_do_juros = valor_divida * (juros / 100)
    valor_total = valor_divida + valor_do_juros
    valor_da_parcela = valor_total / parcelas
    print(
        f"|R$ {valor_total:.2f}\t"
        f"|R$ {valor_do_juros:.2f}\t"
        f"|{parcelas}\t\t\t"
        f"|R$ {valor_da_parcela:.2f}"
    )
    if parcelas == 1:
        parcelas -= 1
    parcelas += 3
    if parcelas > 12:
        break
