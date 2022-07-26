string1 = "Brasil Hexa 2006"
string2 = "Brasil! Hexa 2006!"

tamanho_str_1 = len(string1)
tamanho_str_2 = len(string2)

comparacao_de_tamanho = 'diferentes'
comparacao_de_conteudo = 'conteudo'

if string1 == string2:
    comparacao_de_tamanho = 'iguais'
    comparacao_de_conteudo = 'igual'
elif tamanho_str_1 == tamanho_str_2:
    comparacao_de_tamanho = 'iguais'

print(string1 + " " + str(tamanho_str_1))
print(string2 + " " + str(tamanho_str_2))

print(f'As duas strings sao de tamanhos {comparacao_de_tamanho}.')
print(f'As strings possuem conteudo{comparacao_de_conteudo}')

#print(string1 + " " + str(tamanho_str_1))
#print(string2 + " " + str(tamanho_str_2))

