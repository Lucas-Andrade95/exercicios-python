
#ESTRUTURA CONDICIONAL ANINHADA!

nome = str(input('Qual o seu nome? '))

if nome == 'Lucas':
    print('Que nome lindo!')
elif nome == 'Maria' or nome == 'João' or nome == 'Pedro' or nome == 'Paulo':
    print('Seu nome é bíblico!')
elif nome == 'William' or nome == 'James' or nome == 'John':
    print('Seu nome é estrangeiro! Uia! Que chic!')
elif nome in 'Ana Cláudia Jéssica Juliana Flávia Carolina':
    print('Seu nome é feminino!')
else:
    print('Seu nome é bem normal')

print('Tenha um bom dia!')