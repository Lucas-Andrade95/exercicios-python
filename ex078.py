# INSERINDO VALORES EM UMA LISTA E MOSTRANDO MAIOR E MENOR VALOR
lista = []

for c in range(0,5):
    lista.append(int(input(f'Digite um número na posição {c}: ')))
print(f'Os valores digitados foram: {lista}')

if lista[0] == lista[1] == lista[2] == lista[3] == lista[4]:
    print('Todos os valores são iguais.')
else:
    print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')
    for c, v in enumerate(lista):
        if v == max(lista):
            print(f'{c}... ', end='')
    print(f'\nO menor valor digitado foi {min(lista)} nas posições ', end ='')
    for c, v in enumerate(lista):
        if v == min(lista):
            print(f'{c}... ', end='')


