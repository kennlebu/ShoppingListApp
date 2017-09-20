import unittest
from app.shopping_list_item import ShoppingListItem
from app.user import User

class ShoppingListItemTests(unittest.TestCase):
    """ Defines tests for the shopping list item class """

    def test_create_item(self):
        """ Tests whether an item is created """

        user = User('kennlebu', 'password', 'Kenneth', 'Lebu')
        user.create_shopping_list('Sunday shopping', '15/10/2017', user.username)
        user.shopping_lists[0].add_item('Bacon')
        user.shopping_lists[0].add_item('Soap')
        item = user.shopping_lists[0].items[0]

        self.assertEqual(len(user.shopping_lists[0].items), 2, msg='There should be two items')
        self.assertEqual(item.item_name, 'Bacon', msg='Item name should be Bacon')
        
        # Test quantity
        user.shopping_lists[0].add_item('Soap')
        item = user.shopping_lists[0].items[1]
        self.assertEqual(item.quantity, 2, msg='Quantity should be 2')

    def test_mark_item_bought(self):
        """ Tests whether an item is marked as bought """

        user = User('kennlebu', 'password', 'Kenneth', 'Lebu')
        user.create_shopping_list('Sunday shopping', '15/10/2017', user.username)
        user.shopping_lists[0].add_item('Bacon')
        item = user.shopping_lists[0].items[0]

        assert(not item.bought)
        item.mark_item_as_bought()
        assert(item.bought)

    def test_mark_item_not_bought(self):
        """ Tests whether an item is marked as not bought """

        user = User('kennlebu', 'password', 'Kenneth', 'Lebu')
        user.create_shopping_list('Sunday shopping', '15/10/2017', user.username)
        user.shopping_lists[0].add_item('Bacon')
        item = user.shopping_lists[0].items[0]

        assert(not item.bought)
        item.mark_item_as_bought()
        assert(item.bought)
        item.mark_item_as_not_bought()
        assert(not item.bought)
