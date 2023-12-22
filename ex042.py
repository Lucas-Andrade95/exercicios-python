#TIPOS DE TRIÂNGULO

print('Vamos saber se três retas poderão formar um triângulo.')
a = float(input('Digite o comprimento da primeira reta (cm): '))
b = float(input('Digite o comprimento da segunda reta (cm): '))
c = float(input('Digite o comprimento da terceira reta (cm):'))
if a < (b + c) and b < (a + c) and  c < (a + b):
    print('Sim, é possível formar um triângulo!')
elif a == b and a == c and b == c:
    print('É um triângulo Equilátero!')
elif a == b or a == c or b == c:
    print ('É um triângulo Isósceles!')
elif a !=: b and a !=: c and b =!: c:
    print('É um Triângulo Escaleno!')
else:
    print('Não é possível formar um triângulo.')

    #NÃO FUNUNCIA