from flask import Flask
from app.config import DevelopmentConfig
from app.utils.db import initialize_db
from app.routes.users import users_bp

def create_app():
    app = Flask(__name__)

    # Load configuration
    # app.config.from_object('app.config.DevelopmentConfig')
    app.config.from_object(DevelopmentConfig)
    # Initialize database
    initialize_db(app)

    # Register blueprints
    app.register_blueprint(users_bp)

    return app