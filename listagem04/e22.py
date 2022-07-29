#coding: utf-8

from sys import platform


from os import system


aluno_com_maior_acerto = ""
aluno_com_menor_acerto = ""
maior_acerto = 0
media_da_turma = 0
numero_de_alunos = 0

gabarito = {}
alunos = {}

numero_de_questoes = int(input("Digite o número de questões: "))
menor_acerto = numero_de_questoes


for i in range(1, numero_de_questoes + 1):

    resposta_atual = input(
        f"Digite a resposta correta da questão '{i}': "
    ).upper()

    gabarito["questao_" + str(i)] = resposta_atual

if platform == "win32":
    limpar = "cls"
else:
    limpar = "clear"

while True:

    system(limpar)

    aluno = input("Digite o nome do aluno (ou 0 para sair): ")
    if aluno == "0":
        system(limpar)
        break

    numero_de_alunos += 1


    alunos[aluno] = {"acertos": 0}

    for i in range(1, numero_de_questoes + 1):
        resposta_atual = input(
            f"Digite a resposta que o aluno {aluno} deu para a questão {i}: "
        ).upper()

        alunos[aluno]["questao_" + str(i)] = resposta_atual


for aluno, respostas in alunos.items():

    for questao, resposta in respostas.items():
        if questao == "acertos":
            continue

        if resposta == gabarito[questao]:
            alunos[aluno]["acertos"] += 1

    acertos = alunos[aluno]["acertos"]
    nota = 10 * acertos / numero_de_questoes
    print(
        f"O aluno {aluno} obteve {acertos} acertos dentre {numero_de_questoes}"
        f" questões e ficou com a nota {nota:.2f}"
    )

    if acertos > maior_acerto:
        maior_acerto = acertos
        aluno_com_maior_acerto = aluno
    if acertos < menor_acerto:
        menor_acerto = acertos
        aluno_com_menor_acerto = aluno

    media_da_turma += nota

media_da_turma /= numero_de_alunos
print(
    f"O aluno com o mais acertos é {aluno_com_maior_acerto}, "
    f"com {maior_acerto} acertos"
    f"\nO aluno com o menos acertos é {aluno_com_menor_acerto}, "
    f"com {menor_acerto} acertos"
    f"\nA média da turma é {media_da_turma:.2f}"
)
