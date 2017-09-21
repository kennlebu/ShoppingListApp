from .shopping_list_item import ShoppingListItem
from datetime import datetime

class ShoppingList():
    """ Defines and holds data for a shopping list """

    def __init__(self, shopping_list_name, due_date, username):
        """ Constructor class """
        self.shopping_list_name = shopping_list_name
        self.due_date = due_date
        self.username = username
        self.date_created = datetime.now().strftime('%Y-%m-%d %H:%M.%S')
        self.items = []

    def add_item(self, item_name):
        """ Adds an item to the shopping list """

        # Check whether item already exists in the shopping list.
        # If it does, increament the quantity. Else, add it to the list.
        for item in self.items:
            if item.item_name == item_name:
                item.quantity += 1
                return "Item added"

        new_item = ShoppingListItem(self.shopping_list_name, item_name)
        self.items.append(new_item)

    def delete_item(self, item_name):
        """ Deletes an item from the shopping list """

        for item in self.items:
            if item.item_name == item_name:
                self.items.remove(item)
                return 'Item deleted'

        # Item not found
        return 'Item not found'
