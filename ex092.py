#CADASTRO DE PESSOAS
from datetime import date
from time import sleep

cadastro = {}
geral = list()
fim = 'S'

print('~'*30)
print('    CADASTRO DE TRABALHADOR')
print('~'*30)

while True:
    cadastro['Nome'] = str(input('Nome: '))
    anonascimento = int(input('Ano de Nascimento: '))
    idade =  date.today().year - anonascimento
    cadastro['Idade'] = idade
    ctps = int(input('CTPS: (0 não tem): '))
    if ctps != 0:
        cadastro['CTPS'] = ctps
        ano_de_contratação = int(input('Ano de Contratação: '))
        cadastro['Contratação'] = ano_de_contratação
        cadastro['Salário'] = float(input('Salário: R$ '))
        cadastro['Aposentadoria'] = (ano_de_contratação + 35) - anonascimento
    geral.append(cadastro.copy())
    cadastro.clear()
    fim = input('Deseja cadastrar mais uma pessoa? [S/N]: ').upper().strip() [0]
    while fim not in 'SN':
        fim = input('Sim ou não? [S/N]: ').upper().strip() [0]
    if fim == 'N':
        break
    print('~'*30)

pergunta = input('Gostaria de ver as pessoas cadastradas? [S/N]: ').upper().strip() [0]
while pergunta not in 'SN':
    pergunta = input('Sim ou não? [S/N]: ').upper().strip() [0]
if pergunta == 'S':
    print('~'*30)
    print('PESSSOAS CADASTRADAS: ')
    for cadacadastro in geral:
        print('~'*30)
        for chave, valor in cadacadastro.items():
            print(f'{chave}: {valor}')
            sleep(.3)
print()
print('Cadastro concluído com sucesso! Obrigado.')
        




