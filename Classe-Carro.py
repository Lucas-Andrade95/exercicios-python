class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print(f"O {self.marca} {self.modelo} de {self.ano} foi ligado.")

    def desligar(self):
        self.ligado = False
        print(f"O {self.marca} {self.modelo} de {self.ano} foi desligado.")

# Lista para armazenar os objetos Carro criados
lista_carros = []

while True:
    marca = input("Insira a marca do carro (ou 'sair' para encerrar): ")
    if marca.lower() == 'sair':
        break

    modelo = input("Insira o modelo do carro: ")
    ano = input("Insira o ano do carro: ")

    # Criando um novo objeto Carro com os atributos fornecidos pelo usuário
    novo_carro = Carro(marca, modelo, ano)
    lista_carros.append(novo_carro)

# Exibindo informações dos carros criados
for idx, carro in enumerate(lista_carros, start=1):
    print(f"\nCarro {idx}:")
    print(f"Marca: {carro.marca}")
    print(f"Modelo: {carro.modelo}")
    print(f"Ano: {carro.ano}")
