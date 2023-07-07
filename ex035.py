#É POSSÍVEL FORMAR UM TRIÂNGULO?

print('Vamos saber se três retas poderão formar um triângulo.')
a = float(input('Digite o comprimento da primeira reta (cm): '))
b = float(input('Digite o comprimento da segunda reta (cm): '))
c = float(input('Digite o comprimento da terceira reta (cm):'))
if (b - c) < a < b + c:
    print('Sim, é possível formar um triângulo!')
if (a - c) < b < a + c:
    print('Sim, é possível formar um triângulo! ')
if (a - b) < c < a + b:
    print('Sim, é possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo.')

print('THE END')

#DEU RUIM