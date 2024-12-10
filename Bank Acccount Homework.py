# Empty Lists to Store Multiple Values
deposits_list = []
withdraws_list = []
transfers_list = []
balances = []
second_balances = []
# Default Values
default_balance = 0
# Choosing the Account Number
acc_number = int(input("Do you want to use Account Number 1 or 2: "))
# Running a While Loop to Keep the Program Running
x = 0
while x == 0:
# Naming the Class
    class BankAccounts:
# Initiating Some Variables
        def __init__(self):
            self.deposit = None
            self.withdraw = None
            self.transfer = None
            
# Function to Get the Entries and Save them in the Empty Lists
        def get_dwt_and_save_entries(self):
            deposit_withdraw_or_transfer = input("Do you want to deposit, withdraw, transfer(d/w/t): ").lower()
            if deposit_withdraw_or_transfer == "d":
                deposit = int(input("Enter your deposit amount: "))
                deposits_list.append(deposit)
            if deposit_withdraw_or_transfer == "w":
                withdraw = int(input("Enter your withdraw amount: "))
                withdraws_list.append(withdraw)
            if deposit_withdraw_or_transfer == "t":
                if acc_number == 1:
                    transfer = int(input("How much do you want to tranfer to AccountNumber2: "))
                    transfers_list.append(transfer)
                if acc_number == 2:
                    transfer = int(input("How much do you want to tranfer to AccountNumber1: "))
                    transfers_list.append(transfer)                    
            if deposit_withdraw_or_transfer != "d" and deposit_withdraw_or_transfer != "w" and deposit_withdraw_or_transfer != "t": 
                print("Sorry, this option is not available.")

# Function to get the Balance of the Chosen Account
        def calculate_balance_main(self):
            default_balance = 0
            for deposits_done in deposits_list:
                default_balance += deposits_done
            for withdraws_done in withdraws_list:
                default_balance -= withdraws_done
            for transfers_done in transfers_list:
                default_balance -= transfers_done
            balances.append(default_balance)

# Adding the Transfer the the Second Account
        def add_transfer_to_second_account(self):
            second_account_balance = 0
            for transactions in transfers_list:
                second_account_balance += transactions
                second_balances.append(second_account_balance)

    continue_or_not = (input("Do you want to continue(y/n): ")).lower()
    if continue_or_not == "y":
        pass
# If they don't want to continue it will return the deposits, withdraws, and, transfers along with the balances for both accounts.
    else:
        print(f"Deposits: {deposits_list}")
        print(f"Withdraws: {withdraws_list}")
        print(f"Transfers: {transfers_list}")
        print(f"BALANCE OF ACCOUNT NUMBER 1: {balances[-1]}")
        print(f"BALANCE OF ACCOUNT NUMBER 2: {second_balances[-1]}")
# Breakinig the Code
        break
# Objects
    Object1 = BankAccounts()
    Object1.get_dwt_and_save_entries()
    Object1.calculate_balance_main()
    Object1.add_transfer_to_second_account()

