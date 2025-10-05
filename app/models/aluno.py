from app import db
from datetime import datetime

class Aluno(db.Model):
    __tablename__ = 'alunos'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=True)
    nota_primeiro_semestre = db.Column(db.Float)
    nota_segundo_semestre = db.Column(db.Float)
    nota_final = db.Column(db.Float)
    situacao = db.Column(db.String(20))  # aprovado, reprovado, cursando
    data_cadastro = db.Column(db.DateTime, default=datetime.utcnow)
    
    # chave estrangeira para turma
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=True)
    
    def __repr__(self):
        return f'<Aluno {self.nome}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'cpf': self.cpf,
            'data_nascimento': self.data_nascimento.strftime('%d/%m/%Y'),
            'idade': self.idade,
            'nota_final': self.nota_final,
            'situacao': self.situacao,
            'turma_id': self.turma_id,
            'turma': self.turma.nome if self.turma else None,
            'data_cadastro': self.data_cadastro.strftime('%d/%m/%Y %H:%M')
        }
