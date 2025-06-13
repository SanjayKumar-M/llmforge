class Model:
    def __init__(self,name,params):
        self.name = name
        self.params = params
    def announce(self):
        print(f"We are happy to announce our new model {self.name} with {self.params} parameters")
        
        
deepseek = Model(name="deepseek",params="7B")
deepseek.announce()


"""
    Python doesn't have strict access modifiers like private, protected, and public as in some other languages. Instead, it uses naming conventions to indicate the intended visibility of attributes and methods:

Public: Attributes and methods with no prefix are considered public and can be accessed from anywhere.
Protected: Attributes and methods with a single underscore prefix (_) are considered protected. They are intended for use within the class and its subclasses, but can still be accessed from outside the class (though it's discouraged).
Private: Attributes and methods with a double underscore prefix (__) are considered private. Python uses name mangling to make it more difficult (but not impossible) to access them from outside the class.
"""
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public attribute
        self._balance = balance            # Protected attribute (convention)
        self.__transaction_history = []   # Private attribute (name mangling)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.__transaction_history.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self.__transaction_history.append(f"Withdrew: {amount}")
        else:
            return "Insufficient funds or invalid amount."

    def get_balance(self):
        return self._balance

    def __get_transaction_history(self): # Private method
        return self.__transaction_history

my_account = BankAccount("1234567890", 1000)
print(my_account.account_number) # 1234567890 (Public - accessible)
print(my_account._balance) # 1000 (Protected - accessible, but discouraged)

my_account.deposit(500)
print(my_account.get_balance()) # 1500

# print(my_account.__transaction_history) # AttributeError: 'BankAccount' object has no attribute '__transaction_history'
# print(my_account.__get_transaction_history()) # AttributeError: 'BankAccount' object has no attribute '__get_transaction_history'

print(my_account._BankAccount__transaction_history) # ['Deposited: 500'] (Name mangling - technically accessible, but strongly discouraged)


# getters and setters
class BankAccount:
    def __init__(self, balance):
        # Internal variable to hold the balance
        self._balance = balance

    @property
    def balance(self):
        """
        Getter method: Allows you to access the balance like a normal variable,
        but it's actually calling this method.
        """
        return self._balance

    @balance.setter
    def balance(self, value):
        """
        Setter method: Controls how the balance is updated.
        Here, we prevent setting a negative balance.
        """
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value


# === Usage ===

account = BankAccount(100)     # Creating account with $100
print(account.balance)         # Accessing balance (calls the getter)

account.balance = 200          # Updating balance to $200 (calls the setter)
print(account.balance)         # $200

# account.balance = -50        # ❌ This will raise ValueError




