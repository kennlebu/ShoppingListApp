import unittest
from app.user import User

class UserTests(unittest.TestCase):
    """ Tests for the user class """

    def test_user_creation(self):
        """ Tests whether a user is created and stored successfully """

        user = User('kennlebu', 'password', 'Kenneth', 'Lebu')

        assert user
        self.assertEqual(user.username, 'kennlebu', msg='Username should be kennlebu')
        self.assertEqual(user.lastname, 'Lebu', msg='Lastname should be Lebu')

    def test_create_shopping_list(self):
        """ Tests whether a shopping list is created successfully """

        user = User('kennlebu', 'password', 'Kenneth', 'Lebu')
        user.create_shopping_list('Sunday shopping', '15/10/2017', user.username)

        self.assertEqual(len(user.shopping_lists), 1, msg="There should be one shopping list created")
        self.assertEqual(user.shopping_lists[0].username, 'kennlebu',
                         msg='User of the shopping list should be kennlebu')

    def test_delete_shopping_list(self):
        """ Tests whether a shopping list is deleted successfully """

        user = User('kennlebu', 'password', 'Kenneth', 'Lebu')
        user.create_shopping_list('Sunday shopping', '15/10/2017', user.username)
        self.assertEqual(len(user.shopping_lists), 1, msg="There should be one shopping list created")

        # Deleting a shopping list that does not exist
        user.delete_shopping_list('Monday shopping')
        self.assertEqual(user.delete_shopping_list('Monday shopping'), 'No such shopping list',
                         msg="There should not be a shopping list called Monday shopping")

        user.delete_shopping_list('Sunday shopping')
        self.assertEqual(len(user.shopping_lists), 0, msg="There should not be any shopping lists")

if __name__ == '__main__':
    unittest.main()
