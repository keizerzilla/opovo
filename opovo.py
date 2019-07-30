"""
opovo.py
Artur Rodrigues Rocha Neto

Script que burla o paywall do jornal O Povo (www.opovo.com.br)
Requisitos: Python 3.x, BeautifulSoup
"""

import sys
import requests
from bs4 import BeautifulSoup

if len(sys.argv) != 2:
	print("Erro: número incorreto de argumentos!")
	print("Uso: python3 opovo.py <ulr_da_noticia>")
	sys.exit(1)

url = sys.argv[1]

try:
	page = requests.get(url)
except:
	print("Erro: página não encontrada!")
	print("Favor, tente novamente.")
	sys.exit(1)

if page.status_code != 200:
	print("Erro: página não encontrada!")
	print("Favor, tente novamente.")
	sys.exit(1)

soup = BeautifulSoup(page.content, "html.parser")
text_content = soup.find_all("p", class_="texto")

if len(text_content) == 0:
	text_content = soup.find("div", class_="conteudo-interna")
	print(text_content.get_text())
else:
	for text in text_content:
		print(text.get_text())
	
