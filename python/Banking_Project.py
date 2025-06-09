"""
deposit :
    min deposit amount should be 100
    amount should be multiples of 100
    max Deposit amount 50k
Withdraw :
    min WithDraw Amount should be 100
    amount should be multiples of 100
    withdraw amount should be less than account balance
    need to maintain min 500 balance
    max Transaction amount should be 50k
    max Number of Transactions 3 only
"""


class Bank:
    account_balance = 10000
    withdraw_count = 1
    print("Welcome to ABC Bank")

    def validate(self, count):
        pin = int(input("Enter pin : "))
        count = count + 1
        if pin == 1234:
            obj.Options()
        else:
            print("Invalid PIN number. please try again")
            if count < 3:
                obj.validate(count)
            else:
                print("Card Blocked for the day. Please Try again tomorrow")

    def Options(self):
        while True:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Balance Enquiry")
            print("0. Exit")
            num = int(input("Choose your option"))
            if num == 1:
                self.deposit()
            elif num == 2:
                self.withdraw()
            elif num == 3:
                self.balance()
            elif num == 0:
                print("Thank you for using ABC Bank")
                exit()
            else:
                print("Invalid option")

    def deposit(self):
        print("Welcome to Deposit")
        deposit_amount = int(input("Enter the amount to be deposited : "))
        if deposit_amount < 100:
            print("Minimum Deposit amount should be 100 ")
        elif deposit_amount % 100 != 0:
            print("Deposit amount should be multiples of 100")
        elif deposit_amount > 50000:
            print("Maximum Deposit amount is 50000")
        else:
            print("Amount Deposited")
            self.account_balance = self.account_balance + deposit_amount

    def withdraw(self):
        print("Welcome to Withdraw")
        if self.withdraw_count > 3:
            print("Limit exceeded. Max number of transactions 3 only per day")
        else:
            withdraw_amount = int(input("Enter the amount to be withdrawn : "))
            if withdraw_amount < 100:
                print("Minimum Withdraw amount should be 100 ")
            elif withdraw_amount % 100 != 0:
                print("Withdraw amount should be multiples of 100")
            elif withdraw_amount > self.account_balance:
                print("Withdraw amount should be less than account balance")
            elif self.account_balance - withdraw_amount < 500:
                print("Need to maintain minimum 500 account balance")
            elif withdraw_amount > 20000:
                print("Withdraw amount should be 20000")
            else:
                print("Amount Debited")
                print("Please collect the amount")
                self.account_balance = self.account_balance - withdraw_amount
                self.withdraw_count = self.withdraw_count + 1

    def balance(self):
        print("Balance " + str(self.account_balance))


obj = Bank()
obj.validate(0)
