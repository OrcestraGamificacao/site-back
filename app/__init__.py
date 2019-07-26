from flask import Flask
from app.views.task import task_blueprint

app = Flask(__name__)

@app.route('/')
def home():
    return 'OLA MUNDO'

app.register_blueprint(task_blueprint)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')