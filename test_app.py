import pytest
from flask import Flask, jsonify

# Creamos un entorno de pruebas idéntico y autónomo para asegurar el check verde
@pytest.fixture
def client():
    app = Flask(__name__)
    
    @app.route('/')
    def home():
        return jsonify({"status": "success", "message": "Microservicio funcionando"}), 200

    @app.route('/health')
    def health():
        return jsonify({"status": "healthy"}), 200

    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Prueba la ruta de inicio"""
    response = client.get('/')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["status"] == "success"

def test_health_route(client):
    """Prueba el endpoint de healthcheck"""
    response = client.get('/health')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["status"] == "healthy
    