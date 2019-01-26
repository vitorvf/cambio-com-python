import requests
import json

def main():
    cambio_dollar(None)
    cambio_euro(None)

def cambio_dollar(url):
    #Se o usuário não passar nenhuma URL, vai entrar no IF e será atribuida
    #a variável URL o endereço abaixo
    if url is None:
        url = "http://data.fixer.io/api/latest?access_key=65c2c5494f5a965219e5a0d3568300e4&format=1"
    response = requests.get(url)
    if response.status_code == 200:
        print("Conseguiu se conectar...")
        dados = response.json()
        taxa_usd = dados['rates']['USD']
        taxa_brl = dados['rates']['BRL']
        real = taxa_brl/taxa_usd
        print("O dólar está custando %.2f reais " % real)
    else:
        print("Site com algum problema!")

def cambio_euro(url):
    if url is None:
        url = "http://data.fixer.io/api/latest?access_key=65c2c5494f5a965219e5a0d3568300e4&format=1"
    response = requests.get(url)
    if response.status_code == 200:
        print("Conseguiu se conectar...")
        dados = response.json()
        taxa_eur = dados['rates']['EUR']
        taxa_brl = dados['rates']['BRL']
        real = taxa_brl/taxa_eur
        print("O euro está custando %.2f reais " % real)
    else:
        print("Site com algum problema!")

#Pede para que o programa execute a nossa função main
if __name__ == '__main__':
    main()
