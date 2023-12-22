#MÉDIA DOS ALUNOS

print('Será que você passou de ano? ')
nome = str(input('Nome do aluno: '))
n1 = float(input('Nota do Primeiro Semestre: '))
n2 = float(input('Nota do Segundo Semestre: '))
media = float((n1 + n2) / 2)

if media < 5.0:
    print('Sinto muito {}, mas você foi REPROVADO!'.format(nome))
elif 5.0 < media < 6.9:
    print('{}, você está de RECUPERAÇÃO! Ainda tem uma chance!'.format(nome))
else:
    print ('Parabéns {}! Você passou de ano!'.format(nome))

print ('The End')
