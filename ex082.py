lista = []
pares = []
ímpares = []
fim = 'S'

while True:
    lista.append(int(input('Digite um valor: ')))
    fim = str(input('Quer continuar? [S/N]: ')).upper().strip() [0]
    while fim not in 'SN':
        fim = str(input('Digite S para Sim e N para Não: [S/N]: ')).upper().strip() [0]
    if fim == 'N':
        break

for c in lista:
    if c % 2 == 0:
        pares.append(c)
    else:
        ímpares.append(c)

print(f'Lista de números digitados: {lista}')
print(f'Lista de números pares: {pares}')
print(f'Lista de números ímpares {ímpares}')   
