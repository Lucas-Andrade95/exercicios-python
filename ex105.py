#NOTAS

def notas(*numero, sit=False):
    """
    ---> Lê uma quantidade infinita de notas de alunos e retorna um dicionário com informações relevantes.
    Parâmetro1: *numero --> Recebe as notas dos alunos
    Parâmetro2: sit = False --> Opcional. Caso deseja saber a situação da classe (RUIM, RAZOÁVEL, BOA) defina True
    A função insere as notas em uma lista, calcula a soma e a média das notas e retorna um dicionário com as informações:
    'total': Total de Notas inseridas
    'maior': Maior nota inserida
    'menor': Menor nota inserida
    'media': Media das notas inseridas
    'situacao':  Situação da classe (BOA, RAZOÁVEL, RUIM), se Parâmetro2 = True.
    """

    lista = [numero]
    soma = 0
    for c in numero:
        soma += c
    media = soma / len(numero)
    dicionario = {
        'total': len(numero),
        'maior': max(numero),
        'menor': min(numero),
        'média': media
    }
    if sit == True:
        if media < 6:
            dicionario['situacao'] = 'RUIM'
        elif 6 <= media < 7:
            dicionario['situacao'] = 'RAZOÁVEL'
        elif media >= 7:
            dicionario['situacao'] = 'BOA'
    return dicionario

resp = notas(5, 9.6, 8.5)
print(resp)
