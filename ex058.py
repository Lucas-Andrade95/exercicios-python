#JOGO DA ADVINHAÇÃO COM WHILE

from random import randint

numero = 1
adivinhando = 0
tentativas = 1
while numero != adivinhando:
    numero = randint(0,10)
    adivinhando = int(input('Adivinha o número de 0 a 10 que estou pensando! '))
    if numero != adivinhando:
        tentativas += 1
        print('Não foi esse... Na verdade pensei no {}'.format(numero))
print('Acertou, miserávis! Na {}ª tentativa!'.format(tentativas))
