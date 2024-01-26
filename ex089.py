#ALUNOS EM SALA DE AULA
listageral = []
aluno = []

while True:
    aluno.append(input('Nome do aluno: '))
    aluno.append(float(input('Nota 01: ')))
    aluno.append(float(input('Nota 02: ')))
    aluno.append((aluno[1] + aluno[2]) / 2)
    listageral.append(aluno[:])
    aluno.clear()
    fim = str(input('Cadastrar mais um aluno? [S/N]: ')).upper().strip() [0]
    while fim not in 'SN':
        fim = str(input('Cadastrar mais um aluno? [S/N]: ')).upper().strip() [0]
    if fim == 'N':
        break

print('-'*30)
print('Nº NOME                MEDIA')
print('-'*30)

for c, d in enumerate(listageral):
    print(f'{c:<}  {d[0]},   {d[3]:>15}')

while True:
    print()
    numeroaluno = int(input('Mostrar notas de qual aluno? (999 para parar): '))
    if numeroaluno == 999:
        break
    else:
        print(f'Notas de {listageral[numeroaluno][0]} são {listageral[numeroaluno][1]} e {listageral[numeroaluno] [2]}')
    
print('''
Obrigado! Volte sempre!      ''')
