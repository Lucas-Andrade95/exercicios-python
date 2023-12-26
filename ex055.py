#MAIOR E MENOR PESO
maispesado = 0
maisleve = 0
for x in range(1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(x)))
    if x == 1:
        maispesado = peso
        maisleve = peso
    else:
        if peso > maispesado:
            maispesado = peso
        elif peso < maisleve:
            maisleve = peso
    
print('O maior peso é {}, e o menor peso é {}'.format(maispesado,maisleve))
