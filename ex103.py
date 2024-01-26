def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols no campeonato.')


nome = input('Nome do jogador: ').strip()
gols = input('Gols: ').strip()

if not nome and not gols:
    ficha()
elif not gols:
    ficha(nome=nome)
elif not nome:
    ficha(gols=gols)
else:
    ficha(nome=nome, gols=gols)