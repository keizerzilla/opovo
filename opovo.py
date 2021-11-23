"""
arquivo:     opovo.py
autor:       Artur Rodrigues Rocha Neto
contato:     artur.rodrigues26@gmail.com
descrição:   Script que burla o paywall do jornal O Povo (www.opovo.com.br)
requisitors: beautifulsoup4
"""

import sys
import bs4
import requests
from bs4 import BeautifulSoup

def parse_url(url):
    """ Raspa notícia por trás do paywall do Jornal O Povo.
    
    Parâmetros
    ----------
        url: A url da notícia do O Povo.
    
    Retorno
    -------
        ans: Dicionário com as três partes principais do conteúdo: título, autor
        e conteúdo.
    
    """
    
    page = None
    try:
        page = requests.get(url)
        if page.status_code != 200:
            return "Não consegui quebrar essa página..."
    except:
        return "Não consegui quebrar essa página..."
    
    soup = BeautifulSoup(page.content, "html.parser")
    
    # procura titulo da materia
    # classes possiveis: article-title, tit-noticia
    titulo = soup.find("h1", class_="article-title")
    if titulo:
        titulo = titulo.string.strip()
    else:
        titulo = soup.find("h1", class_="tit-noticia").string.strip()
    
    # procura pela manchete
    # classes possiveis: article-desc, abre-noticia
    manchete = soup.find("span", class_="article-desc")
    if manchete:
        manchete = manchete.string.strip()
    else:
        manchete = soup.find("h2", class_="abre-noticia").string.strip()
    
    # procura nome do autor
    # classes possiveis: by-author, colunista-author
    autor = soup.find("span", class_="by-author")
    if autor:
        autor = autor.find("a").string
    else:
        autor = soup.find("span", class_="colunista-author").string
    
    # formatacao do conteudo textual
    conteudo = []
    for paragrafo in soup.findAll("p", class_="texto"):
        if paragrafo.string:
            conteudo.append(paragrafo.string.strip())
        else:
            subcontent = [coisa.string for coisa in paragrafo.contents if coisa.string]
            conteudo.append("".join(subcontent).strip())
    
    ans = {
        "titulo"   : titulo,
        "autor"    : autor,
        "conteudo" : conteudo
    }
    
    return ans


def cli(url):
    """ Função da interface de linha de comando. Chama função de raspagem e
    mostra conteúdo raspado na saída padrão.
    
    Parâmetros
    ----------
        url: A url da notícia do O Povo.
    
    Retorno
    -------
        Nenhum.
    
    """
    
    ans = parse_url(url)
    
    print(ans["titulo"].upper())
    print(ans["autor"])
    print()
    print()
    
    for line in ans["conteudo"]:
        if len(line) <= 80:
            print(line)
        else:
            print(line[:80])
            print(line[80:])
        print()


def to_txt(url, filename=None):
    """ Função para salvar em arquivo texto. Chama função de raspagem e guarda
    conteúdo raspado em arquivo nomeado por padrão com o mesmo nome da matéria.
    
    Parâmetros
    ----------
        url: A url da notícia do O Povo.
        filename: Nome do arquivo onde salvar o conteúdo raspado.
    
    Retorno
    -------
        Nenhum.
    
    """
    
    ans = parse_url(url)
    
    if filename is None:
        filename = ans["titulo"] + ".txt"
    
    with open(filename, "w") as dump:
        dump.write(ans["titulo"].upper())
        dump.write("\n")
        dump.write(ans["autor"])
        dump.write("\n")
        dump.write(f"Original: {url}\n")
        dump.write("\n\n")
        
        dump.write("\n\n".join(ans["conteudo"]))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        to_txt(sys.argv[1])
    else:
        print("Número insuficiente de argumentos!")
        print("USO: python3 opovo.py <url_da_matéria>")


