#CÓDIGO CRIADO PELO CHATGPT 3.5!!!

'''# Inicializando a variável para armazenar o sexo
sexo = ''

# Enquanto o sexo não for 'M' ou 'F', continuará pedindo a entrada correta
while sexo != 'M' and sexo != 'F':
    sexo = input("Digite o sexo (M/F): ").upper()  # Lê a entrada e converte para maiúsculas

    # Verifica se o valor é válido
    if sexo != 'M' and sexo != 'F':
        print("Valor inválido! Digite apenas 'M' para masculino ou 'F' para feminino.")

# Mostra o sexo válido
print("Sexo digitado:", sexo)'''

#VALIDAÇÃO DE DADOS USANDO WHILE
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper() [0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos! Informe seu sexo: [M/F] ')).upper().strip() [0]
print(f'Sexo {sexo} registrado com sucesso!')
