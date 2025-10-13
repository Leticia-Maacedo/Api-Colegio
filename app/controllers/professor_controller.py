from flask import Blueprint, request, jsonify
from app import db
from app.models.professor import Professor

professor_bp = Blueprint('professores', __name__, url_prefix='/api/professores')


@professor_bp.route('/', methods=['GET'])
def listar_professores():
    """
    Lista todos os professores
    ---
    tags:
      - Professores
    responses:
      200:
        description: Lista de professores retornada com sucesso
        schema:
          type: array
          items:
            type: object
    """
    professores = Professor.query.all()
    return jsonify([p.to_dict() for p in professores]), 200


@professor_bp.route('/<int:id>', methods=['GET'])
def buscar_professor(id):
    """
    Busca um professor pelo ID
    ---
    tags:
      - Professores
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do professor
    responses:
      200:
        description: Professor encontrado
      404:
        description: Professor nao encontrado
    """
    professor = Professor.query.get(id)
    
    if not professor:
        return jsonify({'erro': 'Professor nao encontrado'}), 404
    
    return jsonify(professor.to_dict()), 200


@professor_bp.route('/', methods=['POST'])
def criar_professor():
    """
    Cria um novo professor
    ---
    tags:
      - Professores
    parameters:
      - in: body
        name: body
        required: true
        schema:
          required:
            - nome
            - email
            - cpf
          properties:
            nome:
              type: string
              example: Joao
            email:
              type: string
              example: joao@email.com
            cpf:
              type: string
              example: 123.456.789-00
            idade:
              type: integer
              example: 30
            materia:
              type: string
              example: Matematica
    responses:
      201:
        description: Professor criado com sucesso
      400:
        description: Dados invalidos
    """
    dados = request.get_json()

    if not dados.get('nome'):
        return jsonify({'erro': 'Nome e obrigatorio'}), 400
    if not dados.get('email'):
        return jsonify({'erro': 'Email e obrigatorio'}), 400
    if not dados.get('cpf'):
        return jsonify({'erro': 'CPF e obrigatorio'}), 400

    if Professor.query.filter_by(email=dados['email']).first():
        return jsonify({'erro': 'Email ja cadastrado'}), 400
    if Professor.query.filter_by(cpf=dados['cpf']).first():
        return jsonify({'erro': 'CPF ja cadastrado'}), 400

    novo = Professor(
        nome=dados['nome'],
        email=dados['email'],
        cpf=dados['cpf'],
        idade=str(dados.get('idade')) if dados.get('idade') is not None else None,
        materia=dados.get('materia')
    )
    try:
        db.session.add(novo)
        db.session.commit()
        return jsonify(novo.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': f'Erro ao criar professor: {str(e)}'}), 500


@professor_bp.route('/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    """
    Atualiza um professor
    ---
    tags:
      - Professores
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
            idade:
              type: integer
            materia:
              type: string
    responses:
      200:
        description: Professor atualizado com sucesso
      404:
        description: Professor nao encontrado
    """
    professor = Professor.query.get(id)
    if not professor:
        return jsonify({'erro': 'Professor nao encontrado'}), 404

    dados = request.get_json()

    try:
        if 'nome' in dados:
            professor.nome = dados['nome']
        if 'email' in dados:
            existe = Professor.query.filter_by(email=dados['email']).first()
            if existe and existe.id != id:
                return jsonify({'erro': 'Email ja cadastrado'}), 400
            professor.email = dados['email']
        if 'cpf' in dados:
            existe = Professor.query.filter_by(cpf=dados['cpf']).first()
            if existe and existe.id != id:
                return jsonify({'erro': 'CPF ja cadastrado'}), 400
            professor.cpf = dados['cpf']
        if 'idade' in dados:
            professor.idade = str(dados['idade']) if dados['idade'] is not None else None
        if 'materia' in dados:
            professor.materia = dados['materia']

        db.session.commit()
        return jsonify(professor.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': f'Erro ao atualizar: {str(e)}'}), 500


@professor_bp.route('/<int:id>', methods=['DELETE'])
def deletar_professor(id):
    """
    Deleta um professor
    ---
    tags:
      - Professores
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Professor deletado com sucesso
      404:
        description: Professor nao encontrado
    """
    professor = Professor.query.get(id)
    if not professor:
        return jsonify({'erro': 'Professor nao encontrado'}), 404

    try:
        db.session.delete(professor)
        db.session.commit()
        return jsonify({'mensagem': 'Professor deletado com sucesso'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': f'Erro ao deletar: {str(e)}'}), 500
