#IDENTIFICANDO VOGAIS

palavras = 'python', 'programação', 'escola', 'listas', 'tuplas', 'codando', 'aprendizado', 'tecnologia'

for c in palavras:
    print(f'\nNa palavra {c} temos as vogais ', end = '')
    for letra in c:
        if letra in 'aeiou':
            print(f' {letra}', end='')
            