#ALISTAMENTO MILITAR

print ('----ALISTAMENTO MILITAR----')
nome = str(input('Nome Completo: '))
birth = int(input('Ano de Nascimento: '))
age = int(2024 - birth)

if age == 17 or age == 18:
    print('{}, está na hora de se alistar!'.format(nome))
elif age < 17:
    print ('{}, você ainda vai se alistar!'.format(nome))
    faltaxanos = int(17 - age)
    print ('{}, falta {} anos para o alistamento militar!'.format(nome, faltaxanos))
else:
    print ('{}, você já passou da hora de se alistar!'.format(nome))
    passouxanos = int(age - 18)
    print('Já se passaram {} anos desde o ano do seu alistamento obrigatório.'.format(passouxanos))

print('FIM')

