
def mostralinha():
    '''
    Imprime uma linha tracejada no terminal
    '''
    print('-'*50)

def area(x, y):
    '''
    --> Retorna a área de uma superfície através dos parâmetros:
    x = Comprimento
    y = Largura
    '''
    return x * y


def mensagem(msg):
    '''
    Imprime uma mensagem de título entre linhas tracejadas
    '''
    a = len(msg) + 2
    print('-'*a)
    print(f' {msg}')
    print('-'*a)


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
    
def contagem(inicio, fim, passo):
    if inicio > fim and passo > 0:
        passo = passo * (-1)
    elif inicio > fim and passo == 0:
        passo = - 1
    elif inicio < fim and passo == 0:
        passo = 1
    for x in range(inicio, fim, passo):
        print(x, end = ' ')

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