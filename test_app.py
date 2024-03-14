# test_app_pytest.py
from app import app
import pytest


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    """Send a GET request to the Flask application and check the response."""
    response = client.get('/')
    assert response.data.decode('utf-8') == 'Hello, World!'
    assert response.status_code == 200
