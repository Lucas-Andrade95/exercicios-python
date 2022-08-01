#CALCULO DE HIPOTENUSA
import math
cato = float(input('Cateto Oposto: '))
cata = float(input('Cateto Adjacente: '))
hipotenusa = math.hypot(cato, cata)
print ('A hipotenusa mede {:.2f}'.format(hipotenusa))
