from database import Database

class User:
    def __init__(self, user_type):
        self._balance = 0
        self._user_type = user_type
        self._db = Database()

    def view_balance(self):
        return self._balance

    def _update_balance(self, amount):
        self._balance += amount
        return self._balance
