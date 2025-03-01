# URL Shortener REST API

Este projeto consiste no desenvolvimento de uma API REST para encurtamento de URLs, utilizando Python e Django. A API permite transformar URLs longas em versões curtas, com funcionalidades para redirecionamento e registro de estatísticas como cliques e datas de criação.

## Status do Projeto

:construction: **Em Desenvolvimento** :construction:

## Funcionalidades Planejadas
- Encurtamento de URLs.
- Redirecionamento para a URL original a partir do link encurtado.
- Registro de estatísticas de uso (número de cliques, datas de criação).
- Sistema de autenticação para gerenciamento de URLs por usuários registrados.
- Interface para documentação interativa (Swagger/OpenAPI).

## Tecnologias Utilizadas
- **Linguagem:** Python
- **Framework:** Django, Django REST Framework
- **Banco de Dados:** SQLite 
- **Outras ferramentas:**
  - Django Swagger/OpenAPI para documentação
  - Pytest para testes

## Estrutura do Projeto

```
url-shortener/
|-- manage.py
|-- shortener/
    |-- models.py
    |-- views.py
    |-- serializers.py
    |-- urls.py
    |-- tests.py
```

## Configuração do Ambiente de Desenvolvimento

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes do Python)
- Ambiente virtual (recomendado, ex.: `venv`)

### Passos para Configuração
1. Clone este repositório:
   ```bash
   git clone https://github.com/caiohenriquefranca/encurt-url
   cd url-shortener
   ```
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate # Linux/Mac
   venv\Scripts\activate   # Windows
   ```
3. Execute as migrações para configurar o banco de dados:
   ```bash
   python manage.py migrate
   ```
4. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```
5. Acesse a aplicação localmente em [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

