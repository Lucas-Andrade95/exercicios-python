#CAIXA ELETRÔNICO

print('-'*30)
print('      BANCO SULAMERICANO')
print('-'*30)
valor = int(input('Valor a sacar: '))
total = valor
cédula = 50
totaldecédulas = 0
while True:
    if total >= cédula:
        total -= cédula
        totaldecédulas += 1
    else:
        if totaldecédulas > 0:
            print(f'Total de {totaldecédulas} de R$ {cédula},00 ')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        totaldecédulas = 0
        if total == 0:
          break
print('-' * 30)

