#Progresso Aritmética

print('''=====================================
10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA!
=====================================''')

a = int(input('Digite o primeiro termo da Progressão Aritmética: '))
n = int(input('Digite a razão da P.A.: '))
c = 1
r = False
z = 1


print(a)
while c < 10:
    a += n
    c +=1
    print(a)

while r == False:
    z = int(input('Gostaria de ver mais quantos termos? '))
    c = 0
    if z != 0:
        while c < z:
            a += n
            c += 1
            print (a)
    else:
        r = True
print('Fim')