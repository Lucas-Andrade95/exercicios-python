jogadores = list()
gols = []
contador = totaldegols = 0

while True:
    jogador = {
        'código': contador,
        'nome': str(input('Nome do Jogador: ')),
        'partidas': int(input('Quantas partidas ele jogou? '))
}
    for c in range(0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols na {c + 1}ª partida? ')))

    jogador['gols'] = gols.copy()
    gols.clear()

    for c in jogador['gols']:
         totaldegols += c

    jogador['total'] = totaldegols
    totaldegols = 0

    contador += 1
    jogadores.append(jogador)   
    
    fim = input('Quer continuar? [S/N]: ').strip().upper() [0]
    while fim not in 'SN':
         fim = input('Sim ou Não? ').strip().upper() [0]
    if fim == 'N':
            break
print('~'*50)  
print('cod   nome          gols         total')
print('-'*50)   
for cada_jogador in jogadores:
     print(f'{cada_jogador["código"]}  {cada_jogador["nome"]}   {cada_jogador["gols"]}  {cada_jogador["total"]}')
print('-' * 50)

while True:
    mostrar_dados = int(input('Mostrar dados de qual jogador? (999 para parar):'))
    if mostrar_dados == 999:
        print('Até mais! ')
        break
    if mostrar_dados >= len(jogadores):
         print(f'Erro! não existe jogador na posição {mostrar_dados}, tente novamente.')
    else:
        print(f'Mostrando dados do jogador {jogadores[mostrar_dados]["nome"]} ')
        for c, d in enumerate(jogadores[mostrar_dados]['gols']):
             print(f'Na partida {c} fez {d} gols')
