#ALUNOS EM SALA DE AULA
listageral = []
aluno = []
media = []

while True:
    aluno.append(input('Nome do aluno: '))
    aluno.append(float(input('Nota 01: ')))
    aluno.append(float(input('Nota 02: ')))
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

for c in listageral:
    media.append((c[1] + c[2]) / 2)


for c, d in enumerate(listageral):
    print(f'{c:<}  {d[0]},   {media[c]:>15}')

