<div align="center">

# 🎓 API Colégio Porto

### Sistema de Gerenciamento Escolar

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.3.0-green.svg)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-3.0.5-red.svg)](https://www.sqlalchemy.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-Educational-yellow.svg)]()

API REST completa para controle de **Professores**, **Turmas** e **Alunos**, desenvolvida com Flask seguindo arquitetura MVC.

</div>

---

## 👥 Integrantes do Grupo

<table>
  <tr>
    <td align="center">
      <b>Anna Julia Higa Farincho</b>
    </td>
    <td align="center">
      <b>Leticia Macedo</b>
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

## 🗄️ Modelo de Dados

<div align="center">

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


## 🚀 Como Executar

### 🖥️ Opção 1️⃣: Executar Localmente  

#### **Pré-requisitos**
- Python 3.11 ou superior  
- `pip` (gerenciador de pacotes Python)

#### **Passo a Passo**

```bash
# 1. Clone o repositório
git clone https://github.com/Evemerces/api-colegio-porto.git
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
✅ Pronto!
A API estará disponível em:

🌐 API: http://localhost:5000

📚 Documentação: http://localhost:5000/docs

🐳 Opção 2️⃣: Executar com Docker
Pré-requisitos
Docker instalado

Docker Compose instalado

Passo a Passo
bash
Copiar código
# 1. Clone o repositório
git clone https://github.com/EveMerces/api-colegio-porto.git
cd api-colegio-porto

# 2. Build e execute
docker-compose up --build

# Para rodar em background
docker-compose up -d
Acesse:

🌐 API: http://localhost:5000

📚 Documentação: http://localhost:5000/docs

Comandos úteis Docker
bash
Copiar código
# Ver logs
docker-compose logs -f

# Parar containers
docker-compose down

# Rebuild completo
docker-compose build --no-cache
📚 Documentação da API
A documentação completa e interativa está disponível via Swagger UI:
🔗 http://localhost:5000/docs

📊 Dados Iniciais
O script popular_banco.py cria automaticamente os seguintes registros:

👨‍🏫 Professores	🏫 Turma
Kleber Chiles
Matéria: DevOps

Giovani Bontempo
Matéria: API

Odair Gabriel
Matéria: Desenvolvimento Mobile

Turma: SI 3A
Ano: 2025
Período: Noite
Professor: Odair Gabriel

👨‍🎓 Alunas

Nome	Nota	Situação
Anna Julia Higa Farincho	7.8	✅ Aprovada
Letícia Macedo	8.2	✅ Aprovada
Evelyn Mercês	7.5	✅ Aprovada

✅ Funcionalidades Implementadas
Funcionalidade	Status
CRUD de Professores	✅
CRUD de Turmas	✅
CRUD de Alunos	✅
Relacionamentos entre entidades	✅
Validações de dados	✅
Tratamento de erros	✅
Documentação Swagger	✅
Arquitetura MVC	✅
Docker	✅
Git/GitHub	✅

🔒 Validações Implementadas
✅ Email único para Professores e Alunos

✅ CPF único para Professores e Alunos

✅ Campos obrigatórios verificados

✅ Integridade referencial preservada

✅ Data de nascimento no formato válido (DD/MM/AAAA)

✅ Verificação de existência de entidades relacionadas

✅ Proteção contra deleção de registros com dependências

📖 O Que Aprendemos
Durante o desenvolvimento deste projeto, aprendemos e aplicamos conceitos como:

🎯 Conceitos Técnicos
Arquitetura MVC
APIs RESTful
ORM (SQLAlchemy)
Relacionamentos de banco de dados
Conteinerização com Docker

📆 Ano: 2025
🏫 Curso: Sistemas de Informação
💡 Projeto: API Colégio Porto

✨ "Aprender fazendo é o melhor caminho para dominar a tecnologia."

