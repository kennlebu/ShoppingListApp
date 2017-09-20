import unittest
from app.shopping_list import ShoppingList
from app.user import User

class ShoppingListTests(unittest.TestCase):
    """ Defines tests for the shopping list """

    def test_shopping_item_creation(self):
        """ Tests whether a shopping list is created """

        user = User('kennlebu', 'password', 'Kenneth', 'Lebu')
        user.create_shopping_list('Sunday shopping', '15/10/2017', user.username)
        user.shopping_lists[0].add_item('Bacon')

        self.assertEqual(len(user.shopping_lists[0].shopping_list_items), 1,
                         msg='There should be one shopping list item')

    def test_delete_shopping_list_item(self):
        """ Tests whether a shopping list item is deleted """

        user = User('kennlebu', 'password', 'Kenneth', 'Lebu')
        user.shopping_lists[0].delete_item('Bacon')

        self.assertEqual(len(user.shopping_lists[0].shopping_list_items), 0,
                         msg='There should be no shopping list item')

if __name__ == '__main__':
    unittest.main()
