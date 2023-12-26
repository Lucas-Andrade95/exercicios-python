#TIPOS DE TRIÂNGULO

print('Vamos saber se três retas poderão formar um triângulo.')
a = float(input('Digite o comprimento da primeira reta (cm): '))
b = float(input('Digite o comprimento da segunda reta (cm): '))
c = float(input('Digite o comprimento da terceira reta (cm): '))
if a < (b + c) and b < (a + c) and  c < (a + b):
    print('Sim, é possível formar um triângulo ', end='')
    if a == b == c:
        print('equilátero!')
    elif a != b != c != a:
#IMPORTANTE! --> NA CONSTRUÇÃO "a =! b =! c:" o "a" e o "c" podem ser iguais, por isso precisamos adicionar que "c =! a" no final
        print('escaleno!')
    #elif a == b or a == c or b == c:   (POSSÍVEL CONSTRUÇÃO)
        #print ('isósceles!') 
    else:
        print('isósceles!')    
else:
    print('Não é possível formar um triângulo!')

