#GUESSING A NUMBER

print ('-=-' * 20)
print ('ADVINHE O NÚMERO QUE ESTOU PENSANDO AGORA!')
print ('-=-' * 20)
from random import randint
sorteado = randint(1, 5)  #SORTEIA UM NÚMERO E INSERE NA VAR 'SORTEADO'
numero = int(input('Tente um número de 1 a 5: '))
from time import sleep
print ('PROCESSANDO....')
sleep(3)
if sorteado == numero:
    print('Parabéns, você acertou! Ganhou o jogo!')
    print('-THE END-')
else:
    print('Não foi dessa vez! O número sorteado foi {}!'.format(sorteado))
    print('-----GAME OVER-----')

