frase = input("Digite uma frase: ")
vogais = 0
espacos = 0

for letra in frase:
    if letra == " ":
        espacos += 1
    elif letra in "aeiou":
        vogais += 1
print("A frase tem %d vogais e %d espaços." % (vogais, espacos))