Jogo
perguntarNovamente = True
game_on = True
while game_on:
    palavra_secreta = palavra()
    senha_list = [l for l in palavra_secreta]
    chances = 6
    tentativas = []
    #Esconder palavra
    for i in range(101):
        print()
    print (senha_list) #APENAS PARA TESTE
    #Começo do jogo
    while perguntarNovamente:
        print("A palavra:","_ "*len(senha_list))
        erros = 0
        desenho(erros)
        an = input("Digite uma letra(ou a palavra): ")
        if an == palavra_secreta:
            print("Parabéns você acertou!!")
            break
        elif an not in(senha_list):
            if an in(tentativas):
                print("Você já tentou essa letra!")
                continue
            else:
                print("Não há essa letra na palavra!")
                tentativas.append(an)
                erros +=1
                continue
        else:
            print("Você acertou uma letra!")
            tentativas.append(an)
            continue
    break