from bs4 import BeautifulSoup
import requests
import pandas

#1 - coeltando vagas de python

url = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'

print('enviando requisiçao')

response = requests.get(url)

print(f'status code: {response.status_code}')

soup = BeautifulSoup(response.text, 'lxml')
jobs = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

print(len(jobs))
print(jobs[:3])
