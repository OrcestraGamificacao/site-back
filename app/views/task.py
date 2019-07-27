from flask import Blueprint, jsonify, request, current_app
from app.models import Task, HTTPError
from app import db

task_blueprint = Blueprint('tasks', __name__, url_prefix='/tasks')

@task_blueprint.route('/')
def task_collection_get():
    current_app.logger.debug('Get all tasks')
    all_tasks = db.session.query(Task) \
        .order_by(Task.task_id).all()

    tasks = []
    for item in all_tasks:
        tasks.append(item.to_dict())

    return jsonify(tasks), 200

@task_blueprint.route('/<int:task_id>', methods=['GET'])
def task_resource_get(task_id):
    current_app.logger.debug('Start request')
    task = db.session.query(Task) \
        .filter(Task.task_id == task_id).first()

    if not task:
        current_app.logger.debug('Task does not exist')
        raise HTTPError("Task not found", status_code=404)

    return jsonify(task.to_dict()), 200

@task_blueprint.route('/', methods=['POST'])
def task_post():
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

@task_blueprint.route('/<int:task_id>', methods=['PUT', 'PATCH'])
def task_delete(task_id):
    data = request.get_json()
    print(data)
    task = db.session.query(Task).filter(Task.task_id == task_id).first()

    if not task:
        raise HTTPError('Task not found', status_code=404)

    for item in data:
        if item == 'done':
            item = (data[item] in ('true', 'True', True))
            task.done = item
        else:
            setattr(task, item, data[item])

    db.session.commit()
    return jsonify(task.to_dict()), 200

@task_blueprint.route('/<int:task_id>', methods=['DELETE'])
def update(task_id):
    task = db.session.query(Task).filter(Task.task_id == task_id).first()

    if not task:
        raise HTTPError('Task not found', status_code=404)

    db.session.delete(task)
    db.session.commit()
    return jsonify({}), 204