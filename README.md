<div align="center">

# 🎓 API Colégio Porto

### Sistema de Gerenciamento Escolar

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.3.0-green.svg)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-3.0.5-red.svg)](https://www.sqlalchemy.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-Educational-yellow.svg)]()

API REST completa para controle de **Professores**, **Turmas** e **Alunos**, desenvolvida com Flask seguindo arquitetura MVC.

[Documentação](#-documentação-da-api) •
[Como Usar](#-como-executar) •
[Tecnologias](#-tecnologias-utilizadas) •
[Endpoints](#-endpoints-disponíveis)

</div>

---

## 👥 Integrantes do Grupo

<table>
  <tr>
    <td align="center">
      <b>Anna Julia Higa Farincho</b>
    </td>
    <td align="center">
      <b>Letícia Macedo</b>
    </td>
    <td align="center">
      <b>Evelyn Mercês</b>
    </td>
  </tr>
</table>

---

## 📋 Sobre o Projeto

Este projeto foi desenvolvido como parte da disciplina de **Desenvolvimento de Aplicações Móveis (DAM)** e consiste em uma API REST completa para gerenciamento escolar do Colégio Porto.

### ✨ Principais Características

- 🏗️ **Arquitetura MVC** bem definida
- 🔄 **CRUD Completo** para 3 entidades
- 🔗 **Relacionamentos** entre Professor → Turma → Aluno
- ✅ **Validações** robustas de dados
- 📚 **Documentação Swagger** automática
- 🐳 **Docker** para fácil deploy
- 💾 **SQLite + SQLAlchemy** ORM

---

## 🛠️ Tecnologias Utilizadas

<div align="center">

| Tecnologia | Versão | Descrição |
|------------|--------|-----------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) | 3.11+ | Linguagem de programação |
| ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) | 2.3.0 | Framework web |
| ![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white) | 3.x | Banco de dados |
| ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) | Latest | Conteinerização |
| ![Swagger](https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black) | 0.9.7 | Documentação API |

</div>

---

## 📁 Estrutura do Projeto
---
api-colegio-porto/
├── app/
│   ├── __init__.py           # Configuração do Flask e Swagger
│   ├── models/               # Modelos do banco de dados
│   │   ├── __init__.py
│   │   ├── professor.py      # Model Professor
│   │   ├── turma.py          # Model Turma
│   │   └── aluno.py          # Model Aluno
│   └── controllers/          # Controladores (rotas/endpoints)
│       ├── __init__.py
│       ├── professor_controller.py
│       ├── turma_controller.py
│       └── aluno_controller.py
├── config.py                 # Configurações do banco e app
├── run.py                    # Arquivo principal
├── popular_banco.py          # Script para popular dados iniciais
├── requirements.txt          # Dependências Python
├── Dockerfile                # Configuração Docker
├── docker-compose.yml        # Orquestração Docker
└── README.md                 # Este arquivo

---

## 🗄️ Modelo de Dados

<div align="center">
```mermaid
erDiagram
    PROFESSOR ||--o{ TURMA : leciona
    TURMA ||--o{ ALUNO : possui
    
    PROFESSOR {
        int id PK
        string nome
        string email UK
        string cpf UK
        string materia
        datetime data_cadastro
    }
    
    TURMA {
        int id PK
        string nome
        int ano
        string periodo
        int professor_id FK
        datetime data_cadastro
    }
    
    ALUNO {
        int id PK
        string nome
        string email UK
        string cpf UK
        date data_nascimento
        int idade
        float nota_final
        string situacao
        int turma_id FK
        datetime data_cadastro
    }
  </div>

Relacionamentos
---
Relação             Cardinalidade       Descrição 
Professor → Turma       1:N           Um professor pode lecionar várias turmasTurma → Aluno1:NUma turma pode ter vários alunos
---
Turma → Aluno           1:N           Uma turma pode ter vários alunos
---
🚀 Como Executar
Opção 1️⃣: Executar Localmente
Pré-requisitos

Python 3.11 ou superior
pip (gerenciador de pacotes Python)

Passo a Passo
bash# 1. Clone o repositório
git clone https://github.com/SEU_USUARIO/api-colegio-porto.git
cd api-colegio-porto

# 2. Crie um ambiente virtual
python -m venv venv

# 3. Ative o ambiente virtual
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# 4. Instale as dependências
pip install -r requirements.txt

# 5. (Opcional) Popule o banco com dados iniciais
python popular_banco.py

# 6. Execute a aplicação
python run.py
✅ Pronto! Acesse:

🌐 API: http://localhost:5000
📚 Documentação: http://localhost:5000/docs


Opção 2️⃣: Executar com Docker
Pré-requisitos

Docker instalado
Docker Compose instalado

Passo a Passo
bash# 1. Clone o repositório
git clone https://github.com/SEU_USUARIO/api-colegio-porto.git
cd api-colegio-porto

# 2. Build e execute
docker-compose up --build

# Para rodar em background
docker-compose up -d
✅ Pronto! Acesse:

🌐 API: http://localhost:5000
📚 Documentação: http://localhost:5000/docs

Comandos úteis Docker:
bash# Ver logs
docker-compose logs -f

# Parar containers
docker-compose down

# Rebuild completo
docker-compose build --no-cache

📚 Documentação da API
A documentação completa e interativa está disponível via Swagger UI:
🔗 http://localhost:5000/docs
📊 Dados Iniciais
O script popular_banco.py cria automaticamente:
<table>
<tr>
<td>
👨‍🏫 Professores

Kleber Chiles

Matéria: DevOps


Giovani Bontempo

Matéria: API


Odair Gabriel

Matéria: Desenvolvimento Mobile



</td>
<td>
🏫 Turma

SI 3A

Ano: 2024
Período: Noite
Professor: Odair Gabriel



</td>
</tr>
<tr>
<td colspan="2">
👨‍🎓 Alunas
NomeNotaSituaçãoAnna Julia Higa Farincho7.8✅ AprovadaLetícia Macedo8.2✅ AprovadaEvelyn Mercês7.5✅ Aprovada
</td>
</tr>
</table>

✅ Funcionalidades Implementadas
<div align="center">
FeatureStatusCRUD de Professores✅CRUD de Turmas✅CRUD de Alunos✅Relacionamentos entre entidades✅Validações de dados✅Tratamento de erros✅Documentação Swagger✅Arquitetura MVC✅Docker✅Git/GitHub✅
</div>

🔒 Validações Implementadas

✅ Email único para Professores e Alunos
✅ CPF único para Professores e Alunos
✅ Campos obrigatórios verificados
✅ Integridade referencial preservada
✅ Data de nascimento em formato válido (DD/MM/AAAA)
✅ Verificação de existência de entidades relacionadas
✅ Proteção contra deleção com dependências
---
📖 O Que Aprendemos
Durante o desenvolvimento deste projeto, adquirimos conhecimento em:
<table>
<tr>
<td width="50%">
---
🎯 Conceitos Técnicos

Arquitetura MVC
APIs RESTful
ORM (SQLAlchemy)
Relacionamentos de banco de dados
Conteinerização com Docker

</td>
<td width="50%">