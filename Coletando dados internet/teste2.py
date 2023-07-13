import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve

url = 'https://s3.amazonaws.com/video.udacity-data.com/topher/2018/November/5bf32290_turnstile/turnstile.html'

#Criação da variável page com URL no método request.get
page = requests.get(url)

#coleta,analisa e configura como um objeto BeautifulSoup
soup = BeautifulSoup(page.text,'html.parser')
links = soup.find_all('a')

#retorna os todos os links do Junho de 2017 da página

totalArquivos = 0
for link in links:
    href= link.get('href')
    if href != None and '1706' in href:
        totalArquivos += 1

print(totalArquivos)