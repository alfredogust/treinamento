import random

def lancar_dados():
    return random.randint(2, 12)


entrada = ""
jogada = 0
ponto = 0
print ("digite  \"sair\" para sair (sem aspas)\naperte <enter> para rolar os dados: ")

while (entrada!="sair"):
    jogada += 1
    print("Jogada {}").format(jogada)
    entrada = raw_input("Esperando acao: ")

    if entrada == "sair":
        print("Saindo do jogo... Tchau")
    else:
        if jogada>1:
            print("Seu ponto e {}".format(ponto))
        valor = lancar_dados()
        print("O valor do dado e {}\n\n".format(valor))
        if jogada == 1:
            if valor == 7 or valor == 11:
                print("Voce tirou um natural e ganhou, PARABENS")
                exit()
            elif valor == 2 or valor == 3 or valor == 12:
                print("Voce tirou um craps e perdeu, melhor sorte da proxima vez")
                exit()
            else:
                ponto = valor
        else:
            if valor == 7:
                print("Voce tirou um 7 antes de repetir seu ponto, voce perdeu")
                exit()
            elif ponto == valor:
                print("Voce conseguiu repetir seu ponto e ganhou, Parabens")
                exit()
