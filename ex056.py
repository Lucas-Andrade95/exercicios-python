#COLETANDO E ANALISANDO DADOS

#VARIÁVEIS:
maisvelho = 0
somaidades = 0
menosde20 = 0
homens = 0

#ESTRUTURA DE REPETIÇÃO COM FOR (váriável de controle):
for x in range(1,5):
    print('------{}ª PESSOA------'.format(x))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()

    #ESTRUTURA CONDICIONAL DENTRO DO LAÇO DE REPETIÇÃO
    if sexo == 'M':
            somaidades += idade # QUE É IGUAL A: somaidades = somaidades + idade (ESTRUTURA SOMATÓRIA)
            homens += 1         # QUE É IGUAL A: homens = homens + 1 (ESTRUTURA CONTADORA)
    if sexo == 'M' and idade > maisvelho:
          maisvelho = idade
          nomedomaisvelho = nome
    if sexo == 'F' and idade < 20:
          menosde20 += 1
          
mediaidade = somaidades / homens

#MOSTRANDO OS RESULTADOS: 
print('-' *20)
print('A média de idade entre os homens é de {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maisvelho,nomedomaisvelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(menosde20))
            
