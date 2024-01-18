#LISTAGEM DE PREÇOS COM TUPLAS
listagem = 'caneta', 1, 'lápis', 0.5, 'estojo', 3, 'borracha', 2.75, 'apontador', 2.75, 'caderno', 10, 'fichário', 15, 'grampeador', 6, 'régua', 4.5, 'compasso', 7.5

print(f'''
---------------------------------------
          LISTAGEM DE PREÇOS
---------------------------------------''')

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end = '')
    else:
        print(f'R$ {listagem[pos]:>5.2f}')
