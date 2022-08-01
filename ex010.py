#CALCULO DE USO DE TINTA
altura = float(input('Altura da parede em metros: '))
comprimento = float(input('Comprimento da parede em metros: '))
area = altura*comprimento
tinta = area/2
print('Você irá precisar de {} litros de tinta para pintar toda a parede.'.format(tinta))
