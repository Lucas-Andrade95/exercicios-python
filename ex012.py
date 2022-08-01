#CONVERSÃO DE MOEDA
print('CONVERSOR DE MOEDAS')
reais = float(input('Reais: '))
dolarhoje = float(input('Cotação Dólar hoje: '))
dolar = reais/dolarhoje
print('R${:.2f} vale hoje US${:.2f}'.format(reais, dolar))
