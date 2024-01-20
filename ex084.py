#EXERCÍCIO DE LISTAS DENTRO DE LISTAS - NOME E PESO

listageral = []
maiorpeso = menorpeso = 0


print('- - - - CADASTRO GERAL - - - - ')
while True:

    pessoa = [
        str(input('Nome: ')),
        int(input('Peso(Kg): ')) 
        ]
    if len(listageral) == 0:
        maiorpeso = menorpeso = pessoa[1]
    else:
        if pessoa[1] > maiorpeso:
            maiorpeso = pessoa[1]
  
        if pessoa[1] < menorpeso:
            menorpeso = pessoa[1]

    listageral.append(pessoa[:])
    

    fim = input('Deseja Continuar? [S/N]: ').upper().strip() [0]
    print('-'*30)
    if fim not in 'SN':
        fim = input('Digite Sim ou Não: ').strip().upper() [0]
    if fim == 'N':
        break



    
print(f'Foram cadastradadas {len(listageral)} pessoas')
print(f'O maior peso foi de {maiorpeso}Kg. Peso de...', end='')
for cada_um in listageral:
    if cada_um[1] == maiorpeso:
        print(f' {cada_um[0]} ', end='')
print(f"\nO menor peso foi de {menorpeso}Kg. Peso de... ", end='')
for cada_um in listageral:
    if cada_um[1] == menorpeso:
        print(f' {cada_um[0]} ', end='')