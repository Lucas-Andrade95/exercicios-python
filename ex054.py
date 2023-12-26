#QUANTOS SÃO MAIORES DE IDADE?
from datetime import date
atual = date.today().year
maiores = 0
menores = 0

for x in range(1,8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(x)))
    if atual - ano < 18:
        menores += 1
    else:
        maiores += 1
print('{} são maiores de idade e {} menores de idade.'.format(maiores,menores))
