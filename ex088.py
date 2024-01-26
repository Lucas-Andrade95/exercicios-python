from random import randint
from time import sleep

lista = list()
jogos = []
total = 0

print('-'*30)
print('   PALPITES PARA A MEGA SENA ')
print('-'*30)
quantasvezes = int(input('Quantos palpites de jogos você quer? '))

while total < quantasvezes:
    contador = 0
    while True:
        numero = randint(1,60)
        if numero not in lista:
            lista.append(numero)
            contador += 1
        if contador == 6:   
            break    
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print(f'''
Muito bem, segue {quantasvezes} palpites de jogos: 
      ''')
for posição, cadalista in enumerate(jogos):
    print(f'Jogo nº {posição +1}: {cadalista}')
    sleep(0.3)
print()

'''#PALPITES PARA A MEGA SENA

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
'''