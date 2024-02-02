def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f

#PROGRAMA PRINCIPAL

numero = int(input('Digite um número para calcularmos o fatorial dele: '))
fat = fatorial(numero)
print(f'O fatorial de {numero} é {fat}.')
