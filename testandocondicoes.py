#NOTAS DA ESCOLA
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print ('Sua média é {:.1f}!'.format(m))

#CONDIÇÃO COMPOSTA

#if m >=7:
#    print('Sua média é boa, PARABÉNS!')
#else:
#    print('Você não estudou hein, vai repetir de ano!')

#CONDIÇÃO SIMPLIFICADA
print('Parabéns!' if m >=7 else 'Você é burro')
print('--FIM--')