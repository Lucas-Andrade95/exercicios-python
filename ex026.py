#LENDO UMA STRING E IDENTIFICANDO A POSIÇÃO DE UMA DETERMINADA LETRA
frase = str(input('Escreva uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição ', frase.find('A')+1)
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))
