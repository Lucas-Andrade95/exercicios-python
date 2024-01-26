from funcoes import mostralinha
def maior(lista):
    x = lista[0]
    for c in lista:
        if c > x:
            x = c
    return x


numeros = []

mostralinha()
while True:
    valor = int(input('Digite um número ou 999 para parar: '))
    if valor == 999:
        break
    else:
        numeros.append(valor)

mostralinha()
print('Analisando os valores informados: ')
for c in numeros:
    print(c, end = ' ')
print(f'--> Foram informados {len(numeros)} ao todo.')
print(f'O maior valor informado foi {maior(numeros)}.')


