#LOJA
soma = contador = maisbarato = maisdemilreais = 0
nomedoprodutomaisbarato = '-'

print('-'*25)
print('ATACADÃO TEND-TUDO')
print('-'*25)

while True:
    produto = str(input('Nome do produto: '))
    preço = int(input('Preço: R$ '))
    soma += preço
    contador += 1
    if contador == 1:
        maisbarato = preço
        nomedoprodutomaisbarato = produto
    if preço > 1000:
        maisdemilreais += 1
    if preço < maisbarato:
        maisbarato = preço
        nomedoprodutomaisbarato = produto
    fim = ' '
    while fim not in 'SN':
        fim = str(input('Quer continuar? [S/N]: ')).strip().upper() [0]
    print('-'*25)
    if fim == 'N':
        break

print('---FIM DO PROGRAMA---')
print(f'''O total da compra foi de R$ {soma}.
Temos {maisdemilreais} produtos custando mais de R$ 1000,00 
O produto mais barato foi {nomedoprodutomaisbarato} que custa R$ {maisbarato}''')
