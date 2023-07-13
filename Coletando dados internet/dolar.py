# -*- coding: utf-8 -*-
"""dolar.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HaahqGMaouNGLxgxunbXRBA-NRingC0p
"""

pip install beautifulsoup4

pip install requests

import requests
from bs4 import BeautifulSoup

link = "https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
requisicao = requests.get(link)
print(requisicao)
#print(requisicao.text)
#resposta 200 = significa que a requisição deu certo e além disso ele trás outras informações

#tratamento do texto desorganizado -- sendo uma forma melhor de ler
site = BeautifulSoup(requisicao.text, "html.parser")
#print(site.prettify())

#pegando informações 1 forma
#print(site.title)

#pegando informaçoes 2 forma
titulo = site.find("title")   #passar o nome da tag em HTML
print(titulo)

pesquisa = site.find("input")
print(pesquisa)

#find_all = encontra todas as correspondencias da tag
busca = site.find_all("input")
#print(busca) = imprime todas tags input
print(busca[1])

#BeautifulSoup: é para raspagem de sites ESTATICOS.
# Quando é um site que ocorre atualizações frequente (dinamicos) usa-se outra ferramenta como o SELENIUM

pesquisa2 = site.find("input", class_="i4JFmd")
print(pesquisa2)


cotacao =  site.find("span", class_="DFlfde SwHCTb")
print(cotacao["data-value"])
#informar a versão do navegador para obter dados através do network
# -- REQUEST HEADERS  -- USER-AGENT
#headers = como se fosse o cabeçalho que da informações extras