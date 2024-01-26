#FUNÇÃO FATORIAL COM PARÂMETRO OPCIONAL

def fatorial(n, show=False):
    """
    Calcula o Fatorial de um número inteiro.
    Parâmetro1: Número inteiro a ser calculado o fatorial. Retorna um número inteiro.
    Parâmetro2: Opcional. False por padrão. Se True imprime a sequência de números multiplicados na tela
    e seu resultado em uma string, retornando 'None'.
    """
    f = 1
    if show == False:
        for c in range(n, 0, -1):
            f = f * c
        return f
    else:
        for c in range(n, 0, -1):
            f = f * c
            if c > 1:
                print(f' {c} x', end='')
            elif c == 1:
                print(f' 1 = {f}')
        

numero = int(input('Digite um número: '))
print(fatorial(numero,True))
