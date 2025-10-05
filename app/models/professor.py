from app import db
from datetime import datetime

class Professor(db.Model):
    __tablename__ = 'professores'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    idade = db.Column(db.String(2), unique=True, nullable=False)    
    materia = db.Column(db.String(50))
    data_cadastro = db.Column(db.DateTime, default=datetime.utcnow)
    turmas = db.relationship('Turma', backref='professor', lazy=True)
    
    def __repr__(self):
        return f'<Professor {self.nome}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'cpf': self.cpf,
            'idade': self.idade,
            'materia': self.materia,
            'data_cadastro': self.data_cadastro.strftime('%d/%m/%Y %H:%M')
        }
