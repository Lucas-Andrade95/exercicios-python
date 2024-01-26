numeros = []

def sorteia(lista):
    from random import randint
    for c in range(5):
        lista.append(randint(0,99))

def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    return soma


sorteia(numeros)
print(f'A função sorteia() sorteou os números: {numeros}')
print(f'A soma dos valores pares é de {somaPar(numeros)}.')
        

