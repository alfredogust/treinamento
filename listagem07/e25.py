#coding: utf-8


def gerarPerguntas():


    quantidade_positivo = 0


    status = {2 : "Suspeito(a)",
              3 : "Cúmplice",
              4 : "Cúmplice",
              5 : "Assassino"}


    lista_perguntas = ["Telefonou para a vítima?",
                       "Esteve no local do crime?",
                       "Mora perto da vítima?",
                       "Devia para a vítima?",
                       "Já trabalhou com a vítima?"]


    for index in len(lista_perguntas):
        #efetuar a pergunta.
        print (lista_perguntas[index] + " (sim ou não).")

        #Obter uma resposta.
        resposta = input("Resp.:")


        if resposta.lower() == "sim":
            #incrementar mais um.
            quantidade_positivo += 1


    if quantidade_positivo in status:

        print (status[quantidade_positivo])

    else:
        print ("Inocente")
