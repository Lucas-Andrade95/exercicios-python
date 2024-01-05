import random

# Gera um número aleatório entre 0 e 10
numero_aleatorio = random.randint(0, 10)

# Inicializa o contador de tentativas
tentativas = 0
adivinhou = False

while not adivinhou:
    # Solicita que o usuário faça uma tentativa
    tentativa = int(input("Tente adivinhar o número entre 0 e 10: "))
    
    # Incrementa o contador de tentativas
    tentativas += 1
    
    # Verifica se a tentativa é igual ao número aleatório
    if tentativa == numero_aleatorio:
        print("Parabéns! Você acertou o número", numero_aleatorio, "em", tentativas, "tentativa(s)!")
        adivinhou = True
    else:
        print("Tente novamente!")

