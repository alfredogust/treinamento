#coding: utf-8


eleitores = int(input("Digite o número total de eleitores: "))
candidatoa = 0
candidatob = 0
candidatoc = 0
votantes = 0


while (votantes < eleitores):
    voto = int(input("Digite 1 para votar no candidato A, 2 para o candidato B e 3 para o candidato C"))
if (voto == 1):
    candidatoa = candidatoa + 1
elif (voto == 2):
    candidatob = candidatob + 1
elif (voto == 3):
    candidatoc = candidatoc + 1
    votantes = votantes + 1


print("O candidato A teve", candidatoa, "votos.")
print("O candidato B teve", candidatob, "votos.")
print("O candidato C teve", candidatoc, "votos.")
