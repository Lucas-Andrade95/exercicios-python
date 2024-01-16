#TABUADA, ENCERRANDO COM NÚMEROS NEGATIVOS
numero = 1
resultado = 1

while True:
    print('-'*40)
    numero = int(input('Deseja ver a tabuada de qual valor? '))
    if numero >= 0:
        for x in range(1,11):
            resultado = x * numero
            print(f'{numero} X {x} = {resultado}')
    else:
        print('PROGRAMA TABUADA ENCERRADO! Volte sempre!')
        break

