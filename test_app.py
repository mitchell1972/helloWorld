import unittest
from app import app

class HelloWorldTestCase(unittest.TestCase):

    def setUp(self):
        # Set up the app to run in testing mode
        app.testing = True
        self.app = app.test_client()

    def test_hello_world(self):
        # Send a GET request to the Flask application
        response = self.app.get('/')
        # Check if the response data matches "Hello, World!"
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World!')
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
