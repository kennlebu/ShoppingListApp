import unittest
import app.views
from app.user import User
from flask import url_for

class ViewsTests(unittest.TestCase):
    """ Tests for the views """

    view = app.views

    def test_signup(self):
        """ Tests whether signup page loads """

        with app.app.test_client() as client:
            response = client.get('/signup')
            self.assertEqual(response.status_code, 200)

    def test_login(self):
        """ Tests whether login page is loaded """

        with app.app.test_client() as client:
            response = client.get('/login')
            self.assertEqual(response.status_code, 200)

    def test_index(self):
        """ Tests whether index page loads """

        with app.app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 302) # Redirects coz user isnt logged in

if __name__ == '__main__':
    unittest.main()
