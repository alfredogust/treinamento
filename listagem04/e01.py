num = int(input("Digite um número inteiro: "))

i = 2
res = False

while i < num and not res:
    x = num % i
if x == 0:
    res = True
    i += 1

if res:
    print("não primo")
else:
    print("primo")
