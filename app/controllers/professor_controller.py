from flask import Blueprint, request, jsonify
from app import db
from app.models.professor import Professor

# cria o blueprint para as rotas de professor
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
