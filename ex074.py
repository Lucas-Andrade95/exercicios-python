#INSERTING ALEATORY VALUES IN A TUPLE AND SHOWING THE MINOR AND MAJOR VALUES

from random import randint

tupla = randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10)
print(f'Valores da tupla: {tupla}')

#MAIOR E MENOR VALOR USANDO O FOR
'''for c in range(0, len(tupla)):
    if c == 0:
        menorvalor = tupla[c]
        maiorvalor = tupla[c]
    if tupla[c] < menorvalor:
        menorvalor = tupla[c]
    elif tupla[c] > maiorvalor:
        maiorvalor = tupla[c]

print(f'O menor valor é {menorvalor} e o maior valor é {maiorvalor}') '''

#MAIOR E MENOR VALOR USANDO max() e min()

print(f'O maior valor sorteado foi {max(tupla)} e o menor valor foi {min(tupla)}!')
