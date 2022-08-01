def valorPagamento(p, d):
    return p*1.03 + 0.001*d

c = t = 0

while True:
    p = float(input('Valor da prestação: '))
    if p == 0:
        print(f'Total: {t}. Quantidade: {c} ')
        break
    d = int(input('Dia em atraso: '))
    print(f'Valor a ser pago: {valorPagamento(p, d) :.2f}')
    print('-+-'*10)
    c += 1
    t += valorPagamento(p, d)
