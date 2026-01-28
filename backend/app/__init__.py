import os

from flask import Flask
from dotenv import load_dotenv


def create_app() -> Flask:
    """
    Application factory for the Tic Tac Toe backend.
    """
    # Load environment variables (e.g. app.secret_key from .env)
    load_dotenv()

    # Point Flask to the dedicated frontend folders
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    template_dir = os.path.join(base_dir, "frontend", "templates")
    static_dir = os.path.join(base_dir, "frontend", "static")

    app = Flask(
        __name__,
        template_folder=template_dir,
        static_folder=static_dir,
    )
    app.secret_key = os.getenv("app.secret_key", "change-this-secret")

    # Register blueprints (routes)
    from .routes import bp as main_bp

    app.register_blueprint(main_bp)

    return app

