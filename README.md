# API Connect

API RESTful desenvolvida como Produto Mínimo Viável (MVP) para gerenciamento de usuários, estruturada sob o princípio da Separação de Responsabilidades (SoC), semântica HTTP estrita e padronização determinística das respostas em JSON.

---

## Tecnologias Utilizadas

* Python 3 - Linguagem base da aplicação.
* Flask - Microframework web para estruturação dos endpoints e roteamento modular com Blueprints.
* Virtualenv (venv) - Isolamento e gestão de dependências locais do projeto.
* Thunder Client / VS Code - Ferramentas para validação e execução dos testes manuais de rotas.

---

## Estrutura do Projeto
```
api-connect/
│
├── controllers/
│   └── user_controller.py   # Lógica de negócio, validações de entrada e envelopes de resposta
├── data/
│   └── database.py          # Camada de persistência provisória em memória (RAM)
├── routes/
│   └── user_routes.py       # Mapeamento dos verbos e parâmetros de rotas (Blueprints)
├── app.py                   # Ponto de entrada, configuração do servidor e middlewares
├── requirements.txt         # Lista de dependências e versões da aplicação
├── .gitignore               # Regras de exclusão de arquivos no controle de versão
└── README.md                # Documentação técnica e guia de execução da API
```

## Como Executar o Projeto Localmente

### 1. Clonar o Repositório
```bash
git clone https://github.com/Viniriter/api-connect-vinicius-riter.git
cd api-connect-vinicius-riter
```

### 2. Criar e Ativar o Ambiente Virtual

* No Windows (Prompt de Comando / PowerShell):
```cmd
python -m venv venv
venv\Scripts\activate
```

* No Linux / macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 4. Inicializar o Servidor
```bash
python app.py
```

A aplicação estará em execução e acessível em: `http://127.0.0.1:5000`

---

## Tabela de Endpoints da API

| Método | Endpoint | Descrição | Status de Sucesso | Status de Erro |
| :--- | :--- | :--- | :--- | :--- |
| GET | `/` | Rota base de verificação de integridade da API | 200 OK | - |
| GET | `/users` | Listagem geral de todos os usuários cadastrados | 200 OK | - |
| GET | `/users/<id>` | Busca os dados detalhados de um usuário por ID | 200 OK | 404 Not Found |
| POST | `/users` | Cadastra um novo usuário validando nome e e-mail | 201 Created | 400 Bad Request |
| PUT | `/users/<id>` | Atualiza as informações de um usuário existente | 200 OK | 400 Bad Request, 404 Not Found |
| DELETE| `/users/<id>` | Remove um usuário cadastrado da base | 204 No Content | 404 Not Found |

---

## Exemplos de Uso e Payloads

### 1. Cadastro de Usuário (`POST /users`)
* Corpo da Requisição (JSON):
```json
{
  "name": "Davi Riter",
  "email": "davi.riter@email.com"
}
```
* Resposta de Sucesso (`201 Created`):
```json
{
  "data": {
    "id": 3,
    "name": "Davi Riter",
    "email": "davi.riter@email.com"
  },
  "message": "Usuário cadastrado com sucesso."
}
```

---

### 2. Falha de Validação no Cadastro (`POST /users`)
* Corpo da Requisição (JSON):
```json
{
  "name": "Davi Riter"
}
```
* Resposta de Erro (`400 Bad Request`):
```json
{
  "error": "O campo 'email' é obrigatório e deve ser preenchido."
}
```

---

### 3. Listagem Geral (`GET /users`)
* Resposta de Sucesso (`200 OK`):
```json
[
  {
    "id": 1,
    "name": "Vinicius Riter",
    "email": "vinicius.riter@email.com"
  },
  {
    "id": 2,
    "name": "Evelin Lubas",
    "email": "evelin.lubas@email.com"
  },
  {
    "id": 3,
    "name": "Davi Riter",
    "email": "davi.riter@email.com"
  }
]
```

---

### 4. Busca por ID Inexistente (`GET /users/999`)
* Resposta de Erro (`404 Not Found`):
```json
{
  "error": "Usuário com ID 999 não encontrado."
}
```

---

### 5. Remoção de Usuário (`DELETE /users/1`)
* Resposta de Sucesso (`204 No Content`):
Sem corpo de resposta retornado.
```
