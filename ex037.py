#BASES NUMÉRICAS E CONVERSÃO

number = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases numéricas para conversão:
[1] CONVERTER PARA BINÁRIO
[2] CONVERTER PARA OCTAL
[3] CONVERTER PARA HEXADECIMAL''')

opção = int(input('Sua opção: '))

if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(number, bin(number) [2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(number, oct(number) [2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(number, hex(number) [2:]))
else:
    print('''OPÇÃO INVÁLIDA
TENTE NOVAMENTE''')