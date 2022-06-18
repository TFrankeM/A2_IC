# Introducao a Computacao_A2

  Este projeto tem por finalidade saber quanto que uma pessoa tem investido em dois tipos de ativos, moedas e ações. Para isso usamos _webscrapping_ para retirar de uma carteira fictícia online os nomes e as quantidades de cada ativo que aquela carteira contém. Após termos em mãos os nomes e as quantidades de cada ativo utilizamos a 
biblioteca _yfinance_ do python para buscarmos no site _Yahoofinance_ as cotações, ou seja quanto que um determinado ativo vale em Real(R$). 

  Após essa etapa chegamos a parte final, que é criar um _Dashboard_, e para isso usamos a biblioteca _Openpyxl_. Nosso _Dashboard_ contém duas tabelas, uma para cada tipo de ativo. Nessas tabelas temos o nome de cada ativo, quantidade, cotação e o total em real. Temos também no mesmo _Dashboard_ 3 gráficos. O primeiro é em relação ao ativo moedas, ele representa a quantidade de uma moeda em relação ao total que a carteira tem daquela moeda, isso para cada moeda diferente que temos naquela carteira. O segundo gráfico é em relação ao ativo ações, nele representamos a porcentagem de cada ação em relação ao valor total do ativo dessa modalidade. E o terceiro gráfico é em relação ao valor total da carteira, nesse gráfico mostramos a quantidade de cada ativo separadamente em relação ao valor total da carteira. Por último temos um QRCODE 
que contém o valor total da carteira, ou seja a soma de todos os ativos dos dois tipos em real.

# Segue abaixo o link com as nossas carteiras

https://tfrankem.github.io/A2_IC/index.html
