#CALCULANDO O PREÇO DA VIAGEM

km = int(input('Qual a distância da viagem em Km? '))
'''if km <= 200:
    valordapassagem1 = km*0.5
    print ('O valor da passagem será de R$ {:.2f}'.format(valordapassagem1))
else:
    valordapassagem2 = km*0.45
    print('O valor da passagem será de R$ {:.2f}!'.format(valordapassagem2))'''

#CONDIÇÃO SIMPLIFICADA
valordapassagem = km * .50 if km <= 200 else km * 0.45
print('O valor da passagem será de R$ {:.2f}!'.format(valordapassagem))
print('--FIM--')
