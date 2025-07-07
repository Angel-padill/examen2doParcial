from flask import Flask
from flask_cors import CORS
from config import Config
from database import db
from routes.gasto_routes import gasto_bp

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

db.init_app(app)
with app.app_context():
    db.create_all()

app.register_blueprint(gasto_bp)

if __name__ == '__main__':
    app.run(debug=True)
