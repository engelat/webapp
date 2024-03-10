from flask import Flask
from app import views, apis  # Importing using absolute paths

def create_app():
    app = Flask(__name__)
    with app.app_context():
        # Views and APIs are now imported using absolute paths
        pass
    return app
