from flask import Blueprint, jsonify, request
from app.models import Task
from app import db

task_blueprint = Blueprint('tasks', __name__, url_prefix='/tasks')

@task_blueprint.route('/')
def collection_get():
    return jsonify([
        {
            "Hello": "Wolrd"
        }
    ])

@task_blueprint.route('/<int:task_id>')
def resource_get(task_id):
    return jsonify({
        'Hello': 'World'
    })

@task_blueprint.route('/', methods=['POST'])
def post():
    data = request.get_json()
    print(data)
    name = data.get('name', 'No Name')
    description = data.get('description', 'No description provided')
    done = (data.get('done', False) in ('true', 'True', True))
    task = Task(name, description, done)
    print('Start saving in db')
    db.session.add(task)
    db.session.commit()
    print('Flushed in db')

    return jsonify(task.to_dict()), 201
