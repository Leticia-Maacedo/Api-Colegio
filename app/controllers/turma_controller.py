from flask import Blueprint, request, jsonify
from app import db
from app.models.turma import Turma
from app.models.professor import Professor

turma_bp = Blueprint('turmas', __name__, url_prefix='/api/turmas')


@turma_bp.route('/', methods=['GET'])
def listar_turmas():
    """
    Lista todas as turmas
    ---
    tags:
      - Turmas
    responses:
      200:
        description: Lista de turmas retornada com sucesso
    """
    turmas = Turma.query.all()
    return jsonify([t.to_dict() for t in turmas]), 200


@turma_bp.route('/<int:id>', methods=['GET'])
def buscar_turma(id):
    """
    Busca uma turma pelo ID
    ---
    tags:
      - Turmas
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Turma encontrada
      404:
        description: Turma nao encontrada
    """
    turma = Turma.query.get(id)
    
    if not turma:
        return jsonify({'erro': 'Turma nao encontrada'}), 404
    
    return jsonify(turma.to_dict()), 200


@turma_bp.route('/', methods=['POST'])
def criar_turma():
    """
    Cria uma nova turma
    ---
    tags:
      - Turmas
    parameters:
      - in: body
        name: body
        required: true
        schema:
          required:
            - nome
            - ano
          properties:
            nome:
              type: string
              example: SI 3A
            ano:
              type: integer
              example: 2025
            periodo:
              type: string
              example: noite
            professor_id:
              type: integer
              example: 1
    responses:
      201:
        description: Turma criada com sucesso
      400:
        description: Dados invalidos
    """
    dados = request.get_json()
    
    if not dados.get('nome'):
        return jsonify({'erro': 'Nome e obrigatorio'}), 400
    
    if not dados.get('ano'):
        return jsonify({'erro': 'Ano e obrigatorio'}), 400
    
    if dados.get('professor_id'):
        professor = Professor.query.get(dados['professor_id'])
        if not professor:
            return jsonify({'erro': 'Professor nao encontrado'}), 404
    
    try:
        nova_turma = Turma(
            nome=dados['nome'],
            ano=dados['ano'],
            periodo=dados.get('periodo'),
            professor_id=dados.get('professor_id')
        )
        
        db.session.add(nova_turma)
        db.session.commit()
        
        return jsonify(nova_turma.to_dict()), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': f'Erro ao criar turma: {str(e)}'}), 500


@turma_bp.route('/<int:id>', methods=['PUT'])
def atualizar_turma(id):
    """
    Atualiza uma turma
    ---
    tags:
      - Turmas
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
            ano:
              type: integer
            periodo:
              type: string
            professor_id:
              type: integer
    responses:
      200:
        description: Turma atualizada com sucesso
      404:
        description: Turma nao encontrada
    """
    turma = Turma.query.get(id)
    
    if not turma:
        return jsonify({'erro': 'Turma nao encontrada'}), 404
    
    dados = request.get_json()
    
    try:
        if 'nome' in dados:
            turma.nome = dados['nome']
        
        if 'ano' in dados:
            turma.ano = dados['ano']
        
        if 'periodo' in dados:
            turma.periodo = dados['periodo']
        
        if 'professor_id' in dados:
            if dados['professor_id']:
                professor = Professor.query.get(dados['professor_id'])
                if not professor:
                    return jsonify({'erro': 'Professor nao encontrado'}), 404
            turma.professor_id = dados['professor_id']
        
        db.session.commit()
        return jsonify(turma.to_dict()), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': f'Erro ao atualizar: {str(e)}'}), 500


@turma_bp.route('/<int:id>', methods=['DELETE'])
def deletar_turma(id):
    """
    Deleta uma turma
    ---
    tags:
      - Turmas
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Turma deletada com sucesso
      404:
        description: Turma nao encontrada
      400:
        description: Turma possui alunos vinculados
    """
    turma = Turma.query.get(id)
    
    if not turma:
        return jsonify({'erro': 'Turma nao encontrada'}), 404
    
    if turma.alunos:
        return jsonify({'erro': 'Nao e possivel deletar turma com alunos vinculados'}), 400
    
    try:
        db.session.delete(turma)
        db.session.commit()
        return jsonify({'mensagem': 'Turma deletada com sucesso'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': f'Erro ao deletar: {str(e)}'}), 500
