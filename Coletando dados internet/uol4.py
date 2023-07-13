import requests
from bs4 import BeautifulSoup

url = 'https://www.uol.com.br/start/esport/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())