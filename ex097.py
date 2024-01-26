def mensagem(msg):
    a = len(msg) + 10
    b = len(msg)
    print('-'*a)
    print(' '*b, f'{msg}')
    print('-'*a)

mensagem('Cursinho')