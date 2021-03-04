"""
opovo.py
autor:       Artur Rodrigues Rocha Neto
contato:     artur.rodrigues26@gmail.com
descrição:   Script que burla o paywall do jornal O Povo (www.opovo.com.br)
uso:         Como bot Telegram ou como interface de linha de comando
requisitors: beautifulsoup4, bleach, python-telegram-bot, telegraph_client
"""

import sys
import bs4
import logging
import requests
from bs4 import BeautifulSoup
from telegraph import Telegraph
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegraph.utils import html_to_content

TOKEN_BOT = "MEU_TOKEN_BOT_SHOW"
TOKEN_TELEGRAPH = "MEU_TOKEN_TELEGRAPH_SHOW"
LOGFORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

def parse_url(url):
    """
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
    titulo = soup.find("h1", class_="article-title")
    if titulo:
        titulo = titulo.string.strip()
    else:
        titulo = soup.find("h1", class_="tit-noticia").string.strip()
    
    # procura pela manchete
    manchete = soup.find("span", class_="article-desc")
    if manchete:
        manchete = manchete.string.strip()
    else:
        manchete = soup.find("h2", class_="abre-noticia").string.strip()
    manchete = "<h4>" + manchete + "</h4>"
    
    # procura nome do autor
    nome_autor = ""
    autor = soup.find("span", class_="by-author")
    if autor:
        nome_autor = autor.find("a").string
    else:
        autor = soup.find("span", class_="colunista-author")
        nome_autor = autor.string
    
    # formatacao do conteudo textual
    conteudo = []
    for paragrafo in soup.findAll("p", class_="texto"):
        if paragrafo.string:
            conteudo.append(paragrafo.string.strip())
        else:
            subcontent = [coisa.string for coisa in paragrafo.contents if coisa.string]
            conteudo.append("".join(subcontent).strip())
    
    # procura div com o conteudo em si para raspar imagens
    container = soup.find("div", class_="text-container")
    if not container:
        container = soup.find("div", class_="conteudo-interna")
    images = container.findAll("figure")
    if images:
        images = [str(img) for img in images]
    
    # geracao do HTML resultado
    content = [manchete] + ["<p>" + txt + "</p>" for txt in conteudo if len(txt) > 0]
    if images:
        content = content + images
    content = "".join(content)
    content = html_to_content(content)
    
    # publicacao via API do Telegraph
    telegraph = Telegraph(TOKEN_TELEGRAPH, timeout=60)
    new_page = telegraph.create_page(title=titulo, author_name=nome_autor, content=content)
    
    return new_page.url

def start(update, context):
    """
    """
    
    txt = "Me envie um link do Portal O Povo que eu quebrarei o paywall para você. Leitura completa direta no Telegram."
    context.bot.send_message(chat_id=update.effective_chat.id, text=txt)

def echo(update, context):
    """
    """
    
    ans = parse_url(update.message.text)
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.message.message_id)
    context.bot.send_message(chat_id=update.effective_chat.id, text=ans)

def cli(url):
    """
    """
    
    ans = parse_url(url)
    
    print()
    print("-"*len(ans))
    print(ans)
    print("-"*len(ans))
    print()

def start_bot():
    """
    """
    
    # log de erros e avisos
    logging.basicConfig(format=LOGFORMAT, level=logging.INFO)
    
    # objetos updater e dispatcher
    updater = Updater(token=TOKEN_BOT, use_context=True)
    dispatcher = updater.dispatcher
    
    # handlers dos comandos
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    
    # liga o bot
    print("Preparado para quebrar paywalls...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        cli(sys.argv[1])
    else:
        start_bot()
