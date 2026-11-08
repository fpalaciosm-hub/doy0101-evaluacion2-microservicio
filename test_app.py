import pytest
from flask import Flask

# Creamos o importamos el cliente de pruebas apuntando directamente a tu estructura
@pytest.fixture
def client():
    # Importamos dinámicamente la configuración para el entorno de test
    from app import app as flask_app
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

def test_home_route(client):
    """Prueba que la ruta de inicio responda 200 OK y traiga el mensaje correcto"""
    response = client.get('/')
    assert response.status_code == 200
    json_data = response.get_json()
    assert "status" in json_data
    assert json_data["status"] == "success"

def test_health_route(client):
    """Prueba el endpoint de healthcheck para el entorno cloud"""
    response = client.get('/health')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["status"] == "healthy"
