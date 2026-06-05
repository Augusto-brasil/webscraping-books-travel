from bs4 import BeautifulSoup
import requests
import pandas as pd

# Coletando Livros de viagens

url = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'

print('enviando requisição')

response = requests.get(url)

print(f'status code: {response.status_code}')

soup = BeautifulSoup(response.text, 'lxml')
books = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

book_name = []
book_price = []

for book in books:
    n_tag = book.select_one('h3 a')
    name = n_tag['title'] if n_tag else 'inexistente'
    book_name.append(name)

    price = book.find('p', class_='price_color')
    p_book = price.get_text().replace('£','') if price else "zerado"
    book_price.append(p_book)
    
df_livros = pd.DataFrame()
df_livros['Names'] = book_name
df_livros['Prices'] = book_price

df_livros.to_csv('livrosdeviagens.csv', index=False, encoding='utf-8')
print("Arquivo gerado com sucesso !!!")





