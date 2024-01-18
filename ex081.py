lista = []
fim = 'S'
while True:
    lista.append(int(input('Digite um número: ')))
    fim = str(input('Quer continuar? [S/N]: ')).upper().strip() [0]
    while fim not in 'SN':
        fim = str(input('Quer continuar? [S/N]: ')).upper().strip() [0]
    if fim == 'N':
        break
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse = True)
print(f'Segue a lista de valores em ordem decrescente: {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista! Está na {lista.index(5) +1}ª posição.')
else:
    print('O valor 5 não está na lista.')



