#coding: utf-8


altura  = input("Digite sua altura em metros, separa por ponto (ex: 1.60): ")
vT = (int(72.7)) * altura
r = (int(vT)) - 58  #ValueError: invalid literal for int() with base 10:
print ("Seu peso ideal seria ",r)
