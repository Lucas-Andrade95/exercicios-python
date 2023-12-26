from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] - Pedra
[1] - Papel
[2] - Tesoura''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!')
sleep(0.5)
print('-=-' * 12)
print('Você: {}'.format(itens[jogador]))
print('Computador: {}'.format(itens[computador]))
print('-=-' * 12)

if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('VOCÊ VENCEU!')
    elif jogador == 2:
        print('VOCÊ PERDEU!')
    else:
        print('Jogada inválida!')   
elif computador == 1:
    if jogador == 0:
        print('VOCÊ PERDEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('VOCÊ VENCEU!')
    else:
        print('Jogada inválida!') 

elif computador == 2:
    if jogador == 0:
        print('VOCÊ VENCEU!')
    elif jogador == 1:
        print('VOCÊ PERDEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada inválida!') 
