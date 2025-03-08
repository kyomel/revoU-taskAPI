# README.md

# Task Manager API

This is a simple Task Manager API built with Flask. It implements basic CRUD operations for managing tasks.

## Features

- Create a new task
- Retrieve all tasks
- Retrieve a specific task by ID
- Update an existing task
- Delete a task

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd task-manager-api
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/app.py
   ```

2. The API will be available at `http://localhost:5000`.

## API Endpoints

- `GET /tasks` - Retrieve all tasks
- `GET /tasks/<id>` - Retrieve a task by ID
- `POST /tasks` - Create a new task
- `PUT /tasks/<id>` - Update an existing task
- `DELETE /tasks/<id>` - Delete a task

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.