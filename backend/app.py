from flask import Flask
from backend.config import Config
from backend.extensions import db, jwt
from routes.auth import auth_bp
from routes.admin import admin_bp
from routes.user import user_bp
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)   
    CORS(app)

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(user_bp, url_prefix="/user")

    with app.app_context():
        db.create_all()

    @app.route("/")
    def home():
        return {"message": "Apartment Backend Running"}

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
