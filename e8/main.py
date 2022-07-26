palavra = input("Digite uma palavra: ")
if str(palavra) == str(palavra)[::-1]:
    print("Palindromo")
else:
    print("Não é um Palindromo")
