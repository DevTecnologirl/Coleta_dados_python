import requests
from bs4 import BeautifulSoup
url = 'https://www.uol.com.br/start/esport/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

lista = ['lol','valorant','fifa','fortnite']

for paragrafo in soup.fin_all('body'):
    for palavra in lista:
        for paragrafo_str in paragrafo.stripped_strings:
            if palavra.upper() in str(paragrafo_str).upper():
                print('NOTICIA SOBRE: ', palavra.upper(), '\n', paragrafo_str,'\n')
            break