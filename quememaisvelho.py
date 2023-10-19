#QUEM É MAIS VELHO?

print('='*70)
print('QUEM É MAIS VELHO?')
nome1 = str(input('Nome: '))
birth1 = int(input('Ano de Nascimento:'))
nome2 = str(input('Nome: '))
birth2 = int(input('Data de nascimento: '))

if birth1 < birth2:
    #print( nome1, ' é mais velho do que', nome2)
    print('{} é mais velho(a) do que {}!'.format(nome1,nome2))
else:
    #print(nome2,' é mais velho(a) do que ', nome1)
    print('{} é mais velho(a) do que {}'.format(nome2, nome1))

print('='*70)
print('FIM')

