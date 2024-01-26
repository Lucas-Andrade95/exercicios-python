cadastro = {}
geral = []
mulheres = []

#LOOP PARA INSERIR OS DADOS
while True:
    cadastro = { 
        'nome': str(input('Nome: ')),   
        'sexo': str(input('Sexo: [M/F]: ')).upper().strip() [0],
        'idade': int(input('Idade: '))
    }

    if cadastro['sexo'] == 'F':
        mulheres.append(cadastro['nome'])

    geral.append(cadastro)
    

    fim = input('Quer continuar? [S/N]: ').strip().upper() [0]
    while fim not in 'SN':
        fim = input('Sim ou Não? [S/N]: ').strip().upper() [0]
    if fim == 'N':
        break

#SOMANDO AS IDADES
'''for c in geral:
    totalidades += c["idade"]'''
#SOMANDO AS IDADES E CALCULANDO A MÉDIA DE UMA FORMA PYTHONICA
media = sum(cadastro['idade'] for cadastro in geral) / len(geral)

print('~'*70)
print(f' - O grupo tem {len(geral)} pessoas.')
print(f' - A média de idade é de {media:.2f} anos.')
print(f' - As mulheres cadastradas foram: ', end ='')
for c in mulheres:
    print(f'{c} ', end='')
print(f'\n - Lista das pessoas que estão acima da média de idade: ')
for c in geral:
    if c['idade'] > media:
        for chave, valor in c.items():
            print(f'{chave} = {valor}; ', end = '')
print()
print('>>> ENCERRADO <<<')

'''#CADASTRO DE PESSOAS

cadastro = {}
geral = []
mulheres = []
contador = 1
fim = 'S'
totalidades = 0

while True:
    cadastro['número'] = contador
    cadastro['nome'] = str(input('Nome: '))
    cadastro['sexo'] = str(input('Sexo: [M/F]: ')).upper().strip() [0]
    if cadastro['sexo'] == 'F':
        mulheres.append(cadastro['nome'])
    cadastro['idade'] = int(input('Idade: '))
    geral.append(cadastro.copy())
    cadastro.clear()
    contador += 1
    fim = input('Quer continuar? [S/N]: ').strip().upper() [0]
    while fim not in 'SN':
        fim = input('Sim ou Não? [S/N]: ').strip().upper() [0]
    if fim == 'N':
        break

for c in geral:
    totalidades += c["idade"]

media = totalidades / geral[-1]["número"]

print('~'*70)
print(f' - O grupo tem {geral[-1]["número"]} pessoas.')
print(f' - A média de idade é de {media:.2f} anos.')
print(f' - As mulheres cadastradas foram: ', end='')
for c in geral:
    if c['sexo'] == 'F':
        print(f'{c["nome"]}', end=' ')
print(f'\n - Lista das pessoas que estão acima da média de idade: ')
for c in geral:
    if c['idade'] > media:
        print()
        for chave, valor in c.items():
            print(f'{chave} = {valor}; ', end = '')
print()
print('>>> ENCERRADO <<<')'''
