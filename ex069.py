#IDADE E SEXO
maiorde18 = homens = novinhas = 0

while True:
    print('------CADASTRO GERAL------')
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F]: ').upper().strip() [0]
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F]: ').upper().strip() [0]
    if idade > 18:
        maiorde18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20: 
        novinhas += 1
    print('-'*25)
    continua = str(input('Quer continuar? [S/N]: ')).upper().strip() [0]
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]: ')).upper().strip() [0]
    if continua == 'N':
        break
print(f'''===FIM DO PROGRAMA===
Total de pessoas com mais de 18 anos: {maiorde18}
Ao todo temos {homens} homens cadastrados.
E temos {novinhas} mulher(es) com menos de 18 anos.''')

    
