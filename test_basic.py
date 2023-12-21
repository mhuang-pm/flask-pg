import unittest
from app import app

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_with_bypass(self):
        with self.app.test_request_context(headers={}):
            response = self.client.get('/endpoint1')
            self.assertEqual(response.status_code, 200)

    def test_missing_token(self):
        with self.app.test_request_context(headers={}):
            response = self.client.get('/endpoint2')
            self.assertEqual(response.status_code, 403)

    def test_with_token(self):
        with self.app.test_request_context(headers={}):
            # we can mock the is valid part
            response = self.client.get('/endpoint2', headers={"Authorization": "valid_token"})
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
