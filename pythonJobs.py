from bs4 import BeautifulSoup
import requests

#1 - coeltando vagas de python

url = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'

print('enviando requisiçao')

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
    p_book = price.get_text()[2:] if price else "zerado"
    book_price.append(p_book)


for x_nome, Y_preço in zip(book_name, book_price):
    print(f'nome: {x_nome} - preco:{Y_preço}')



