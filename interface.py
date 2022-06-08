from modulos import *

def Interface():
    # Página de início no Robo de investimentos

    print('*' * 40)
    print(f'       Avaliador de Investimentos       ')
    print('*' * 40)
    print()
    print('*' * 60)
    print('Digite 1 para analisar uma carteira de investimentos \nDigite 2 para sair')
    print('*' * 60)

    # O que o usuário deseja fazer
    while True:
        opcao = int(input('O que você deseja fazer: '))
        if opcao == 1:
            # Usuario informa a url do site onde a carteira está
            url = str(input('Informe a url da Carteira: '))
            
            # Variável 'carteira' recebe uma lista com os resultados do scrapping da url
            carteira = scrapping.encontrar(url)
            # Variável 'carteira_cotacoes' recebe uma lista que contem uma lista com as cotações das moedas e outra com as das ações
            carteira_cotacoes = cotacao.cotacao(carteira)
        
            # Usuário escolhe um nome para o arquivo Excel com as Análises
            nome_excel = str(input('Digite um nome para a sua Carteira: '))
            # Salvar o arquivo excel com a análise de investimentos
            excel.dashboard(carteira, carteira_cotacoes, nome_excel)
            print(f'{nome_excel} foi criado(a) com sucesso!')
        elif opcao == 2:
            break
        else:
            print('Opção inválida, tente novamente.')
    print('Encerrando o programa...')
