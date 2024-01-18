#BRASILEIRÃO - TREINANDO TUPLAS

colocados = 'Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza'
print('-----TABELA BRASILEIRÃO 2023-----')
print(f'Os cinco primeiros colocados são: {colocados[:5]}')
print(f'Os últimos 4 colocados são: {colocados[-4:]}')
print('Segue uma lista com os times em ordem alfabética: ')
print(sorted(colocados))
print(f'O time do Botafogo está na {colocados.index("Botafogo")+1}ª posição.')