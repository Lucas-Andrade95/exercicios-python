#ELE VOTA OU NÃO VOTA!?
from funcoes import mensagem, mostralinha

def voto(anodenascimento):
    from datetime import date
    idade = date.today().year - anodenascimento
    if 16 <= idade < 18 or idade > 65:
        return (f'{idade} anos de idade. Situação: OPCIONAL')
    elif 18 <= idade < 65:
        return (f'{idade} anos de idade: Situação: OBRIGATÓRIO ')
    elif idade < 16:
        return (f'{idade} anos de idade: Situação: PROIBIDO')

mensagem('SITUAÇÃO ELEITORAL')

nome = input('Nome: ')
ano = int(input('Ano de nascimento: '))
mostralinha()
print(f'{nome} tem {voto(ano)}')

