# opovo.py

`opovo_pwb` (*O Povo Paywall Breaker*) é um projeto que visa construir uma interface para raspagem de notícia do Jornal [O Povo](https://www.opovo.com.br/) de Fortaleza, Ceará. Até o momento, permite salvar o conteúdo raspado em arquivo (uso padrão como script) ou visualizando na própria saída padrão (em construção: formatação adequada à quantidade de colunas disponíveis).

## Instalação de pré-requisitos

Para instalar os pacotes necessários, basta chamar o gerenciador de pacotes pip de dentro da raíz do projeto:

```
pip3 install --user --upgrade -r requirements.txt
```

Se o seu sistema não reconhecer o compando pip3, tente trocá-lo para pip. Se o erro persistir, verifique como instalar o gerenciador de pacotes no seu sistema operacional.

## Uso

```python
python3 opovo.py <url_da_materia>
```

