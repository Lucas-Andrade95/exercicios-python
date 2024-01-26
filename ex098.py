from funcoes import mostralinha, contagem

def contagem(inicio, fim, passo):
    if inicio > fim and passo > 0:
        passo = passo * (-1)
    elif inicio > fim and passo == 0:
        passo = - 1
    elif inicio < fim and passo == 0:
        passo = 1
    for x in range(inicio, fim, passo):
        print(x, end = ' ')

mostralinha()
contagem(1, 11, 1)
print('Fim!')
mostralinha()
contagem(10, 0, -2)
print('Fim! ')
mostralinha()
print('Agora é a sua vez de personalizar a contagem! ')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contagem(inicio, fim, passo)
print('Fim! ')
mostralinha()