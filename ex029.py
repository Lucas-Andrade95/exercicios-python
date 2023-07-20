#LENDO A VELOCIDADE DE UM CARRO

velocidade = float(input('Velocidade do carro (Km/h): '))
if velocidade > 80:
    multa = (velocidade-80)*7
    print('Você foi multado!!! Multa de R$ {:.2f}'.format(multa))
else:
    print('Boa viagem!')
print('--Tchau Tchau--')