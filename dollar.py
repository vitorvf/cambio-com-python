import requests
import json
import pandas as pd

def main():
    dollar = cambio_dollar()
    euro = cambio_euro()
    print(euro)
    exportar_csv(dollar, euro)

def cambio_dollar(url = "http://data.fixer.io/api/latest?access_key=65c2c5494f5a965219e5a0d3568300e4&format=1"):
    #Se o usuário não passar nenhuma URL, vai entrar no IF e será atribuida
    #a variável URL o endereço abaixo
    response = requests.get(url)
    if response.status_code == 200:
        print("Conseguiu se conectar...")
        dados = response.json()
        taxa_usd = dados['rates']['USD']
        taxa_brl = dados['rates']['BRL']
        real = taxa_brl/taxa_usd
        real = round(real, 2)
        return real
    else:
        print("Site com algum problema!")

def cambio_euro(url = "http://data.fixer.io/api/latest?access_key=65c2c5494f5a965219e5a0d3568300e4&format=1"):
    response = requests.get(url)
    if response.status_code == 200:
        print("Conseguiu se conectar...")
        dados = response.json()
        taxa_eur = dados['rates']['EUR']
        taxa_brl = dados['rates']['BRL']
        real = taxa_brl/taxa_eur
        real = round(real, 2)
        print(real)
        return real
    else:
        print("Site com algum problema!")

def exportar_csv(dollar, euro):
    print(euro)
    linha = {'Dollar - USD': [dollar], 'Euro - EUR': [euro]}
    frame = pd.DataFrame(linha, columns = ['Dollar - USD', 'Euro - EUR'])
    frame.to_csv('mo.csv')
    print('dados salvo na tabela!')

#Pede para que o programa execute a nossa função main
if __name__ == '__main__':
    main()
