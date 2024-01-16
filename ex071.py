#CAIXA ELETRÔNICO
valor = cedulas50 = 0

print('-'*30)
print('      BANCO SULAMERICANO')
print('-'*30)
valor = int(input('Valor a sacar: '))
if valor > 50:
    cedulas50 = valor / 50
    print(f'TOTAL DE {cedulas50} cédulas de R$ 50,00')