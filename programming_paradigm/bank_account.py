class BankAccount:
    def __init__(self):
        self.account_balance = 0 #Default value

    def deposit(self,amount):
        deposit = amount + self.account_balance
        print (f"{deposit}")

    def withdraw(self,amount):
        withdraw = self.account_balance - amount
        if withdraw <= self.account_balance:
            return True
        else:
            print("Insufficient funds")
            return False

    def display_balance(self):
        print("Your current balance is {self.display_balance}")
        

person1 = BankAccount()