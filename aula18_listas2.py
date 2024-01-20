#LISTAS DENTRO DE LISTAS
cadastrogeral = list()

print(f'-------CADASTRO GERAL-------')

while True:
    pessoa = [
        str(input('Nome: ')),
        int(input('Idade: ')),
        str(input('Sexo: '))
    ]
    cadastrogeral.append(pessoa)
    fim = str(input('Deseja cadastrar mais uma pessoa? [S/N]: ')).upper().strip() [0]
    if fim == 'N':
        break
print('Você cadastrou as seguintes pessoas: ')
for nome, idade, sexo in cadastrogeral:
        print(f'{nome} tem {idade} anos de idade e é do sexo {sexo}')
print('Os maiores de idade são: ')
for nome, idade, _ in cadastrogeral:
    if idade >= 18:
        print(nome)
    else:
        print(f'{nome} não é maior de idade não')

'''
cadastrogeral = []

print('-------CADASTRO GERAL-------')

while True:
    pessoa = [
        input('Nome: '),
        int(input('Idade: ')),
        input('Sexo: ')
    ]
    cadastrogeral.append(pessoa)

    fim = input('Deseja cadastrar mais uma pessoa? [S/N]: ').upper().strip()[0]
    if fim == 'N':
        break

print('Você cadastrou as seguintes pessoas:')
for nome, idade, _ in cadastrogeral:
    print(f'{nome} tem {idade} anos de idade')'''
