import pytest
import json
from app import app, tasks

@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def reset_tasks():
    """Reset tasks before each test"""
    global tasks
    tasks.clear()
    yield
    tasks.clear()

class TestHomeEndpoint:
    """Tests for the home endpoint"""
    
    def test_home_returns_200(self, client):
        """Test that home endpoint returns 200 status"""
        response = client.get('/')
        assert response.status_code == 200
    
    def test_home_returns_correct_message(self, client):
        """Test that home endpoint returns correct message"""
        response = client.get('/')
        data = json.loads(response.data)
        assert data['message'] == 'Welcome to the CI/CD Pipeline API'
        assert data['status'] == 'success'

class TestHealthCheck:
    """Tests for the health check endpoint"""
    
    def test_health_check_returns_200(self, client):
        """Test that health check returns 200 status"""
        response = client.get('/api/health')
        assert response.status_code == 200
    
    def test_health_check_returns_healthy_status(self, client):
        """Test that health check returns healthy status"""
        response = client.get('/api/health')
        data = json.loads(response.data)
        assert data['status'] == 'healthy'

class TestTaskOperations:
    """Tests for task CRUD operations"""
    
    def test_get_tasks_empty(self, client):
        """Test getting tasks when list is empty"""
        response = client.get('/api/tasks')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['count'] == 0
        assert data['tasks'] == []
    
    def test_create_task_success(self, client):
        """Test creating a new task"""
        task_data = {
            'title': 'Test Task',
            'description': 'This is a test task'
        }
        response = client.post('/api/tasks', 
                              json=task_data,
                              content_type='application/json')
        assert response.status_code == 201
        data = json.loads(response.data)
        assert data['title'] == 'Test Task'
        assert data['description'] == 'This is a test task'
        assert data['completed'] == False
    
    def test_create_task_missing_title(self, client):
        """Test creating a task without title"""
        task_data = {'description': 'No title'}
        response = client.post('/api/tasks',
                              json=task_data,
                              content_type='application/json')
        assert response.status_code == 400
    
    def test_get_specific_task(self, client):
        """Test getting a specific task by ID"""
        # Create a task first
        task_data = {'title': 'Task 1'}
        client.post('/api/tasks', json=task_data, content_type='application/json')
        
        # Get the task
        response = client.get('/api/tasks/1')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['title'] == 'Task 1'
    
    def test_get_nonexistent_task(self, client):
        """Test getting a task that doesn't exist"""
        response = client.get('/api/tasks/999')
        assert response.status_code == 404
    
    def test_delete_task(self, client):
        """Test deleting a task"""
        # Create a task
        task_data = {'title': 'Task to delete'}
        client.post('/api/tasks', json=task_data, content_type='application/json')
        
        # Delete the task
        response = client.delete('/api/tasks/1')
        assert response.status_code == 200
        
        # Verify it's deleted
        response = client.get('/api/tasks/1')
        assert response.status_code == 404

class TestAddNumbers:
    """Tests for the add numbers endpoint"""
    
    def test_add_numbers_success(self, client):
        """Test adding two numbers successfully"""
        data = {'a': 5, 'b': 3}
        response = client.post('/api/add',
                              json=data,
                              content_type='application/json')
        assert response.status_code == 200
        result_data = json.loads(response.data)
        assert result_data['result'] == 8
    
    def test_add_numbers_floats(self, client):
        """Test adding float numbers"""
        data = {'a': 5.5, 'b': 2.5}
        response = client.post('/api/add',
                              json=data,
                              content_type='application/json')
        assert response.status_code == 200
        result_data = json.loads(response.data)
        assert result_data['result'] == 8.0
    
    def test_add_numbers_missing_parameter(self, client):
        """Test adding numbers with missing parameter"""
        data = {'a': 5}
        response = client.post('/api/add',
                              json=data,
                              content_type='application/json')
        assert response.status_code == 400
    
    def test_add_numbers_invalid_type(self, client):
        """Test adding with invalid input types"""
        data = {'a': 'abc', 'b': 'def'}
        response = client.post('/api/add',
                              json=data,
                              content_type='application/json')
        assert response.status_code == 400

class TestBasicMath:
    """Basic math tests"""
    
    def test_simple_addition(self):
        """Test basic addition"""
        assert 1 + 1 == 2
        assert 5 + 3 == 8
    
    def test_simple_subtraction(self):
        """Test basic subtraction"""
        assert 5 - 3 == 2
        assert 10 - 5 == 5
