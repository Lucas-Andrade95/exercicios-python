#  ESTRUTURAS DE REPETIÇÃO COM TESTE LÓGICO
'''c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')

n = 1
while n != 0:
    n = int(input('Digite um número: '))
print('Fim')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares.'.format(par, impar))

#UTILIZAMOS ESSA ESTRUTURA QUANDO NÃO TEMOS UM INTERVALO (RANGE) ESPECÍFICO
