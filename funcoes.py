
def mostralinha():
    print('-'*50)

def area(x, y):
    return x * y


def mensagem(msg):
    print('=-='*30)
    print(f'{msg:^90}')
    print('=-='*30)


def multiplica(a, b):
    resultado = (a * b)
    print(f'{a} x {b} =', resultado)


def contador(* numeros):
    contador = 0
    for c in numeros:
        contador += 1
    print(f'Recebi {contador} valores.')


def dobralista(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2
        posicao += 1
    

'''
print('Vou mostrar uma linha na tela -> ')
mostralinha()

mensagem('CURSO EM VÍDEO')
mensagem('CADASTRO DE ALUNOS')

multiplica(int(input('Valor A ')), int(input('Valor B ')))

contador(2, 5, 4)

valores = 5
dobralista(valores)
print(valores)

'''

#EMPACOTANDO E DESEMPACOTANDO VALORES
'''
tupla = 1, 2, 3, 4, 5, 6
print(tupla)
a, *b, c = tupla

print(b)
'''