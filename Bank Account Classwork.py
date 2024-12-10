class BankAccounts:
    def __init__(self, account_holder, account_number, balance=0.0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def Deposit(self):
        amount = int(input("How much do you want to deposit?: "))
        if amount > 0:
            self.balance += amount
            print(f"Dear, {self.account_holder} you have Deposited: {self.balance} into the account number {self.account_number}.")

        else:
            print("Deposited amount must be positive.")
            
    def Withdraw(self):
        amount = int(input("How much do you want to withdraw?: "))
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Dear, {self.account_holder} you have Withdrawn: ${amount} from the account number {self.account_number} remaining balance will be ${self.balance}.")
            else:
                print(f"Insufficient Balance your remaining balance is {self.balance}")
        else:
            print("Withdrawal amount has to be more than zero.")
    
    def Transfer(self):
        amount = int(input("How much do you want to transfer?: "))
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Dear, {self.account_holder} you have Transferred: ${amount} from the account number {self.account_number} remaining balance will be ${self.balance}.")
            else:
                print(f"Insufficient Balance, your remaining balance is {self.balance}")
        else:
            print("Transfer amount must be more than zero.")
    
    def Balance(self):
        return (f"The balance of your account is {self.balance} ")
    

BankAccount1 = BankAccounts("Iqra Chaudhary", 1234, 500.00)
BankAccount2 = BankAccounts("Hira Noureen", 5678, 1000.00)
print(BankAccount1.Balance())
print(BankAccount2.Balance())
BankAccount1.Deposit()
BankAccount2.Withdraw()
BankAccount1.Transfer()
print(BankAccount1.Balance())
print(BankAccount2.Balance())
