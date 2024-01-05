'''#CALCULO DE FATORIAL COM FOR
print ('Cálculo de Fatorial')
fatorial = 1
n = int(input('Inisira um número positivo: '))

for x in range(1,n + 1):
    fatorial = fatorial * x

print('O fatorial n! de {} é igual a {}'.format(n,fatorial))
      
#NÃO CONSEGUI RESOLVER ESSA BUCHA SOZINHO'''

#CALCULO DE FATORIAL COM WHILE

print('''CÁLCULO DE FATORIAL n!
 ''')
n = int(input('Digite um número inteiro positivo: '))
c = n
f = 1
print(f'Calculando {n}! = ', end = '')
while c > 0:
    print(c, end = ' ')
    print('x' if c > 1 else '=', end = ' ' )
    f *= c
    c -= 1
print(f)

#TAMBÉM PODEMOS USAR O MÓDULO MATH > FACTORIAL