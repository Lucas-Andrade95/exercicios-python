#SOMANDO NÚMEROS ÍMPARES, DIVISÍVEIS POR 3 DE 1 ATÉ 500

s = 0
for x in range(1,501,2):
    if x % 3 == 0:
        s += x
print('A soma de todos os números ímpares, divisíveis por 3 no intervalo de 1 à 500 é de: {}'.format(s))    
