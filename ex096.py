#FUNÇÃO PARA CÁLCULO DE ÁREA
from funcoes import mostralinha, area



print('Controle de Terrenos')
mostralinha()
a = float(input('Largura (m): '))
b = float(input('Comprimento (m): '))

print(f'A área de um terreno {a} x {b} é de {area(a, b)}m²')