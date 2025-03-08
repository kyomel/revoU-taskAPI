def validate_task_data(data):
    if 'title' not in data or not data['title']:
        return False, "Title is required."
    if 'description' not in data or not data['description']:
        return False, "Description is required."
    return True, ""

def format_response(data, message="", status_code=200):
    return {
        "status": status_code,
        "message": message,
        "data": data
    }