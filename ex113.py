def leiaint():
    while True:
        try:
            n = input('Digite um valor inteiro: ')
            n = int(n)
            return n
        except (KeyboardInterrupt):
            print('O usuário preferiu não informar nenhum número.')
            return 0
        except:
            print('Erro! Por favor digite um número inteiro válido. ')



def leiafloat():
    while True:
        try:
            n = input('Digite um valor real: ').replace(',','.')
            n = float(n)
            return n
        except KeyboardInterrupt:
            print('O usuário preferiu não informar nenhum número.')
            return 0
        except:
            print('Erro! Por favor digite um número válido.')
        else:
            return n

#PROGRAMA PRINCIPAL

x = leiaint()
y = leiafloat()

print(f'Você digitou o valor inteiro {x} e o valor real {y}!')
