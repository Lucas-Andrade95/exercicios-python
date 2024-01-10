#SOMANDO NUMEROS, CALCULANDO A SOMA E A MÉDIA, MAIOR E MENOR VALOR E PERGUNTANDO SE DESEJA CONTINUAR.

numero = soma = contador = maiorvalor = menorvalor = 0
fim = 'S'

#menorvalor = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999 #JEITINHOBRASILEIRO

while fim == 'S':
    numero = float(input('Digite um número: '))
    soma += numero
    if numero != 0:
        contador += 1
    if contador == 1:
         maiorvalor = menorvalor = numero
    if numero > maiorvalor:
         maiorvalor = numero
    if numero < menorvalor:
         menorvalor = numero
    pergunta = input('Deseja continuar [S/N]? ').upper().strip() [0]
    if pergunta == 'N':
        fim = 'N'
    elif pergunta == 'S':
            fim = 'S'
    else:
        pergunta = input('Digite "S" para Sim e "N" para não: ').upper().strip()
        fim = pergunta

media = soma / contador
print(f'''Você digitou {contador} números. A soma deles é {soma} e a média é {media:.3f}.
O maior valor é {maiorvalor} e o menor valor é {menorvalor}''')