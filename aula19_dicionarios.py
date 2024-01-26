#APRENDENDO DICIONÁRIOS

brasil = list()
estado = dict()

for c in range(0,3):
    estado['UF'] = str(input('UF: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
print(brasil)

for cadaestado in brasil:
    for cadavalor in cadaestado.values():
        print(cadavalor)

'''
filmes = {
'nome': 'Star Wars',
'ano': 1977,
'diretor': 'George Lucas'

}

print(filmes)
print(filmes.values())
print(filmes.keys())
print(filmes.items())

for chaves, valores in filmes.items():
    print(f'O {chaves} é {valores}. ')

print(f'O filme {filmes["nome"]} é de {filmes["ano"]}')

filmes['gênero'] = 'ficção-científica'
print(filmes.items())

for k, v in filmes.items():
    print(f'O {k} é {v}.')

del filmes['diretor']

print(filmes)
print(filmes.items())'''