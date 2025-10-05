from app import db
from datetime import datetime

class Professor(db.Model):
    # nome da tabela no banco
    __tablename__ = 'professores'
    
    # colunas da tabela
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    materia = db.Column(db.String(50))
    data_cadastro = db.Column(db.DateTime, default=datetime.utcnow)
    
    # relacionamento: um professor pode ter varias turmas
    turmas = db.relationship('Turma', backref='professor', lazy=True)
    
    def __repr__(self):
        return f'<Professor {self.nome}>'
    
    # converte o objeto para dicionario (usado no json)
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'cpf': self.cpf,
            'materia': self.materia,
            'data_cadastro': self.data_cadastro.strftime('%d/%m/%Y %H:%M')
        }
