class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = 0
        self.__balance = 0.0
        self.set_account_number(account_number)
        self.set_balance(balance)
        
    def set_balance(self, balance):
        if balance < 0:
            print("The balance must not be a negative number.")
        else:
            self.__balance = float(balance)
            
    def set_account_number(self, account_number):
        self.__account_number = int(account_number)

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number


a1 = BankAccount(12345, 1000)
print("Account 1")
print("Account Number:", a1.get_account_number())
print("Balance:", a1.get_balance())
print()

print("Update balance to -100")
a1.set_balance(-100)

print("Account Number:", a1.get_account_number())
print("Balance:", a1.get_balance())