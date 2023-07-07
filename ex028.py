#GUESSING A NUMBER

import random
sorteado = random.randint(1, 5)
numero = int(input('Digite um número de 1 a 5: '))
if sorteado == numero:
    print('Uau! Parabéns, você acertou! Ganhou o jogo!')
else:
    print('Não foi dessa vez! O número sorteado foi {}!'.format(sorteado))
print('--FIM--')
