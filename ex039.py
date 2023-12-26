#ALISTAMENTO MILITAR
from datetime import date
atual = date.today().year

print ('----ALISTAMENTO MILITAR----')

nome = str(input('Nome Completo: '))
sexo = int(input('Sexo: MASCULINO: 1; FEMININO: 2: '))
if sexo == 2:
    print('Você é mulher e não precisa se alistar!')
else:
    birth = int(input('Ano de Nascimento: '))
    age = int(atual - birth)

if age == 18:
    print('{}, está na hora de se alistar!'.format(nome))
elif age < 18:
    print ('{}, você ainda vai se alistar!'.format(nome))
    faltaxanos = int(18 - age)
    print ('{}, falta {} anos para o alistamento militar!'.format(nome, faltaxanos))
else:
    print ('{}, você já passou da hora de se alistar!'.format(nome))
    passouxanos = int(age - 18)
    print('Já se passaram {} anos desde o ano do seu alistamento obrigatório.'.format(passouxanos))

print('FIM')

