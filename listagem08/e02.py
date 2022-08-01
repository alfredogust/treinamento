def imprimir(valor):
    if isinstance(valor, int):
        x = 1
        while x <= valor:
            y = 1
            texto = ''
            while y <= x:
                texto += str(y) + "\t"
                y += 1
            print(texto)
            x += 1
