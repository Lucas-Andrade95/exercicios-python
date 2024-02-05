def menu(lista):
    print('-' * 50)
    print(f'                     MENU')
    print('-' * 50)
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print('-' * 50)
    opc = leiaint(input('Sua opção: '))
    return opc


def leiaint(n):
    while True:
        try:
            n = int(n)
            return n
        except (KeyboardInterrupt):
            print('O usuário preferiu não informar nenhum número.')
            return 0
        except:
            print('Erro! Por favor digite um número inteiro válido. ')


def opção():
    while True:
        try:
            opção = int(input('Sua opção: '))
            while opção not in (1,2,3):
                opção = int(input('Digite uma opção válida: '))
            return opção
        except:
            print('Erro! Digite uma opção válida.')

def mensagem(msg):
    '''
    Imprime uma mensagem de título entre linhas tracejadas
    '''
    a = len(msg) + 20
    print('-'*a)
    print(f'          {msg}')
    print('-'*a)

def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
        return True
    except:
        return False

def CriarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()  
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler arquivo')
    else:
        mensagem('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}  {dado[1]:>3}')
    finally:
        a.close()

def cadastrar(arquivo, nome='unknown', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Houve um erro ao abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao inserir dados no arquivo.')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso!')
            a.close()