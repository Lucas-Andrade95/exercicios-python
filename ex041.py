#FAIXA ETÁRIA DOS NADADORES PROFISSIONAIS

print('CADASTRO NA CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
nome = str(input('Nome completo: '))
ano = int(input('Ano de Nascimento: '))
idade = int(2024 - ano)
print ('CATEGORIA:')

if idade <= 9:
    print ('MIRIM')
elif 9 < idade <= 14:
    print ('INFANTIL')
elif 14 < idade <= 19:
    print('JÚNIOR')
elif 19 < idade <= 20:
    print('SÊNIOR')
else:
    print('MASTER')

print ('Cadastro Concluído.')