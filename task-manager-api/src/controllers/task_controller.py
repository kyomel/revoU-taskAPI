class TaskController:
    def __init__(self):
        self.tasks = []
        self.counter = 1

    def get_tasks(self):
        return self.tasks

    def get_task(self, task_id):
        task = next((task for task in self.tasks if task['id'] == task_id), None)
        return task

    def create_task(self, title, description):
        task = {
            'id': self.counter,
            'title': title,
            'description': description,
            'completed': False
        }
        self.tasks.append(task)
        self.counter += 1
        return task

    def update_task(self, task_id, title=None, description=None, completed=None):
        task = self.get_task(task_id)
        if task:
            if title is not None:
                task['title'] = title
            if description is not None:
                task['description'] = description
            if completed is not None:
                task['completed'] = completed
            return task
        return None

    def delete_task(self, task_id):
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            return task
        return None