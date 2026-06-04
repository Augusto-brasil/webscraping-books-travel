from bs4 import BeautifulSoup
import requests
import pandas

#1 - coeltando vagas de python

url = 'https://www.timesjobs.com/job-search?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='

print('enviando requisiçao')

response = requests.get(url)

print(f'status code: {response.status_code}')

