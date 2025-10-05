import os

class Config:
    # pega o caminho absoluto do projeto
    basedir = os.path.abspath(os.path.dirname(__file__))
    
    # caminho do banco de dados sqlite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'colegio_porto.db')
    
    # desabilita tracking de modificacoes (economiza memoria)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # chave secreta para sessoes
    SECRET_KEY = 'porto-secreto-2024'