#APRENDENDO LISTAS

from random import randint

'''lista = [input('Nome: '), input('Idade: '), input('Sexo: ')]
print('Você cadastrou: ', lista)
altera = str(input('Gostaria de alterar o nome? [S/N]: ')).strip().upper()
if altera == 'S':
    nome = str(input('Nome: '))
    lista[0] = nome
print(lista)'''

lista = [randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10)]
print(lista)
#lista.sort()
#print('Lista em ordem: ', lista)    
lista.sort(reverse=True)
print('Lista em ordem reversa: ', lista)
print(f'Essa lista tem {len(lista)} elementos.')

#ELIMINANDO OS ZEROS DA LISTA COM WHILE
'''
c = len(lista)

while c >= 0:
    if lista[c] == 0:
        del lista[c]
    c -= 1

print('Lista sem zeros: ', lista)
print(f'Agora a lista tem {len(lista)} elementos.')'''

#ELIMINANDO ZEROS DA LISTA COM IF _ IN

if 0 in lista:
    print('Vou remover os zeros!')
    lista.remove(0)
    print(f'Agora a lista tem {len(lista)}, veja!: {lista}')

lista.insert(0,'início -->')
lista.append('fim')

for c, v in enumerate(lista):
    print(f'Na posição {c} encontramos o {v}!')
print('Agora vamos adicionar mais 2 valores a essa listinha: ')

for c in range(0,2):
    lista.append(int(input('Digite um número: ')))

print(f'Essa é minha nova lista: {lista}')

print('Agora você pode adicionar quantos valores quiser! Vamos lá!')

while True:
    lista.append(input('Digite algo: '))
    fim = 'S'
    fim = input('Deseja continuar? [S/N]: ').strip().upper() [0]
    if fim not in 'SN':
        fim = input('Deseja continuar? [S/N]: ').strip().upper() [0]
    if fim == 'N':
        break
print('Agora nossa lista ficou assim: ', lista)