from bs4 import BeautifulSoup
import requests

#1 - coeltando vagas de python

url = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'

print('enviando requisiçao')

response = requests.get(url)

print(f'status code: {response.status_code}')

soup = BeautifulSoup(response.text, 'lxml')
books = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')


for book in books:
    book_name = book.find('h3')

    if book_name:
        sel_book = book_name.find('a')['title']
        print(f'nome de Livros: {sel_book}\n')
