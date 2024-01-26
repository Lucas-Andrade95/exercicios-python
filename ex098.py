from funcoes import mostralinha

def contagem(a, b, c):
    for x in range(a, b, c):
        print(x, end = ' ')

mostralinha()
contagem(1, 11, 1)
print('Fim!')
mostralinha()
contagem(10, 0, -2)
print('Fim! ')
mostralinha()
print('Agora é a sua vez de personalizar a contagem! ')
mostralinha()

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
if inicio > fim and passo > 0:
    passo = passo * (-1)
elif inicio > fim and passo == 0:
    passo = - 1
elif inicio < fim and passo == 0:
    passo = 1
contagem(inicio, fim, passo)
print('Fim! ')