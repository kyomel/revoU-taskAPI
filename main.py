from flask import Flask, jsonify, request

app = Flask(__name__)

tasks_db = {
    "tasks": {
        "1": {
            "id": 1,
            "title": "Task Title",
            "description": "Task Description",
            "completed": False,
        }
    }
}

def get_all_tasks():
    task_list = []
    for task_id, task in tasks_db["tasks"].items():
        task_list.append(task)
    return task_list

def get_specific_task(task_id):
    task = tasks_db["tasks"][task_id]
    return task

def register_task_repository(task_data, task_id):
    tasks_db.update({f"{task_id}" : task_data})

def register_task(task_data):
    task_id = int(max(tasks_db.keys())) + 1
    task_data.update({"id" : f"{task_id}", "completed" : False})
    register_task_repository(task_data, task_id)
    return task_data


# optional route for argument
@app.route("/tasks", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
@app.route("/tasks/<task_id>", methods=["GET"])
def specific_task(task_id = False):
    match request.method:
        case "GET":
            if task_id:
                return get_specific_task(task_id)

            else:
                return get_all_tasks()
        
        case "POST":
            return register_task(request.json)

        # case "PUT":


        # case "DELETE":


        # case "PATCH":


    # return jsonify({"test" : task_id}), 200
