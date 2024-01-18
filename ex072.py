#MOTRANDO O NÚMERO POR EXTENSO USANDO UMA TUPLA

numbers = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

while True:
    posição = int(input('Digite um número entre 0 e 20: '))
    if posição not in range(0, 21):
        posição = int(input('Tente novamente: Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {numbers[posição]}!')
    continuar = str(input('Quer digitar outro número? [S/N]: ')).strip().upper() [0]
    if continuar not in 'SN':
        continuar = str(input('Sim ou não? --> ')).strip().upper() [0]
    if continuar == 'N':
        break

print('Obrigado e Volte Sempre! ')
    
