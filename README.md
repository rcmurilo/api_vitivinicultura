# API de Vitivinicultura - Embrapa

Esta API realiza raspagem (scraping) dos dados públicos disponíveis no site da Embrapa sobre vitivinicultura brasileira, abrangendo produção, processamento, comercialização, importação e exportação de uvas e derivados. Os dados raspados são armazenados em um banco SQLite para uso posterior, como por exemplo alimentar modelos de Machine Learning.

---

## Tecnologias Utilizadas

- **Python 3.9+**
- **FastAPI**
- **SQLAlchemy**
- **BeautifulSoup**
- **SQLite**
- **JWT (JSON Web Tokens)**
- **Uvicorn**

---

## Estrutura do Projeto

```
api_vitivinicultura/
├── app/
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── security.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   └── models.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── comercializacao.py
│   │   ├── exportacao.py
│   │   ├── importacao.py
│   │   ├── processamento.py
│   │   └── producao.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── scrapers.py
│   ├── __init__.py
│   └── main.py
├── vitivinicultura.db
├── requirements.txt
├── .env
├── procfile
└── README.md
```

---

## Funcionalidades

- Scraping das tabelas disponíveis no site da Embrapa
- Proteção por autenticação via JWT
- Armazenamento em banco de dados relacional SQLite
- Organização modular com FastAPI
- Documentação automática com Swagger

---

## Como executar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/rcmurilo/api_vitivinicultura.git
cd api_vitivinicultura
```

### 2. Crie o ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate   # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure seu `.env`

Crie um arquivo `.env` com:

```
USERNAME=admin
PASSWORD=admin123
```

### 5. Execute a aplicação

```bash
uvicorn app.main:app --reload
```

Acesse: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Autenticação

1. Acesse `/docs`
2. Use o botão `Authorize`
3. Informe `username` e `password` definidos no `.env`
4. Após login, use os endpoints protegidos

---

## Endpoints

- `POST /token` - login com usuário e senha
- `GET /producao` - dados da produção
- `GET /processamento` - dados do processamento
- `GET /comercializacao` - dados da comercialização
- `GET /importacao` - dados da importação
- `GET /exportacao` - dados da exportação

---

## Caso de uso proposto

A API pode ser usada para alimentar dashboards, painéis analíticos e modelos de previsão de produção e consumo da indústria vitivinícola brasileira.

---
