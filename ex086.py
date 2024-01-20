#MATRIZ 3X3
matriz = [[0,0,0],[0,0,0],[0,0,0]]

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um número na posição ({linha},{coluna}): '))

for x, y, z in matriz:
    print(f'[ {x:^4} ]  [ {y:^4} ] [ {z:^4} ]')


'''
#MINHA TENTATIVA:

matriz = [[[],[],[]],[[],[],[]],[[],[],[]]]

for cadaposicao in matriz:
    for cadalista in cadaposicao:
        cadalista.append(int(input(f'Digite um número: ')))

print('-'*20)
for x, y, z in matriz:
    print(x, y, z)'''