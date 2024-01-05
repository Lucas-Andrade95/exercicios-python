from datetime import datetime

# Obtendo a data de nascimento do usuário
data_nascimento = input("Digite sua data de nascimento (formato: DD/MM/AAAA): ")

# Convertendo a string para um objeto datetime
data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')

# Obtendo a data atual
data_atual = datetime.now()

# Calculando a diferença entre as datas para obter a quantidade de dias vividos
dias_vividos = (data_atual - data_nascimento).days

print(f"Você viveu {dias_vividos} dias até hoje.")
