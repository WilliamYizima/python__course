column = ["nome","sobrenome"]

dados = ["will","yizima"]

print(list(zip(column,dados)))
print(dict(zip(column,dados)))

"""exemplo prático"""
print('\n')
colunas = ['nome','sobremnome']
dados = [
    (['will','yizima']),
    (['rafa','m']),
    (['luan','T']),
    ]

for dado in dados:
    print(dict(zip(column,dado)))

#melhorando mais ainda:
print('\n')
print([dict(zip(colunas, dado)) for dado in dados])