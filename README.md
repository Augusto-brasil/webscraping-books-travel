# Scraping de Livros de Viagem - Books to Scrape 📚✈️

Este é um projeto prático desenvolvido para treinar técnicas de **Web Scraping** (raspagem de dados) utilizando Python. 

O script realiza uma requisição para o site *Books to Scrape*, extrai informações específicas dos livros da categoria "Travel" (Viagem), trata os dados e os exporta para um arquivo estruturado.

## 🛠️ Tecnologias e Bibliotecas Utilizadas
* **Python 3**
* **Requests**: Para envio das requisições HTTP e captura do HTML.
* **BeautifulSoup4 (com parser lxml)**: Para navegação na árvore HTML e extração dos dados (títulos e preços).
* **Pandas**: Para estruturação dos dados em um DataFrame e exportação limpa.

## 📈 Desafios Resolvidos no Projeto
* **Tags sem identificação direta**: Captura de títulos através de seletores CSS (`h3 a`) quando a tag pai não possuía classes definidas.
* **Tratamento de Strings**: Limpeza do texto do preço para remover o símbolo da moeda (`£`) e focar apenas no valor numérico.
* **Robustez do Código**: Implementação de verificações condicionais para evitar erros (`AttributeError`) caso alguma tag falhe ao carregar.
* **Exportação Limpa**: Salvamento do arquivo CSV omitindo os índices automáticos do Pandas (`index=False`).

## 💾 Como Executar
1. Instale as dependências: `pip install beautifulsoup4 requests pandas lxml`
2. Execute o script: `python precosLivrosVieagem.py`
3. O arquivo `livrosdeviagens.csv` será gerado na raiz do projeto.
