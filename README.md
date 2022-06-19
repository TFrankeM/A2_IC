<h1 align="center">Introdução à Computação A2</h1>
<h2 align="center">Robô de Avaliação de Portfólio de Investimentos</h2>
<p>
Este projeto tem por finalidade avaliar a configuração dos “ativos”, distribuídos em carteiras de investimentos. Os ativos, representados por “moedas e ações”, foram cotados de acordo com mercado e, a partir dessas informações, foram criados gráficos que permitem auxiliar na gestão dos investimentos. Para uma melhor avaliação, o trabalho foi dividido em três módulos, que estão dentro da pasta “módulos”, um arquivo interface que conecta esses módulos e um arquivo main –  é por esse arquivo que o código deve ser rodado.
</p>

<h3>Web Scraping</h3>
<p>
Essa fase consiste na retirada dos dados de carteiras fictícias de investimentos da web, convertendo-os em informações estruturadas para posterior análise. Para tanto, foram utilizadas as bibliotecas requests e o pacote <i>Beautiful Soup</i> da biblioteca <i>bs4</i>.
A seguir, o link das carteiras de investimentos:
</p>
<p align="center">https://tfrankem.github.io/A2_IC/index.html</p>

<h3>Cotação</h3>
<p>
Uma vez obtidos os nomes e as quantidades de cada ativo, utilizamos a biblioteca <i>yfinance</i> do pyhon para buscarmos no site <i>Yahoofinance</i> as cotações, ou seja; quanto que um determinado ativo vale em Real (R$).
</p>

<h3>Dashboard</h3>
<p>
Utilizamos a biblioteca <i>Openpyxl</i> para gerar um dashboard no Excel com as informações da carteira de investimentos. O Dashboard contém duas tabelas, uma para o ativo moedas e outra correspondente a ações. As tabelas têm os nomes de cada ativo, as quantidades, as cotações e o totais em real.
</p>
<p>
Além disso, há três gráficos que ressaltam aspectos da carteira considerados importantes:
</p>
<p>
O primeiro gráfico formado por um conjunto de moedas compara a quantidade de cada uma e, uma vez convertido pela cotação, infere o valor total em reais que este ativo representa.
</p>
<p>
O segundo gráfico representa a porcentagem dos ativos investidos em ações. Ele permite visualizar, percentualmente, a representatividade de cada ação em relação ao capital total investido nesta modalidade de ativo.
</p>
<p>
O terceiro gráfico apresenta o valor de cada ativo investido em relação ao valor total da carteira. Na representação, pode-se visualizar o conjunto de todos os ativos, tanto percentualmente como o valor individual de cada ativo em relação ao capital total formado pela carteira.
</p>
<p>
Por último, um QrCode contém o valor total da carteira, ou seja, a soma total dos ativos em real.
</p>

<h3>Requisitos</h3>
<p>Instale as seguintes bibliotecas para rodar o código perfeitamente:</p>
<ol>
<li>bs4</li>
<li>copy</li>
<li>openpyxl</li>
<li>openpyxl.chart</li>
<li>openpyxl.chart.series</li>
<li>openpyxl.drawing.image</li>
<li>openpyxl.styles</li>
<li>qrcode</li>
<li>requests</li>
<li>yfinance</li>
</ol>
