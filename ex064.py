#LENDO NÚMEROS, CONTANDO E SOMANDO

#DECLARANDO VARIÁVEIS
numero = 0
soma = 0
contador = -1

#LAÇO PARA LER E SOMAR OS NÚMEROS DIGITADOS
while numero != 999:
    numero = int(input('Digite um número inteiro qualquer ou 999 para finalizar o programa: '))
    soma += numero
    contador += 1

#SUBTRAINDO A FLAG '999'
total = soma - 999

#MOSTRANDO O RESULTADO
print(f'Você digitou {contador} números e a soma deles é igual a {total}!')

