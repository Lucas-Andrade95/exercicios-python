#QUAL O MAIOR E MENOR NÚMERO?

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Só mais um número, vai: '))
if n1 > n2 > n3:
    maiornumero = n1
    menornumero = n3
    print('O maior número é o {} e o menor número é o {}'.format(maiornumero, menornumero))
if n1 > n3 > n2:
    maiornumero1 = n1
    menornumero1 = n2
    print('O maior número é o {} e o menor número é o {}'.format(maiornumero1, menornumero1))
if n2 > n1 > n3:
    maiornumero2 = n2
    menornumero2 = n3
    print('O maior número é o {} e o menor número é o {}'.format(maiornumero2, menornumero2))
if n2 > n3 > n1:
    maiornumero3 = n2
    menornumero3 = n1
    print('O maior número é o {} e o menor número é o {}'.format(maiornumero3, menornumero3))
if n3 > n2 > n1:
    maiornumero4 = n3
    menornumero4 = n1
    print('O maior número é o {} e o menor número é o {}'.format(maiornumero4, menornumero4))
if n3 > n1 > n2:
    maiornumero5 = n3
    menornumero5 = n2
    print('O maior número é o {} e o menor número é o {}'.format(maiornumero5, menornumero5))

print('THE END')
    
#O PROGRAMA NÃO FUNUNCIA QUANDO COLOCAMOS NÚMEROS IGUAIS


