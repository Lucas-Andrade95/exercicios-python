#INSERINDO NÚMEROS EM APENAS UMA LISTA E SEPARANDO PARES E ÍMPARES

lista = [[],[]]

for c in range(1,8):
    numero = int(input(f'Digite uo {c}º número: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)

lista[0].sort()
lista[1].sort()

print(f'''
Os valores pares digitados foram: {lista[0]}
Os valores ímpares digitados foram: {lista[1]}
''')

'''UTILIZANDO 2 LISTAS:
pares = []
ímpares = []

for c in range(0,7):
    numero = int(input('Digite um número: '))
    lista.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        ímpares.append(numero)
pares.sort()
ímpares.sort()

print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {ímpares}')
'''