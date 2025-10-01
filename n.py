import unittest
import json
from app import app

class AuthServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_register(self):
        response = self.app.post('/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        self.app.post('/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        response = self.app.post('/login', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertIn('token', data)

    def test_protected_route_without_token(self):
        response = self.app.get('/protected')
        self.assertEqual(response.status_code, 403)

if __name__ == '__main__':
    unittest.main()