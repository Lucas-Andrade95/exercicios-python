#PROGRESSÃO ARITMÉTICA

print('''=====================================
10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA!
=====================================''')
a = int(input('Digite o primeiro termo da Progressão Aritmética: '))
n = int(input('Digite a razão da P.A.: '))
print(a)
for c in range(0,9):
    a += n
    print(a)
print('FIM')
