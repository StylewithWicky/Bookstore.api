from flask import Flask
from flask_sqlalchemy import SQLALCHEMY
from flask_migrate import Migrate
from config import Config

db=SQLALCHEMY()
migrate=Migrate()

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app,db)

    from .controllers import register_routes
    register_routes(app)
    
    return app