from flask import Blueprint, request, jsonify
from app import db
from app.models.aluno import Aluno
from app.models.turma import Turma
from datetime import datetime

aluno_bp = Blueprint('alunos', __name__, url_prefix='/api/alunos')


@aluno_bp.route('/', methods=['GET'])
def listar_alunos():
    """
    Lista todos os alunos
    ---
    tags:
      - Alunos
    responses:
      200:
        description: Lista de alunos retornada com sucesso
    """
    alunos = Aluno.query.all()
    return jsonify([a.to_dict() for a in alunos]), 200


@aluno_bp.route('/<int:id>', methods=['GET'])
def buscar_aluno(id):
    """
    Busca um aluno pelo ID
    ---
    tags:
      - Alunos
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Aluno encontrado
      404:
        description: Aluno nao encontrado
    """
    aluno = Aluno.query.get(id)
    
    if not aluno:
        return jsonify({'erro': 'Aluno nao encontrado'}), 404
    
    return jsonify(aluno.to_dict()), 200


@aluno_bp.route('/', methods=['POST'])
def criar_aluno():
    """
    Cria um novo aluno
    ---
    tags:
      - Alunos
    parameters:
      - in: body
        name: body
        required: true
        schema:
          required:
            - nome
            - email
            - cpf
            - data_nascimento
            - idade
          properties:
            nome:
              type: string
              example: Maria Silva
            email:
              type: string
              example: maria@email.com
            cpf:
              type: string
              example: 987.654.321-00
            data_nascimento:
              type: string
              example: 10/02/2005
            idade:
              type: integer
              example: 20
            nota_final:
              type: number
              example: 7.5
            situacao:
              type: string
              example: aprovado
            turma_id:
              type: integer
              example: 1
    responses:
      201:
        description: Aluno criado com sucesso
      400:
        description: Dados invalidos
    """
    dados = request.get_json()
    
    # validacoes
    if not dados.get('nome'):
        return jsonify({'erro': 'Nome e obrigatorio'}), 400
    
    if not dados.get('email'):
        return jsonify({'erro': 'Email e obrigatorio'}), 400
    
    if not dados.get('cpf'):
        return jsonify({'erro': 'CPF e obrigatorio'}), 400
    
    if not dados.get('data_nascimento'):
        return jsonify({'erro': 'Data de nascimento e obrigatoria'}), 400
    
    if not dados.get('idade'):
        return jsonify({'erro': 'Idade e obrigatoria'}), 400
    
    # verifica se ja existe
    if Aluno.query.filter_by(email=dados['email']).first():
        return jsonify({'erro': 'Email ja cadastrado'}), 400
    
    if Aluno.query.filter_by(cpf=dados['cpf']).first():
        return jsonify({'erro': 'CPF ja cadastrado'}), 400
    
    # verifica se turma existe (se foi informada)
    if dados.get('turma_id'):
        turma = Turma.query.get(dados['turma_id'])
        if not turma:
            return jsonify({'erro': 'Turma nao encontrada'}), 404
    
    try:
        # converte a data de string para date
        data_nasc = datetime.strptime(dados['data_nascimento'], '%d/%m/%Y').date()
        
        novo_aluno = Aluno(
            nome=dados['nome'],
            email=dados['email'],
            cpf=dados['cpf'],
            data_nascimento=data_nasc,
            idade=dados['idade'],
            nota_final=dados.get('nota_final'),
            situacao=dados.get('situacao'),
            turma_id=dados.get('turma_id')
        )
        
        db.session.add(novo_aluno)
        db.session.commit()
        
        return jsonify(novo_aluno.to_dict()), 201
        
    except ValueError:
        return jsonify({'erro': 'Data de nascimento invalida. Use o formato DD/MM/AAAA'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': f'Erro ao criar aluno: {str(e)}'}), 500


@aluno_bp.route('/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    """
    Atualiza um aluno
    ---
    tags:
      - Alunos
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        schema:
          properties:
            nome:
              type: string
            email:
              type: string
            cpf:
              type: string
            data_nascimento:
              type: string
            idade:
              type: integer
            nota_final:
              type: number
            situacao:
              type: string
            turma_id:
              type: integer
    responses:
      200:
        description: Aluno atualizado com sucesso
      404:
        description: Aluno nao encontrado
    """
    aluno = Aluno.query.get(id)
    
    if not aluno:
        return jsonify({'erro': 'Aluno nao encontrado'}), 404
    
    dados = request.get_json()
    
    try:
        if 'nome' in dados:
            aluno.nome = dados['nome']
        
        if 'email' in dados:
            existe = Aluno.query.filter_by(email=dados['email']).first()
            if existe and existe.id != id:
                return jsonify({'erro': 'Email ja cadastrado'}), 400
            aluno.email = dados['email']
        
        if 'cpf' in dados:
            existe = Aluno.query.filter_by(cpf=dados['cpf']).first()
            if existe and existe.id != id:
                return jsonify({'erro': 'CPF ja cadastrado'}), 400
            aluno.cpf = dados['cpf']
        
        if 'data_nascimento' in dados:
            aluno.data_nascimento = datetime.strptime(dados['data_nascimento'], '%d/%m/%Y').date()
        
        if 'idade' in dados:
            aluno.idade = dados['idade']
        
        if 'nota_final' in dados:
            aluno.nota_final = dados['nota_final']
        
        if 'situacao' in dados:
            aluno.situacao = dados['situacao']
        
        if 'turma_id' in dados:
            if dados['turma_id']:
                turma = Turma.query.get(dados['turma_id'])
                if not turma:
                    return jsonify({'erro': 'Turma nao encontrada'}), 404
            aluno.turma_id = dados['turma_id']
        
        db.session.commit()
        return jsonify(aluno.to_dict()), 200
        
    except ValueError:
        return jsonify({'erro': 'Data de nascimento invalida. Use o formato DD/MM/AAAA'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': f'Erro ao atualizar: {str(e)}'}), 500


@aluno_bp.route('/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    """
    Deleta um aluno
    ---
    tags:
      - Alunos
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Aluno deletado com sucesso
      404:
        description: Aluno nao encontrado
    """
    aluno = Aluno.query.get(id)
    
    if not aluno:
        return jsonify({'erro': 'Aluno nao encontrado'}), 404
    
    try:
        db.session.delete(aluno)
        db.session.commit()
        return jsonify({'mensagem': 'Aluno deletado com sucesso'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': f'Erro ao deletar: {str(e)}'}), 500
