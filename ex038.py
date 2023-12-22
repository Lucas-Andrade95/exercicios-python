# QUAL NÚMERO É MAIOR?

number1 = int(input('Digite um número: '))
number2 = int(input('Digite outro número: '))

if number1 > number2:
    print('O primeiro valor ({}) é o maior!'.format(number1))
elif number1 < number2: 
    print('O segundo valor ({}) é o maior!'.format(number2))
else:
    print('Os dois valores são iguais!')

print ('Fim')