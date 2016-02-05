from app import app
import unittest

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        with open('cookies.cook','r') as f:
            cookies = f.read().split('%')
            cookies = [cookie.strip() for cookie in cookies]
        self.cookies = cookies


    def test_response(self):
        resp = self.app.get('/')
        assert resp.status_code == 200
        assert resp.data in self.cookies

if __name__ == '__main__':
    unittest.main()
