# ALGORITMO PARA APROVAÇÃO DE EMPRÉSTIMO BANCÁRIO
print ('SIMULAÇÃO DE EMPRÉSTIMO BANCO BESTANDER')

nome = str(input('Nome completo: '))
casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário atual: R$ '))
anos = int(input('Em quantos anos pretende pagar? '))
mensalidade = float(casa / (anos * 12))
salario30 = float(salario * 0.3)

if mensalidade <= (salario30):
    print ('Parabéns {}! Seu empréstimo foi aprovado! '.format(nome))
    print ('Mensalidade: {}x de R${:.2f},  '.format(anos, mensalidade))
else:
    print ('Empréstimo NEGADO.')

print('Até a próxima!')

