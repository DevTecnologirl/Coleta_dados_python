from logging import exception
import requests as r
from bs4 import BeautifulSoup

try:
  resultado = r.get("https://www.uol.com.br/")
except Exception as erro:
  print("ERRO",erro)
else:
  resposta = resultado.text
  soup = BeautifulSoup(resposta, 'html.parser')

  print(soup.find("h2", class_="kicker kicker--live headlineHorizontalLive__content__kicker").prettify())

  #prettify = usado para organizar o texto HTML facilitando a leitura
  #find_all = chama varios elementos do mesmo atributo