#VERIFICANDO SE O SITE DO PUDIM ESTÁ ACESSÍVEL
import requests

try:
    requests.get('http://pudim.com.br')
except:
    print('O site do Pudim NÃO está acessível!')
else:
    print('O site do Pudim está acessível!')

