#FATIAMENTO DE STRING
frase = input('Nome: ')
print(frase.upper())
print(frase.lower())
frase1 = frase.strip()
print('Seu nome tem {} letras'.format(len(frase1)))
frase2 = frase.split()
print('Seu primeiro nome tem {} letras'.format(len(frase2[0])))

