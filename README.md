# opovo.py

`opovo.py` é um projeto que visa construir uma interface para raspagem de notícia do Jornal [O Povo](https://www.opovo.com.br/) de Fortaleza, Ceará. Até o momento, permite salvar o conteúdo raspado em arquivo ou visualizando na própria saída padrão.

## Instalação

Para usar o script, primeiro é necessário instalar os pacotes Python de pré-requisito. Basta chamar o gerenciador de pacotes `pip` de dentro da raíz do projeto:

```
pip3 install --user --upgrade -r requirements.txt
```

Se o seu sistema não reconhecer o compando `pip3`, tente trocá-lo para `pip`. Se o erro persistir, verifique como instalar o gerenciador de pacotes no seu sistema operacional.

## Uso

```python
python3 opovo.py <url_da_materia>
```

