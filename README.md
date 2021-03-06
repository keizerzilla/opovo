# opovo_pwb
`opovo_pwb` (*O Povo Paywall Breaker*) é um projeto que visa construir uma interface para raspagem de notícia do Jornal [O Povo](https://www.opovo.com.br/) de Fortaleza, Ceará. Pode ser usado como CLI (interface de linha de comando) ou como bot Telegram. Escrito em Python 3, o código necessita de alguns pacotes para funcionamento (arquivo `requirements.txt`), além de uma chave API para o serviço Telegraph; essas são os requistos obrigatórios ([instruções Telegraph](https://telegram.org/blog/telegraph)). Para uso como bot Telegram, que é uma funcionalidade opcional, uma bot token desse serviço é necessário ([instruções Telegram bot](https://core.telegram.org/bots#3-how-do-i-create-a-bot)).

## Instalação de pré-requisitos

Para instalar os pacotes necessários, basta chamar o gerenciador de pacotes pip de dentro da raíz do projeto:

```
pip3 install --user --upgrade -r requirements.txt
```

Se o seu sistema não reconhecer o compando pip3, tente trocá-lo para pip. Se o erro persistir, verifique como instalar o gerenciador de pacotes no seu sistema operacional.

## Configurando chaves Telegraph e Telegram bot

Nas primeiras linhas do código você encontrará duas variáveis: `TOKEN_TELEGRAPH` e `TOKEN_BOT`, que guardam as chaves de API pros serviços Telegraph e Telegram bot, respectivamente. Você deve trocar os valores temporários com as respectivas chaves que você criou seguindo as intruções linkadas no início deste README (lembrando que apenas o serviço Telegraph é obrigatório).
