from modulos import *

def Interface():
    # Página de início no Robo de investimentos
    print('\033[1;32m$\033[m' * 40)
    print(f'\033[1;32m$\033[m      \033[1;36mAvaliador de Investimentos      \033[1;32m$\033[m')
    print('\033[1;32m$\033[m' * 40)
    print()
    print('\033[1;32m=\033[m' * 60)
    print('Digite \033[1;36m1\033[m para analisar uma carteira de investimentos \nDigite \033[1;31m2\033[m para sair')
    print('\033[1;32m=\033[m' * 60)

    # O que o usuário deseja fazer
    while True:
        opcao = int(input('\033[1;36mO que você deseja fazer? \033[m'))
        if opcao == 1:
            # Usuario informa a url do site onde a carteira está
            url = str(input('\033[1;35mInforme a url da Carteira: \033[m'))
            
            # Variável 'carteira' recebe uma lista com os resultados do scrapping da url
            carteira = scrapping.encontrar(url)
            # Variável 'carteira_cotacoes' recebe uma lista que contem uma lista com as cotações das moedas e outra com as das ações
            carteira_cotacoes = cotacao.cotacao(carteira)
        
            # Usuário escolhe um nome para o arquivo Excel com as Análises
            nome_excel = str(input('\033[1;35mDigite um nome para a sua Carteira: \033[m'))
            # Salvar o arquivo excel com a análise de investimentos
            excel.dashboard(carteira, carteira_cotacoes, nome_excel)
            print(f'{nome_excel} \033[1;33mfoi criado(a) com sucesso!\033[m')
        elif opcao == 2:
            break
        else:
            print('\033[1;31mOpção inválida, tente novamente.\033[m')
    print('Encerrando o programa...')
