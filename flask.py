from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    # Perform validation on the received data

    # Generate a unique ID for the task
    task_id = len(tasks) + 1

    # Create the task object
    task = {
        'id': task_id,
        'title': data['title'],
        'description': data['description'],
        'due_date': data['due_date'],
        'status': 'Incomplete'
    }

    # Add the task to the list
    tasks.append(task)

    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)

    if task:
        return jsonify(task)
    else:
        return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)

    if task:
        data = request.get_json()
        # Perform validation on the received data

        task['title'] = data['title']
        task['description'] = data['description']
        task['due_date'] = data['due_date']
        task['status'] = data['status']

        return jsonify(task)
    else:
        return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)

    if task:
        tasks.remove(task)
        return jsonify({'message': 'Task deleted'})
    else:
        return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks', methods=['GET'])
def list_tasks():
    # Implement pagination here if desired
    return jsonify(tasks)
