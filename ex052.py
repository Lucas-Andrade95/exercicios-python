print('SERÁ QUE É NÚMERO PRIMO?')

n = int(input('Digite um número inteiro: '))
a = 0
for x in range(1,n+1):
    if n % x == 0:
        a += 1

if a == 2:
    print(n, 'É um número primo!')
else:
    print('{} é um número composto! Ele é divisível por {} números.'.format(n, a))
