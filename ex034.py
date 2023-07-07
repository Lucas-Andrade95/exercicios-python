#AUMENTO SALARIAL

salario = float(input('Qual o seu salário? R$ '))
if salario > 1250:
    aumento = (salario*0.1) + salario
    print('Seu salário irá aumentar 10%, você vai receber R$ {:.2f}'.format(aumento))
else:
    aumento1 = (salario*0.15) + salario
    print('Seu salário irá aumentar 15%, você vai receber R$ {:.2f}'.format(aumento1))
print('THE END')
