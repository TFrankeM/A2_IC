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
        # Para encontrar a cotação da moeda, o nome dela deve ser seguido por 'BRX=X' exceto quando a moeda for o Real
        if nome_moeda != "BRL":
            nome_moedas = yf.Ticker(f"{nome_moeda}BRX=X ")
            informacoes = nome_moedas.info
            # Pega a cotação da moeda e armazena em uma lista
            cotacoes_moedas.append(informacoes['regularMarketPrice'])
        else:
            cotacoes_moedas.append(1)

    cotacoes_carteira.append(cotacoes_moedas)

        # Cotação das ações
    # A lista abaixo armazena as cotações das ações
    cotacoes_acoes = []
    for nome_acao in carteira[2]:
        empresa = yf.Ticker(f"{nome_acao}")
        informacoes = empresa.info
        moeda = informacoes['currency']
        valor_acao = informacoes['regularMarketPrice']
        # Se a ação da empresa está em real, basta adicioná-la à lista 'cotacoes_acoes'
        if moeda == "BRL":
            cotacoes_acoes.append(valor_acao)
        # Se a ação da empresa não está em real, é preciso multiplicar a cotação da ação pela cotação da moeda da ação
        if moeda != "BRL":
            nome_para_buscar = (f"{moeda}BRL=X")
            info_da_moeda_buscar = yf.Ticker(nome_para_buscar)
            info_moeda = info_da_moeda_buscar.info
            cotacao_em_real = info_moeda['regularMarketPrice']
            valor_acao_em_real = valor_acao * cotacao_em_real
            cotacoes_acoes.append(round(valor_acao_em_real,2))

    cotacoes_carteira.append(cotacoes_acoes)
    return cotacoes_carteira
