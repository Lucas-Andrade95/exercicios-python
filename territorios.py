#TERRITÓRIOS DA LS
geral = []

print('-----TERRITÓRIOS LS CAMPO GRANDE-----')
menu = int(input('''
1) NOVO TERRITÓRIO
2) EDITAR TERRITÓRIO
3) EXCLUIR TERRITÓRIO
4) LISTA DE TERRITÓRIOS
---> '''))

if menu == 1:
    cont = 0
    while True:
        territorio = {
            'código': cont,
            'endereço': input('Endereço: '),
            'região': input('Região: '),
            'observação': input('Observação: ')
        }
        geral.append(territorio)
        cont = cont + 1
        fim = input('Deseja cadastrar outro território? [S/N]: ').upper().strip()
        while fim not in 'SN':
            fim = input('Sim ou Não? [S/N]: ').strip().upper()
        if fim == 'N':
            break
for c, d in enumerate(geral):
    print(c, d, end='')
