#SOMANDO APENAS NÚMEROS PARES
soma=0
conta=0
for x in range(0,7):
    y = int(input('Digite um número: '))
    if y % 2 == 0:
        soma += y
        conta += 1
print('A soma apenas dos {} valores pares é: {}'.format(conta,soma))
