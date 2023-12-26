maisvelho = 0
somaidades = 0
menosde20 = 0
homens = 0

for x in range(1,5):
    print('------{}ª PESSOA------'.format(x))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    if sexo == 'M':
            somaidades += idade
            homens += 1
    if sexo == 'M' and idade > maisvelho:
          maisvelho = idade
          nomedomaisvelho = nome
    if sexo == 'F' and idade < 20:
          menosde20 += 1
          
mediaidade = somaidades / homens

print('-' *20)
print('A média de idade entre os homens é de {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maisvelho,nomedomaisvelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(menosde20))
            
