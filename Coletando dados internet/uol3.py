import requests
from bs4 import BeautifulSoup

url = 'https://www.uol.com.br/start/esport/'
page = requests.get(url)
print(page.content)