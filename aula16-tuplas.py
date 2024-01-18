lanche = 'burguer', 'pudim', 'suco', 'pizza', 'sorvete', 'orange'
#print(lanche[-1]) PEGA O ÚLTIMO

for c in lanche:
    print(f'Eu vou comer {c}')


for c in range(0,len(lanche)):
    print(f'''I'm gonna eat {lanche[c]} na posição {c}''')


for posição, c in enumerate(lanche):   #ENUMERA AS POSIÇÕES EM LANCHE
    print(f'eu vou comer {c} na posição {posição}')

print(sorted(lanche)) #MOSTRA EM ORDEM ALFABÉTICA

#CONCATENANDO TUPLAS
tupla1 = 1, 2, 5, 6
tupla2 = 6, 9, 7
concatenando = tupla1 + tupla2
print(concatenando)

#CONTANDO QUANTOS NÚMEROS 6 TEMOS NA TUPLA 'CONCATENANDO' com o .count()
print(f'Temos {concatenando.count(6)} números 6 ')

#MOSTRANDO EM QUAL POSIÇÃO ESTÁ COM O .index()
print('O suco está na posição', lanche.index('suco'))
