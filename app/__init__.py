from flask import Flask
from config import config
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_envvar('APP_CONFIG')
    app.config.from_object(config[config_name])
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config[app.config['DATABASE_VAR']]
    config[config_name].init_app(app)

    from .main import main_blueprint
    app.register_blueprint(main_blueprint)

    db.init_app(app)

    return app
