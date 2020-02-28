"""
opovo.py
Artur Rodrigues Rocha Neto

Script que burla o paywall do jornal O Povo (www.opovo.com.br)
Requisitos: Python 3.x, BeautifulSoup4
"""

import sys
import base64
import tempfile
import requests
import codecs
import webbrowser
from bs4 import BeautifulSoup

## checando numero de parametros
if len(sys.argv) != 2:
	print("Erro: número incorreto de argumentos!")
	print("Uso: python3 opovo.py <ulr_da_noticia>")
	sys.exit(1)

## pegando URL passado por paramentro e fazendo conexao
url = sys.argv[1]
try:
	page = requests.get(url)
except:
	print("Erro: não foi possível carregar o recurso!")
	print("Favor, tente novamente.")
	sys.exit(1)

## conferindo se tudo deu certo com a conexao
if page.status_code != 200:
	print("Erro: página não encontrada!")
	print("Favor, tente novamente.")
	sys.exit(1)

## carregando template de pagina a ser exibida no navegador
template = open("template.html", "r")
html_template = template.read()
template.close()

## fazendo o parse da pagina e montagem do HTML resultado
soup = BeautifulSoup(page.content, "html.parser")
title = soup.title.string + " (opovo.py)"

div_content = soup.find("div", class_="text-container")
if div_content == None:
	div_content = soup.find("div", class_="conteudo-interna")

html = html_template.format(title, title, div_content)

## criando pagina em arquivo temporario
temp_page = tempfile.NamedTemporaryFile(delete=False)
path = temp_page.name + ".html"
f = codecs.open(path, "w", "utf-8")
f.write(html)
f.close()

## exibindo conteudo que foi extraido
webbrowser.open("file://" + path, new=2)

