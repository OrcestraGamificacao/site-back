from flask import Blueprint, jsonify

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
