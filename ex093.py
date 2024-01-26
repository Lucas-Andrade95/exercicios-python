#APROVEITAMENTO DOS JOGADORES
jogador = {
    'nome': input('Nome do Jogador: '),
    'gols': [int(input(f'Quantos gols na {c+1}ª partida? ')) for c in range(int(input(f'Quantas partidas jogou? ')))]
}
jogador['total'] = sum(jogador['gols'])

print('~' *70)
print(jogador)
print('~' *70)

for chave, valor in jogador.items():
    print(f'O campo {chave} tem o valor {valor}.')

print()
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas. ')

for indice, gols in enumerate(jogador["gols"]):
    print(f'Na {indice + 1}ª partida fez {gols} gols.')

'''
dicionario = dict()
dicionario['nome'] = str(input('Nome do Jogador: '))
gols = []
totaldegols = 0

partidas = int(input(f'Quantas partidas {dicionario["nome"]} jogou? '))

for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na {c +1}ª partida? ')))
dicionario['gols'] = gols[:]
dicionario['total'] = sum(gols)

print('~'*70)
print(dicionario)
print('~'*70)

for c, v in dicionario.items():
    print(f'O campo {c} tem o valor {v}.')
print('~'*70)
print(f'O jogador {dicionario["nome"]} jogou {partidas} partidas.')
for indice, valor in enumerate(dicionario['gols']):
    print(f'Na {indice +1}ª partida, fez {valor} gols. ')
print()
print(f'Foi um total de {dicionario["total"]} gols.')'''
