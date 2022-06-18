import yfinance as yf

        # BUSCAR COTAÇÃO

def cotacao(carteira):
    # A variável 'cotacoes_carteira' é uma lista que recebe as listas 'cotacoes_moedas' e 'cotacoes_acoes'
    # e "entrega" para a interface)
    cotacoes_carteira = []
    
        # Cotação das moedas
    # A lista abaixo armazena as cotações das moedas
    cotacoes_moedas = []
    for nome_moeda in carteira[0]:
        # Se a moeda tem nome diferente de "BRL" ou "BRL=X", pesquisamos a cotação
        if nome_moeda != "BRL" and nome_moeda != "BRL=X":
            nome_moedas = yf.Ticker(nome_moeda)
            informacoes = nome_moedas.info
            # Caso a moeda não exista ou não seja encontrada, adiciona-se zero na lista
            if informacoes['regularMarketPrice'] == None:
                cotacoes_moedas.append(0)
            # Caso a moeda seja encontrada, pega a cotação da moeda e armazena na lista
            else:
                cotacoes_moedas.append(informacoes['regularMarketPrice'])
        # Se a moeda for o Real, adicionamos 1
        else:
            cotacoes_moedas.append(1)
    # Adicionar as cotações em uma outra lista que será devolvida para a interface 
    cotacoes_carteira.append(cotacoes_moedas)

        # Cotação das ações
    # A lista abaixo armazena as cotações das ações
    cotacoes_acoes = []
    for nome_acao in carteira[2]:
        empresa = yf.Ticker(nome_acao)
        informacoes = empresa.info
        moeda = informacoes['currency']
        valor_acao = informacoes['regularMarketPrice']
        # Se a ação da empresa está em real, basta adicioná-la à lista 'cotacoes_acoes'
        if moeda == "BRL":
            cotacoes_acoes.append(valor_acao)
        # Se a ação da empresa não está em real, é preciso multiplicar a cotação da ação pela cotação da moeda da ação
        if moeda != "BRL":
            # Se a ação não foi encontrada, adicionamos 0
            if valor_acao == None:
                cotacoes_acoes.append(0)
            else:    
                nome_para_buscar = (f"{moeda}BRL=X")
                info_da_moeda_buscar = yf.Ticker(nome_para_buscar)
                info_moeda = info_da_moeda_buscar.info
                cotacao_em_real = info_moeda['regularMarketPrice']
                valor_acao_em_real = valor_acao * cotacao_em_real
                cotacoes_acoes.append(round(valor_acao_em_real,2))
    # Adicionar as cotações em uma outra lista que será devolvida para a interface
    cotacoes_carteira.append(cotacoes_acoes)
    return cotacoes_carteira
