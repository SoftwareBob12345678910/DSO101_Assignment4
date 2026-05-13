from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database for tasks
tasks = []

@app.route('/', methods=['GET'])
def home():
    """Home endpoint - returns a welcome message"""
    return jsonify({
        'message': 'Welcome to the CI/CD Pipeline API',
        'status': 'success',
        'version': '1.0.0'
    }), 200

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'CI/CD Pipeline API'
    }), 200

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    return jsonify({
        'tasks': tasks,
        'count': len(tasks)
    }), 200

@app.route('/api/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    
    task = {
        'id': len(tasks) + 1,
        'title': data['title'],
        'description': data.get('description', ''),
        'completed': False
    }
    
    tasks.append(task)
    return jsonify(task), 201

@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Get a specific task by ID"""
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    return jsonify(task), 200

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Update a task"""
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    data = request.get_json()
    task.update(data)
    
    return jsonify(task), 200

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task"""
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    
    return jsonify({'message': 'Task deleted'}), 200

@app.route('/api/add', methods=['POST'])
def add_numbers():
    """Add two numbers - for testing"""
    data = request.get_json()
    
    if not data or 'a' not in data or 'b' not in data:
        return jsonify({'error': 'Both a and b are required'}), 400
    
    try:
        result = float(data['a']) + float(data['b'])
        return jsonify({
            'a': data['a'],
            'b': data['b'],
            'result': result
        }), 200
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid input types'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
