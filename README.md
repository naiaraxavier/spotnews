# Spotnews 📰✨

O Spotnews é uma aplicação web desenvolvida como parte do curso da Trybe, que permite armazenar e categorizar notícias. O projeto utiliza o framework Django, trabalhando com Django Rest Framework para criar uma API que gerencia categorias, usuários e notícias.

## Estrutura do Projeto 🚀

### Desenvolvido por Mim
- `news/models.py`
- `news/templates/base.html`
- `news/templates/home.html`
- `news/templates/news_details.html`
- `news/templates/categories_form.html`
- `news/templates/news_form.html`
- `news/templates/404.html`
- `news/serializers.py`
- `news/urls.py`
- `news/validators.py`
- `news/models.py`
- `news/forms.py`

### Desenvolvido pela Trybe
- Arquivos e pastas não mencionados como desenvolvidos por mim estão relacionados ao desenvolvimento pela Trybe.

## Como Executar o Projeto 🛠️

### Pré-requisitos
Certifique-se de ter o Python 3.x e o Docker instalados na sua máquina.

### Passos para Executar a Aplicação 🚀

**Usando Docker:**
1. Certifique-se de ter o Docker instalado.
2. Execute o seguinte comando para subir a aplicação:
   ```bash
   docker compose up
    ```


**Executando Localmente:**


Crie um ambiente virtual para o projeto:
```bash
python3 -m venv .venv && source .venv/bin/activate
```
Instale as dependências necessárias:
```bash
python3 -m pip install -r dev-requirements.txt
```
Inicie o servidor Django:
```bash
python3 manage.py runserver
```


### Acesso à Aplicação 🌐

Abra o navegador e acesse http://127.0.0.1:8000/ para visualizar o Spotnews.


## Contribuições 💪

Desenvolvido por Naiara Martins

Arquivos e pastas específicos estão relacionados ao desenvolvimento pela Trybe.
