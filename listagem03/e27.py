#coding: utf-8

soma = 0
n = int(input("Digite n: "))
m = 1
print("S = ", end="")
for i in range(1, n + 1):
    print(f"{i}/{m}", end="")
    if i < n and n > 1:
        print(" + ", end="")
    else:
        print(".")
    soma += i / m
    m += 2
print(f"A soma da série deu {soma:.2f}")
