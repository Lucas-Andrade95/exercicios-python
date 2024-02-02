
help()

'''def ParouImpar(n):
    if n % 2 == 0:
        return True
    else:
        return False

while True:
    if ParouImpar(int(input('Digite um número: '))):
        print('É par!')
    else:
        print('É ímpar!')'''

'''cadastro = {}
geral = []
mulheres = []
contador = 0
totalidades = 0

while True:
    cadastro = { 
        'nome': str(input('Nome: ')),   
        'sexo': '',  # Inicializamos o campo 'sexo' com uma string vazia
        'idade': int(input('Idade: '))
    }

    while True:  # Loop para garantir que o sexo seja válido
        cadastro['sexo'] = input('Sexo: [M/F]: ').upper().strip()
        if cadastro['sexo'] in ['M', 'F']:  # Verifica se o sexo é 'M' ou 'F'
            break  # Se for válido, sai do loop
        else:
            print('Opção inválida. Por favor, digite M para masculino ou F para feminino.')

    if cadastro['sexo'] == 'F':
        mulheres.append(cadastro['nome'])

    geral.append(cadastro)
    
    contador += 1

    fim = input('Quer continuar? [S/N]: ').strip().upper() [0]
    while fim not in 'SN':
        fim = input('Sim ou Não? [S/N]: ').strip().upper() [0]
    if fim == 'N':
        break

#SOMANDO AS IDADES
totalidades = sum(cadastro['idade'] for cadastro in geral)

media = totalidades / contador

print('~'*70)
print(f' - O grupo tem {contador} pessoas.')
print(f' - A média de idade é de {media:.2f} anos.')
print(f' - As mulheres cadastradas foram: ', end = '')
for cada_cadastro in geral:
    if cada_cadastro['sexo'] == 'F':
        print(f'{cada_cadastro["nome"]} ', end = '')
print(f'\n - Lista das pessoas que estão acima da média de idade: ')
for c in geral:
    if c['idade'] > media:
        for chave, valor in c.items():
            print(f'{chave} = {valor}; ', end = '')
print()
print('>>> ENCERRADO <<<')
'''