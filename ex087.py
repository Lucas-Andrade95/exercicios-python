'''matriz = [ [  [],[],[]  ], [  [],[],[]  ], [  [],[],[]  ] ]

for x, y, z in matriz:
    print(x,y,z)'''

matriz = [ [  [],[],[]  ], [  [],[],[]  ], [  [],[],[]  ] ]
somapares = numero = somaterceiracoluna = 0

for cadaum in matriz:
    for c in range(0, 3):
        cadaum[c].append(int(input(f'Digite um valor: ')))

#IMPRIMINDO A MATRIZ:
print('-'*30)
for x, y, z in matriz:
    print(f'{x}    {y}    {z}')

#ACESSANDO OS VALORES E SOMANDO OS PARES
for c in matriz:
    for d in c:
        for y in d:
            if y % 2 == 0:
                somapares += y

#SOMANDO A TERCEIRA COLUNA
for x, y, z in matriz:
    somaterceiracoluna += z[0]
    
print('-'*30)
print(f'A soma dos valores pares é igual a {somapares}')
print(f'A soma da terceira coluna é igual a {somaterceiracoluna}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
