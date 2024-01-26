def dicionario():
    while True:
        print('-----PYHELP-----')
        funcao = input('Função ou Biblioteca >>> ')
        if funcao == 'fim':
            break
        else:
            help(funcao)
    
dicionario()