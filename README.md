🎓 API Colégio Porto
Sistema de gerenciamento escolar desenvolvido para a disciplina de Desenvolvimento de Aplicações Móveis (DAM).
API REST completa para controle de Professores, Turmas e Alunos do Colégio Porto, seguindo arquitetura MVC.

👥 Integrantes do Grupo

Anna Julia Higa Farincho
Letícia Macedo
Evelyn Mercês


🛠️ Tecnologias Utilizadas

Python 3.11
Flask - Framework web
SQLAlchemy - ORM para banco de dados
SQLite - Banco de dados
Flasgger - Documentação automática (Swagger)
Docker - Conteinerização


📁 Arquitetura do Projeto
O projeto segue o padrão MVC (Model-View-Controller) sem a camada de View, pois é uma API REST.
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

🗄️ Modelo de Dados
Relacionamentos
Professor (1) ──< (N) Turma (1) ──< (N) Aluno

Um Professor pode ter várias Turmas
Uma Turma pertence a um Professor
Uma Turma pode ter vários Alunos
Um Aluno pertence a uma Turma

Tabelas
professores

id (PK)
nome
email (unique)
cpf (unique)
idade (unique)
materia
data_cadastro

turmas

id (PK)
nome
ano
periodo (manhã/tarde/noite)
professor_id (FK)
data_cadastro

alunos

id (PK)
nome
email (unique)
cpf (unique)
data_nascimento
idade
nota_final
situacao (aprovado/reprovado/cursando)
turma_id (FK)
data_cadastro


🚀 Como Executar o Projeto
Opção 1: Executar Localmente
Pré-requisitos

Python 3.11+
pip

Passos

Clone o repositório

bashgit clone https://github.com/SEU_USUARIO/api-colegio-porto.git
cd api-colegio-porto

Crie um ambiente virtual

bashpython -m venv venv

Ative o ambiente virtual

bash# Windows (PowerShell)
venv\Scripts\Activate.ps1

# Windows (CMD)
venv\Scripts\activate.bat

# Mac/Linux
source venv/bin/activate

Instale as dependências

bashpip install -r requirements.txt

Popule o banco de dados (opcional)

bashpython popular_banco.py

Execute a aplicação

bashpython run.py

Acesse a API


URL Base: http://localhost:5000
Documentação Swagger: http://localhost:5000/docs


Opção 2: Executar com Docker
Pré-requisitos

Docker
Docker Compose

Passos

Clone o repositório

bashgit clone https://github.com/SEU_USUARIO/api-colegio-porto.git
cd api-colegio-porto

Build e execute

bashdocker-compose up --build

Acesse a API


URL Base: http://localhost:5000
Documentação Swagger: http://localhost:5000/docs


Para parar

bashCtrl + C
docker-compose down

📚 Documentação da API
A documentação completa está disponível via Swagger UI em:
http://localhost:5000/docs
Endpoints Disponíveis
👨‍🏫 Professores (/api/professores)

GET / - Lista todos os professores
GET /{id} - Busca professor por ID
POST / - Cria novo professor
PUT /{id} - Atualiza professor
DELETE /{id} - Deleta professor

🏫 Turmas (/api/turmas)

GET / - Lista todas as turmas
GET /{id} - Busca turma por ID
POST / - Cria nova turma
PUT /{id} - Atualiza turma
DELETE /{id} - Deleta turma

👨‍🎓 Alunos (/api/alunos)

GET / - Lista todos os alunos
GET /{id} - Busca aluno por ID
POST / - Cria novo aluno
PUT /{id} - Atualiza aluno
DELETE /{id} - Deleta aluno


🧪 Exemplos de Requisições
Criar um Professor
bashcurl -X POST "http://localhost:5000/api/professores/" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Carlos Silva",
    "email": "carlos@colegioporto.com.br",
    "cpf": "111.222.333-44",
    "idade": ".."
    "materia": "Matemática"
  }'
Criar uma Turma
bashcurl -X POST "http://localhost:5000/api/turmas/" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "SI 3B",
    "ano": 2024,
    "periodo": "noite",
    "professor_id": 1
  }'
Criar um Aluno
bashcurl -X POST "http://localhost:5000/api/alunos/" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "João Santos",
    "email": "joao@email.com",
    "cpf": "555.666.777-88",
    "data_nascimento": "15/05/2004",
    "idade": 20,
    "nota_final": 8.5,
    "situacao": "aprovado",
    "turma_id": 1
  }'

📊 Dados Iniciais
O script popular_banco.py cria os seguintes dados:

Professores

Kleber Chiles - DevOps
Giovani Bontempo - API
Odair Gabriel - Desenvolvimento Mobile

Turma

SI 3A - 2025 - Noite - Prof. Odair Gabriel

Alunas

Anna Julia Higa Farincho - Nota: 7.8 - Aprovada
Letícia Macedo - Nota: 8.2 - Aprovada
Evelyn Mercês - Nota: 7.5 - Aprovada


🎯 Funcionalidades Implementadas
✅ CRUD completo de Professores
✅ CRUD completo de Turmas
✅ CRUD completo de Alunos
✅ Relacionamentos entre entidades
✅ Validações de dados
✅ Tratamento de erros
✅ Documentação automática com Swagger
✅ Banco de dados SQLite com SQLAlchemy
✅ Arquitetura MVC
✅ Conteinerização com Docker
✅ Versionamento com Git/GitHub

🔍 Validações Implementadas

Email único para Professores e Alunos
CPF único para Professores e Alunos
Campos obrigatórios validados
Integridade referencial: não permite deletar Professor com Turmas ou Turma com Alunos
Data de nascimento no formato DD/MM/AAAA
Verificação de existência antes de vincular Professor à Turma


📝 Aprendizados do Projeto
Durante o desenvolvimento deste projeto, aprendemos:

Arquitetura MVC: Separação clara de responsabilidades
ORM SQLAlchemy: Trabalhar com banco de dados sem SQL direto
Relacionamentos: One-to-Many entre entidades
API REST: Verbos HTTP e códigos de status corretos
Documentação: Importância do Swagger para APIs
Docker: Conteinerização para facilitar deploy
Git/GitHub: Versionamento e trabalho em equipe


🐛 Problemas Encontrados e Soluções
Problema 1: Erro ao deletar Professor com Turmas
Solução: Implementamos validação que verifica se existem turmas vinculadas antes de permitir a deleção.
Problema 2: Data de nascimento em formato incorreto
Solução: Adicionamos parsing da data usando datetime.strptime() e tratamento de exceção.
Problema 3: Relacionamentos não apareciam no JSON
Solução: Criamos o método to_dict() em cada model para serializar corretamente os dados.

🚧 Melhorias Futuras

 Adicionar autenticação JWT
 Implementar paginação nas listagens
 Adicionar filtros de busca
 Criar sistema de notas por disciplina
 Adicionar upload de fotos
 Implementar relatórios em PDF
 Adicionar testes unitários


📄 Licença
Este projeto foi desenvolvido para fins educacionais como parte da disciplina de Desenvolvimento de Aplicações Móveis.

📞 Contato
Para dúvidas ou sugestões sobre o projeto, entre em contato com os integrantes do grupo.

Desenvolvido pelas alunas da Faculdade Impacta

🔗 Links Úteis

Documentação Flask
Documentação SQLAlchemy
Documentação Flasgger
Documentação Docker