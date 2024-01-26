#DICIONÁRIO --> CADASTRO DE ALUNO
listageral = list()

print('-'* 30)
print('    CADASTRO DE ALUNO')
print('-'*30)

quantosalunos = int(input('Quantos alunos deseja cadastrar? '))

for c in range(0,quantosalunos):
    print('-'*30)
    aluno = {
        'Nome': str(input('Nome do Aluno: ')),
        'Média': float(input('Média do Aluno: '))
    }
    if aluno['Média'] >= 7:
        aluno['Situação'] = 'Aprovado'
    elif 5 <= aluno['Média'] < 7:
        aluno['Situação'] = 'Recuperação'
    else:
        aluno['Situação'] = 'Reprovado'
    listageral.append(aluno.copy())
    aluno.clear()

print()
print('CADASTRO GERAL DE ALUNOS: ')
for cadaaluno in listageral:
    print('-'*30)
    for chave, valor in cadaaluno.items():
        print(f'{chave}: {valor}')