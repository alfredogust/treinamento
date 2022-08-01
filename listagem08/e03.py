def soma(x,y,z):
    return (x + y + z)

def media(num):
    return num/3

def menu():
    x = int(input('Primeiro numero: '))
    y = int(input('Segundo numero : '))
    z = int(input('Terceiro numero: '))

    print('Soma: ', soma(x,y,z))
    print('Media:', media( soma(x,y,z) ))

while True:
    menu()
