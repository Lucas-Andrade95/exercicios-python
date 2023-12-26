#VALORES DE PRODUTO, JUROS E CONDIÇÕES

print('''Olá! Aqui vendemos somente três tipos de Sapatos:
1 - Sapato Social por R$ 149,90')
2 - Tênis por apenas R$ 99,90 ')
3 - Sandália por apenas R$ 49,90''')

produto = int(input('Qual deles você escolhe? (Digite 1, 2 ou 3): '))

if produto == 1:
    print('Legal! Você escolheu o Sapato Social!')
    valor = float(149.9)
elif produto == 2:
    print('Legal! Você escolheu o Tênis!')
    valor = float(99.9)
elif produto == 3:
    print('Legal! Você escolheu a Sandália!')
    valor = float(49.9)
else:
    print('Você não digitou um número válido! Reinicie o programa.')

print('Qual será a forma de pagamento?')
pgto = int(input('1 - Á vista; 2 - À vista no cartão;  3 - Parcelado: '))

if pgto == 1:
    print('Ok! Você ganhou 10% de desconto!')
    valorfinal = float(valor - (valor * 0.1))
    print('Fica apenas R$ {:.2f}!'.format(valorfinal))
elif pgto == 2:
    print ('Ok! Você ganhou 5% de desconto!')
    valorfinal = (float(valor - (valor * 0.05)))
    print('Fica apenas R$ {:.2f}!'.format(valorfinal))
elif pgto == 3:
    parcelas = int(input('Ok! Em quantas vezes gostaria de parcelar? '))
    valorfinalparcelado = float(valor + ((valor * 0.05) * parcelas))
    valordaparcela = (valorfinalparcelado / parcelas)
    print('Ok! Como tem uma taxinha de 5% de juros por parcela, fica assim: ')
    print('{}x de R$ {:.2f}. Sendo que o valor final parcelado será de R$ {:.2f}!'.format(parcelas,valordaparcela,valorfinalparcelado))
else:
    print('Desculpe, você não digitou um valor válido! Reinicie o programa.')

print('OBRIGADO E VOLTE SEMPRE!')