#Analisando os parenteses
expressão = str(input('Digite uma expressão: '))
pilha = list()
for c in expressão:
    if c == '(':
        pilha.append(c)
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')


