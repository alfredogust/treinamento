menor_20 = ['', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove']
dezenas = ['', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
centena = ['', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']

numero = int(input('Digite o numero: '))
print(f'O numero {numero} por extenso fica: ', end='')

if numero == 100:
    print('cem')
elif numero == 0:
    print('zero')
else: 
    if numero > 100:
        print(centenas[int(str(numero)[0])], end= '')
        numero = numero - int(str(numero)[0])*100
        if numero != 0:
            print(' e', end= ' ')
    if numero < 20:
        print(menor_20[numero])
        numero = 0
    elif numero >= 20:
        print(dezenas[int(str(numero)[0])], end = ' ')
        numero = numero - int(str(numero)[0])*10
    if numero != 0:
        print('e', menor_20[numero])
