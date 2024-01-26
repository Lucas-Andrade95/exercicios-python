
#GUARDANDO RESULTADOS DOS DADOS EM UMA LISTA

from random import randint
from time import sleep
from operator import itemgetter

jogandodados = { 
    'jogador1': randint(1,6),
    'jogador2': randint(1,6),
    'jogador3': randint(1,6),
    'jogador4': randint(1,6)
}
ranking = []

for k, v in jogandodados.items():
    sleep(0.3)
    print(f' O {k} tirou {v} no dado.')

ranking = sorted(jogandodados.items(), key = itemgetter(1), reverse = True)

print('--------RANKING--------')
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]}')




'''jogandodados = {}
lista = []


print('Valores sorteados: ')
for c in range(1,5):
    sleep(0.3)
    resultado = randint(1,7)
    jogandodados['Nome'] = str(f'jogador{c}')
    jogandodados['Resultado'] = resultado
    print(f'O jogador{c} tirou {resultado}')
    lista.append(jogandodados.copy())

    jogandodados.clear()

print(lista)    
print('Ranking dos jogadores: ')'''
