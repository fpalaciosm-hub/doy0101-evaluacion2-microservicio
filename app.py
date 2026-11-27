from flask import Flask, jsonify
from prometheus_client import make_wsgi_app, Counter
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import time

app = Flask(__name__)

# Métrica personalizada para contar las solicitudes (Opcional para ganar puntos extra en IE3)
REQUEST_COUNT = Counter('app_requests_total', 'Total de solicitudes recibidas', ['method', 'endpoint', 'http_status'])

@app.route('/')
def home():
    REQUEST_COUNT.labels(method='GET', endpoint='/', http_status='200').inc()
    return jsonify({
        "status": "Microservicio DevOps en línea",
        "timestamp": int(time.time()),
        "version": "EP3"
    })

@app.route('/api/v1/data')
def get_data():
    REQUEST_COUNT.labels(method='GET', endpoint='/api/v1/data', http_status='200').inc()
    return jsonify({
        "users_active": 42,
        "environment": "production-simulated"
    })

# Middleware obligatorio para mapear y exponer la ruta /metrics para Prometheus
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
