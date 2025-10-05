from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec',
                "route": '/apispec.json',
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/docs"
    }
    
    template = {
        "info": {
            "title": "API Colégio Porto",
            "description": "API REST para gerenciamento escolar",
            "version": "1.0.0"
        }
    }
    
    Swagger(app, config=swagger_config, template=template)
    
    with app.app_context():
        db.create_all()
    from app.controllers.professor_controller import professor_bp
    from app.controllers.turma_controller import turma_bp
    from app.controllers.aluno_controller import aluno_bp
    app.register_blueprint(professor_bp)
    app.register_blueprint(turma_bp)
    app.register_blueprint(aluno_bp)
    
    return app
