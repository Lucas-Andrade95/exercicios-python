#JOKENPÔ
import random

print('JO-KEN-PÔ!')
jogador = int(input('1 - PEDRA; 2 - PAPEL; 3 - TESOURA: '))
computador = random.randint(1, 3)

if jogador == 1 and computador == 1:
    print('PEDRA X PEDRA: NINGUÉM VENCEU.')
elif jogador == 1 and computador == 2:
   print('PEDRA X PAPEL: VOCÊ PERDEU!')
elif jogador == 1 and computador == 3:
   print('PEDRA X TESOURA: VOCÊ VENCEU!')
elif jogador == 2 and computador == 1:
   print('PAPEL X PEDRA: VOCÊ VENCEU!')
elif jogador == 2 and computador == 2:
   print('PAPEL X PAPEL: NINGUÉM VENCEU.')
elif jogador == 2 and computador == 3:
   print('PAPEL X TESOURA: VOCÊ PERDEU!')
elif jogador == 3 and computador == 1:
   print ('TESOURA X PEDRA: VOCÊ PERDEU!')
elif jogador == 3 and computador == 2:
   print('TESOURA X PAPEL: VOCÊ VENCEU!')
elif jogador == 3 and computador == 3:
   print('TESOURA X TESOURA: NINGUÉM VENCEU.')
else:
   print(jogador, 'NÃO É UM NÚMERO VÁLIDO. TENTE NOVAMENTE.')

print('End of Game')
