from flask import Flask
from website.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from website.main.routes import main
    from website.errors.handlers import errors
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app