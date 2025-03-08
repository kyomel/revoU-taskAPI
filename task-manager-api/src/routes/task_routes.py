from flask import Blueprint
from controllers.task_controller import TaskController

task_routes = Blueprint('task_routes', __name__)
controller = TaskController()

def register_routes(app):
    task_routes.add_url_rule('/tasks', view_func=controller.get_tasks, methods=['GET'])
    task_routes.add_url_rule('/tasks/<int:task_id>', view_func=controller.get_task, methods=['GET'])
    task_routes.add_url_rule('/tasks', view_func=controller.create_task, methods=['POST'])
    task_routes.add_url_rule('/tasks/<int:task_id>', view_func=controller.update_task, methods=['PUT'])
    task_routes.add_url_rule('/tasks/<int:task_id>', view_func=controller.delete_task, methods=['DELETE'])
    
    app.register_blueprint(task_routes)