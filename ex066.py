#Armazenando e contando números (WHILE/BREAK)

#var
numero = contador = soma = 0

while True:
    numero = float(input('DIgite um número (ou 999 para parar): '))
    if numero == 999:
        break
    else:
        contador += 1
        soma += numero
    
print(f'Você digitou {contador} número(s) e a soma deles é igual a: {soma}! ')
