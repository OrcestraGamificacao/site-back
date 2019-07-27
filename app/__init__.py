import os
from flask import Flask
from flask_sqlalchemy  import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI', 'postgresql://anitta:123456@localhost:5433/flaskapp')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app=app)

# Register views
from app.views.task import task_blueprint

@app.route('/')
def home():
    return 'OLA MUNDO'

app.register_blueprint(task_blueprint)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')