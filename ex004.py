#DISSECANDO UMA VARIÁVEL

it = input('Digite algo: ')
print(type(it))
print('É alfanumérico? ', it.isalnum())
print('É um número? ', it.isnumeric())
print('É alfabético? ', it.isalpha())
print('É um dígito?', it.isdigit())
print('É um código ASCII ?', it.isascii())
print('É um espaço? ', it.isspace())
print('É um número decimal? ', it.isdecimal())
print('É printável na tela? ', it.isprintable())
print('Está em letras maiúsculas? ', it.isupper())
print('Está em letras minúsculas? ', it.islower())

#SOMANDO NUMEROS REAIS
number1 = float(input('Digite um numero: '))
number2 = float(input('Digite outro numero: '))
sum = (number1 + number2)
print('A soma entre {} e {} é igual a {}'.format(number1, number2, sum))