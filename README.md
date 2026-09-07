# 📚 API de Biblioteca

Projeto acadêmico desenvolvido em Python com **FastAPI**, para gerenciamento de livros e clientes de uma biblioteca, com persistência de dados em banco **SQLite**.

## 👥 Integrantes

- Enrico Bertolacini - RM 570999
- Matheus Sá - RM 571719
- Guilherme Alvejan - RM 570835
- Pedro Antonio  - RM 572549
- Julia Lima da Silva - RM 569203

## ⚙️ Como executar o projeto

**1. Instalar as dependências**

```bash
python -m pip install fastapi uvicorn
```

**2. Executar a API**

```bash
python -m uvicorn main:app --reload
```

**3. Acessar a API**

A API estará disponível em:

```
http://127.0.0.1:8000
```

> ⚠️ **Observação:** para visualizar a documentação interativa (Swagger UI), onde é possível testar todos os endpoints diretamente pelo navegador, acesse `http://127.0.0.1:8000/docs`.

## 🗂️ Estrutura do projeto

```
CheckPoint-4---Python/
├── main.py                        # Ponto de entrada da API (FastAPI)
│
├── controller/                    # Camada de rotas (endpoints)
│   ├── controller_livro.py        # Rotas de livros
│   └── controller_cliente.py      # Rotas de clientes
│
├── service/                       # Camada de regras de negócio
│   ├── service_livro.py           # Lógica de livros
│   └── service_cliente.py         # Lógica de clientes
│
├── database/                      # Camada de acesso a dados
│   └── database.py                # Conexão e criação das tabelas (SQLite)
│
└── .gitignore
```

## 🏗️ Arquitetura

O projeto segue uma separação em três camadas:

1. **Controller** → define os endpoints da API e recebe as requisições HTTP
2. **Service** → concentra a lógica de negócio e realiza as operações no banco
3. **Database** → responsável pela conexão com o SQLite e criação das tabelas

## 📌 Endpoints disponíveis

### Livros (`/livros`)
| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/livros` | Cadastrar um livro |
| GET | `/livros` | Listar todos os livros |
| GET | `/livros/{livro_id}` | Buscar um livro por ID |
| PUT | `/livros/{livro_id}` | Atualizar um livro |
| DELETE | `/livros/{livro_id}` | Excluir um livro |

### Clientes (`/clientes`)
| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/clientes` | Cadastrar um cliente |
| GET | `/clientes` | Listar todos os clientes |
| GET | `/clientes/{cliente_id}` | Buscar um cliente por ID |
| PUT | `/clientes/{cliente_id}` | Atualizar um cliente |
| DELETE | `/clientes/{cliente_id}` | Excluir um cliente |

## 🛠️ Tecnologias utilizadas

- Python 3
- FastAPI
- Uvicorn
- SQLite

## 📄 Sobre o banco de dados

O banco de dados (`biblioteca.db`) é criado automaticamente na primeira execução da API, com as tabelas `livros` e `clientes` já configuradas.
