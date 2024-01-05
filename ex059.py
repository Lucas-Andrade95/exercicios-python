#CALCULADORA (QUASE) INTELIGENTE

#DECLARANDO VARIÁVEIS:
n1 = 0
n2 = 0
escolha = 0
fim = False
soma = 0
multiplica = 0

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

#ESTRUTURA DE REPETIÇÃO COM TESTE LÓGICO

while not fim:

    #MENU
    escolha = int(input('''O que você quer fazer? 
                        
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    
    Sua escolha: ''' )) 
    if escolha == 5:
        fim = True
        print('Obrigado e volte sempre!')
    else:
        if escolha == 1:
            soma = n1 + n2
            print('{} + {} = {}'.format(n1, n2, soma))
        elif escolha == 2:
            multiplica = n1 * n2
            print('{} x {} = {}'. format(n1, n2, multiplica))
        elif escolha == 3:
            if n1 > n2:
                print('{} é maior que {}.'.format(n1, n2))
            else:
                print('{} é maior que {}'.format(n2, n1))
        elif escolha == 4:
            print('Ok, vamos lá... ')
            n1 = float(input('Digite um número: '))
            n2 = float(input('Digite outro número: '))
        else:
            print('Por favor, digite um número válido.')
print('Fim')


            
            