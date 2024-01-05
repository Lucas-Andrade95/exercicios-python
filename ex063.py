#SEQUÊNCIA DE FIBONACCI
t1 = 0
t2 = 1

n = int(input('Quantos elementos da sequência de Fibonacci você quer? '))
c = 0

while c < n:
    t3 = t1 + t2
    print(t1)
    t1 = t2
    t2 = t3
    c = c + 1
print('Fim')
   
