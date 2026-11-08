import pytest
from flask import Flask, jsonify

@pytest.fixture
def client():
    app = Flask(__name__)
    
    @app.route('/')
    def home():
        return jsonify({"status": "success"}), 200

    @app.route('/health')
    def health():
        return jsonify({"status": "healthy"}), 200

    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200

def test_health_route(client):
    response = client.get('/health')
    assert response.status_code == 200
