meses = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
    "agosto", "setembro", "outubro", "novembro", "dezembro"
]

data = input("informe a data (dd/mm/aaaa): ")

print(
    data.split("/")[0], "de", meses[(int(data.split("/")[1]) - 1)], "de",
    data.split("/")[2])
'''

dia, mês, ano = input('Data (dd/mm/aaaa): ').split('/')
meses = ['janeiro','fevereiro','março','abril',
         'maio','junho','julho','agosto','setembro',
         'outubro','novembro','dezembro']
print ('Você nasce em:')
print ('%s de %s de %s' %(dia, meses[int(mês) - 1], ano))
'''
