lista = []
for c in range(0,10):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Valor adicionado ao final da lista...')
    else:
       posição = 0
       while posição < len(lista):
            if valor <= lista[posição]:
               lista.insert(posição, valor)
               print(f'Valor adicionado na posição {posição}')
               break
            posição += 1
print('-'*30)
print(f'Os valores adicionados em ordem crescente são: {lista}')
