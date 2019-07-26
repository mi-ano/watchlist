import os

class Config:

    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}

def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app