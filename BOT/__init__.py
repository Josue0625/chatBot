from flask import Flask

def create_app():
    app = Flask(__name__,instance_relative_config=False)

    with app.app_context():
        from .home import home
        from .service_api import service_api


        app.register_blueprint(home.home_bp)
        app.register_blueprint(service_api.service_api_bp)

        return app