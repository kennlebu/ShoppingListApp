class ShoppingListItem():
    """ A model to hold data about a shopping list item """

    def __init__(self, shopping_list_name, item_name):
        """ Constructor takes shopping_list_name and the item
        name as parameters """
        self.shopping_list_name = shopping_list_name
        self.bought = False
        self.item_name = item_name
        self.quantity = 1

    def mark_item_as_bought(self):
        """ Marks an item as bought """
        self.bought = True

    def mark_item_as_not_bought(self):
        """ Marks an item as not yet bought """
        self.bought = False
