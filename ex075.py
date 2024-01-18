#Inserting values in a tuple
conta9 = posiçãode3 = pares = 0
tempar = False

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
valor3 = int(input('Digite ainda outro valor: '))
valor4 = int(input('Só mais um numerozinho: '))

tupla = valor1, valor2, valor3, valor4
print(f'Pronto! Você digitou os valores: {tupla}')

'''
for posição, c in enumerate(tupla):
    if c == 9:
        conta9 += 1
    if c % 2 == 0:
        pares = c + posição #NÃO CONSEGUI FAZER OS VALORES PARES
    if c == 3:
        posiçãode3 = posição

if posiçãode3 == 0:
    print(f'O valor 9 apareceu {conta9} vezes')
    print(f'O valor 3 não apareceu em nenhuma posição')
    print(f'Os valores pares digitados foram: {pares}')
else:
    print(f'O valor 9 apareceu {conta9} vezes')
    print(f'O valor 3 aparece na {posiçãode3 +1}ª posição')
    print(f'Os valores pares digitados foram: {pares}') 

'''
print(f'O valor de 9 apareceu {tupla.count(9)} vezes!')
if 3 in tupla:
    print(f'O valor 3 foi digitado na {tupla.index(3) +1}ª posição.')
else:
    print('O valor 3 não foi digitado.')

for c in tupla:
    if c %2 == 0:
        tempar = True

if tempar == True:
    print('Os valores pares digitados foram: ', end='')
    for c in tupla:
        if c %2 == 0:
            print(c, end=' ')
else:
    print('Nenhnum número par foi digitado.')
