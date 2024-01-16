#LOOP INFINITO / COMANDO BREAK

cont = 1
while True:
    print(cont)
    cont += 1
    if cont == 1000:
        break
print('Fim')