#IMC

nome = str(input('Nome Completo: '))
altura = float(input('Altura (m): '))
peso = float(input('Peso (Kg): '))
imc = float(peso / (altura ** 2))
print ('IMC = {:.1f}'.format(imc))

if imc < 18.5:
    print ('{}, você está abaixo do peso ideal.'.format(nome))
elif 18.5 < imc <= 25:
    print ('{}, você está no peso ideal! Parabéns!'.format(nome))
elif 25 < imc <= 30:
    print ('{}, você está com sobrepeso! Trate de emagrecer enquanto é fácil.'.format(nome))
elif 30 < imc <= 40:
    print ('{}, você está obeso! Faça dieta e exercícios.'.format(nome))
else:
    print ('{}, você está com obesidade mórbida! Seu caso é grave.'.format(nome))

print('The End')
