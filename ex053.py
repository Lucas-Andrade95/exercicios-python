#É UM PALÍNDROMO?
frase = str(input('Digite uma frase: ')).strip().upper().replace(" ","")

inverso = ''
for letra in range(len(frase) - 1, -1, -1):
    inverso += frase[letra]
if inverso == frase:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo...')
    