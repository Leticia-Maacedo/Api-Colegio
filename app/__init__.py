from flask import Flask, send_from_directory, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
import os
import json

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # --- Serve a interface do Swagger UI ---
    @app.route('/docs')
    def swagger_ui():
        # Mostra o HTML do Swagger UI (usando CDN oficial)
        html_content = """
        <!DOCTYPE html>
        <html lang="pt-br">
          <head>
            <meta charset="UTF-8" />
            <title>API Colegio Porto</title>
            <link rel="stylesheet" type="text/css"
              href="https://unpkg.com/swagger-ui-dist/swagger-ui.css" />
          </head>
          <body>
            <div id="swagger-ui"></div>
            <script src="https://unpkg.com/swagger-ui-dist/swagger-ui-bundle.js"></script>
            <script>
              window.onload = () => {
                SwaggerUIBundle({ url: '/swagger.json', dom_id: '#swagger-ui' });
              };
            </script>
          </body>
        </html>
        """
        return html_content

    # --- Serve o arquivo swagger.json ---
    @app.route('/swagger.json')
    def swagger_spec():
        with open(os.path.join(app.root_path, 'swagger', 'swagger.json')) as f:
            return jsonify(json.load(f))

    with app.app_context():
        db.create_all()

    # --- Importa e registra blueprints ---
    from app.controllers.professor_controller import professor_bp
    from app.controllers.turma_controller import turma_bp
    from app.controllers.aluno_controller import aluno_bp
    app.register_blueprint(professor_bp)
    app.register_blueprint(turma_bp)
    app.register_blueprint(aluno_bp)

    return app