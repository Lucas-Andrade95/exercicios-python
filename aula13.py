#ESTRUTURAS DE REPETIÇÃO COM FOR

for c in range(0, 3):
    print('Hi World!')
print('FIM')

for d in range(0, 5):
    print(d)
print('FIM')

for e in range(7, 0, -1):
    print(e)
print('FIM')

for f in range(0, 7, 2):
    print(f)
print('FIM')

n = int(input('Digite um número: '))
for g in range(0, n):
    print(g)
print('Fim')

n1 = int(input('Digite um número: '))
for x in range(0, n1 + 1):
    print(x)
print('FIM')

inicio = int(input('Digite o início do intervalo: '))
fim = int(input('Digite o fim do intervalo: '))
passo = int(input('Digite o passo: '))
for y in range(inicio, fim, passo):
    print(y)
print('FIM')

s = 0
for w in range(0,4):
    numero = int(input('Digite um número: '))
    s += numero #QUE NADA MAIS É DO QUE S = S + NUMERO
print('O somatório de todos os números é: {}'.format(s))
