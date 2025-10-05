from app import db


class Turma(db.Model):
    __tablename__ = 'turmas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    periodo = db.Column(db.String(20))

    # relacionamento com Professor (opcional)
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=True)

    # relacionamento com Aluno
    alunos = db.relationship('Aluno', backref='turma', lazy=True)

    def __repr__(self):
        return f'<Turma {self.nome}>'

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'ano': self.ano,
            'periodo': self.periodo,
            'professor_id': self.professor_id,
        }


