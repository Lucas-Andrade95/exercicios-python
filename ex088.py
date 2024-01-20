#PALPITES PARA A MEGA SENA
from random import randint
import time
print('-'*30)
print(f'      PALPITES DA MEGA SENA')
print('-'*30)

quantosjogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-----Sorteando {quantosjogos} Jogos----- ')
for c in range (1, quantosjogos + 1):
    time.sleep(0.3)
    palpites = [randint(0,61), randint(0,61), randint(0,61), randint(0,61), randint(0,61), randint(0,61)]
    print(f'Jogo {c}: {palpites}')
print('----FIM---')