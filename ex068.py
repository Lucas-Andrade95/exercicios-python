#PAR OU ÍMPAR
from random import randint
contador = 0

while True:
    print('=-='*25)
    print('Vamos jogar PAR OU ÍMPAR!')
    jogador = int(input('Digite um número: '))
    parouimpar = str(input('PAR OU ÍMPAR? [P/I]: ')).upper().strip() [0]
    computador = randint(0,11)
    soma = jogador + computador
    print(f'Você jogou {jogador} e o computador {computador}. Total: {soma}. ', end='')
    if soma % 2 == 0:
        print(' DEU PAR!')
        verificador = 'P'
    else:
        print(' DEU ÍMPAR!')
        verificador = 'I'

    if verificador == parouimpar:
        contador += 1
        print('Você venceu!!!')
        print('Vamos jogar novamente...')
    else:
        break
print(f'GAME OVER! Você venceu {contador} vez(es).')
