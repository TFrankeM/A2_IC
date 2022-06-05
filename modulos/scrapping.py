import requests
from bs4 import BeautifulSoup

# Função que divide 'lista_moedas' e em uma com nomes e outra com quantidades. O mesmo para 'lista_acoes'
def organizar(lista_moedas, lista_acoes):
    # A variável 'carteira' é uma lista que recebe as listas 'nome_moeda', 'quantidade_moeda', 'nome_acao'
    # e 'quantidade_acao' e "entrega" para a interface)
    carteira = []
    # Recebemos uma lista com moedas e quantidade, convertemos para duas listas, uma com nome da moeda e outra com quantidade:
    nome_moeda = []
    quantidade_moeda = []

    for posicao, valor in enumerate(lista_moedas):
        if posicao % 2 == 0:
            nome_moeda.append(valor)
        else:
            quantidade_moeda.append(float(valor))
    carteira.append(nome_moeda)
    carteira.append(quantidade_moeda)   

    # Recebemos uma lista com ações e quantidade, convertemos para duas listas, uma com nome da ação e outra com quantidade:
    nome_acao = []
    quantidade_acao = []

    for item in lista_acoes:
        if lista_acoes.index(item) % 2 == 0:
            nome_acao.append(item) 
        else:
            quantidade_acao.append(float(item))
    carteira.append(nome_acao)
    carteira.append(quantidade_acao)        
    return carteira

# Função para encontrar as tabelas de moedas e ações 
def encontrar(url):
    site = requests.get(url)
    soup = BeautifulSoup(site.content, 'html.parser')
    moedas = soup.find_all('div', class_='moeda')
    acoes = soup.find_all('div', class_='acao')

    # Extraindo apenas as listas de moedas e de ações
    lista_moedas = []
    lista_acoes = []

    for moeda in moedas:
        cada_moeda = moeda.find_all('td')
        lista_moedas.append(cada_moeda)
    for acao in acoes:
        cada_acao = acao.find_all('td')
        lista_acoes.append(cada_acao)

    # 'Lista_moedas' é, originalmente, uma lista com vários itens, pegamos apenas o primeiro deles e aplicamos na mesma variável 
    lista_moedas = lista_moedas[0]
    lista_acoes = lista_acoes[0]

    # Adiciona à 'lista_moedas' e à 'lista_acoes' apenas o texto das celulas das tabelas (sem tags html)
    for posição, item in enumerate(lista_moedas):
        lista_moedas[posição] = item.text.strip()

    for posição, item in enumerate(lista_acoes):
        lista_acoes[posição] = item.text.strip()
    return organizar(lista_moedas, lista_acoes)

