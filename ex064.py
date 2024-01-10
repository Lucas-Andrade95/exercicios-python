#LENDO NÚMEROS, CONTANDO E SOMANDO

#DECLARANDO VARIÁVEIS
numero = soma = contador = 0

#LAÇO PARA LER E SOMAR OS NÚMEROS DIGITADOS
numero = int(input('Digite um número inteiro qualquer ou 999 para finalizar o programa: '))
while numero != 999:
    soma += numero
    contador += 1
    numero = int(input('Digite um número inteiro qualquer ou 999 para finalizar o programa: '))

#MOSTRANDO O RESULTADO
print(f'Você digitou {contador} números e a soma deles é igual a {soma}!')

