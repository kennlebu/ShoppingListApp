from app.shopping_list import ShoppingList

class User:
    """ Holds data related to a user of the application """

    def __init__(self, username, password, firstname, lastname):
        """ Constructor initializes instance variables for user """
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.shopping_lists = []

    def create_shopping_list(self, shopping_list_name, due_date):
        """ Creates a shopping list for the user """

        self.shopping_lists.append(ShoppingList(shopping_list_name, due_date, self.username))

    def delete_shopping_list(self, shopping_list_name):
        """ Deletes a shopping list """

        for shopping_list in self.shopping_lists:
            if shopping_list.shopping_list_name == shopping_list_name:
                self.shopping_lists.remove(shopping_list)
                return 'Item deleted'

        # Item not found
        return 'Shopping list not found'
