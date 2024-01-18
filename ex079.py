lista = []
valor = 0
fim = 'S'
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar... ')
    fim = str(input('Deseja continuar? [Sim/Não]: ')).strip().upper() [0]
    if fim not in 'SN':
        fim = str(input('Sou uma máquina, só entendo se você responder Sim ou Não: '))
    if fim == 'N':
        break
lista.sort()
print('-' * 30)
print(f'Você digitou os valores {lista}')