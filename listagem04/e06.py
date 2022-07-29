v_candidato_1 = 0
v_candidato_2 = 0
v_candidato_3 = 0
eleitores = int(input("Digite o numero de eleitores: "))
for i in range(eleitores):
    voto = input(
        "Digite o numero (1/2/3) do candidato em quem o "
        f"eleitor {i + 1} quer votar: "
    )
    if voto == "1":
        v_candidato_1 += 1
    if voto == "2":
        v_candidato_2 += 1
    if voto == "3":
        v_candidato_3 += 1

print(
    "Votação encerrada"
    f"\nCandidato 1: {v_candidato_1} voto(s)"
    f"\nCandidato 2: {v_candidato_2} voto(s)"
    f"\nCandidato 3: {v_candidato_3} voto(s)"
)
