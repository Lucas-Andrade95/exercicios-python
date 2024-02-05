# MINI SISTEMA DE CADASTRO

# IMPORTANDO AS FUNÇÕES
from uteis import texto

#CRIANDO ARQUIVO, SE AINDA NÃO EXISTIR
arq = 'cadastros.txt'
if not texto.arquivoexiste(arq):
    texto.CriarArquivo('cadastros.txt')

#PROGRAMA PRINCIPAL
while True:
    resposta = texto.menu(['Lista de Cadastros', 'Novo Cadastro', 'Encerrar programa',])
    if resposta == 1:
        texto.lerArquivo(arq)

    elif resposta == 2:
        texto.mensagem('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = texto.leiaint(input('Idade: '))
        texto.cadastrar(arq, nome, idade)

    elif resposta == 3:
        texto.mensagem('Encerrando sistema')
        break
    else:   
        print('ERRO! Digite um valor válido! ')






