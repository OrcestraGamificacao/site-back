import os
from flask import Flask, jsonify
from flask_sqlalchemy  import SQLAlchemy
from app.models import HTTPError
import app.config as cf

app = cf.create_app(__name__)
db = cf.get_db_instance(app)

# Register views
from app.views.task import task_blueprint

app.register_blueprint(task_blueprint)

# Register handlers
@app.errorhandler(HTTPError)
def handle_http_error(error):
    res = jsonify(error.to_dict())
    res.status_code = error.status_code

    return res

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')