from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

tasks = []
task_id_counter = 1


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", tasks=tasks)


@app.route("/tasks", methods=["GET"])
def get():
    if request.headers.get("Accept") == "application/json":
        return jsonify(tasks)
    return redirect(url_for("index"))


@app.route("/tasks", methods=["POST"])
def create():
    global task_id_counter

    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    if not data or "title" not in data:
        return jsonify({"error": "Title cannot be empty"}), 400

    new = {
        "id": task_id_counter,
        "title": data["title"],
        "description": data.get("description", ""),
        "completed": False,
    }

    tasks.append(new)
    task_id_counter += 1

    if request.is_json:
        return jsonify(new), 201
    return redirect(url_for("index"))


@app.route("/tasks/<int:task_id>", methods=["POST", "PUT", "DELETE"])
def task_operations(task_id):
    method = request.form.get("_method", request.method).upper()

    if method == "PUT":
        for task in tasks:
            if task["id"] == task_id:
                if request.is_json:
                    data = request.get_json()
                    task["title"] = data.get("title", task["title"])
                    task["description"] = data.get("description", task["description"])
                    task["completed"] = data.get("completed", task["completed"])
                else:
                    task["completed"] = request.form.get("completed") == "true"

                if request.is_json:
                    return jsonify(task)
                return redirect(url_for("index"))

    elif method == "DELETE":
        for index, task in enumerate(tasks):
            if task["id"] == task_id:
                deleted_task = tasks.pop(index)
                if request.is_json:
                    return jsonify(deleted_task)
                return redirect(url_for("index"))

    return jsonify({"error": "Task not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
