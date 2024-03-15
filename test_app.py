# test_app.py
import pytest
from app import app, db, HelloWorld

@pytest.fixture(scope='module')
def test_client():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True

    # Establish an application context before running the tests
    ctx = app.app_context()
    ctx.push()

    db.create_all()

    # Add test data
    hello_message = HelloWorld(content='Hello, World!')
    db.session.add(hello_message)
    db.session.commit()

    yield app.test_client()  # this is where the testing happens!

    db.session.remove()
    db.drop_all()
    ctx.pop()

def test_hello(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data
