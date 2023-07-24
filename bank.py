class Account:
    """
    The Account class represents a bank account with basics functionalities
    Atrribute: 
    - `account_id` which uniquely identifies each customer's account in our system
    - `account_name1 which identifies the customer`s name 
    - `balance`, representing how many money we have on hand for this particular account
    Methods:
    1- Deposit To Bank
    2- Bank Withdrawals
    3- Check Current Balances
    
    """
    def __init__(self, account_id, account_name,balance):
        self.account_id = account_id
        self.account_name =  account_name
        self.balance = balance
    def deposit_to_bank(self, amount):
        """
        Deposit the specified amount
        """
        self.balance += amount
    def bank_withdrawal(self, amount):
        """
        withdrew a certain amount
        cannot withdraw if the amount is less than the specified amount
        """
        print("\nYou can withdraw from this Bank only.")
        if amount <= self.balance:
            self.balance -= amount
        else:
            return "Insufficient Fund!"
    def balance_inquiry(self):
        """
        shows the amount in the user`s bank account
        """
        #print f"Your current Balance is {str(self.balance)}."
        print(f"Your current balnce is {str(self.balance)}")
account_id = int(input("Enter your acount number: "))
account_name = str(input("Enter your account name: "))
account_balance = 0.0
account = Account(account_name, account_id, account_balance)
deposit_amount = float(input("Ente the amount you want to deposit: "))
account.deposit_to_bank(deposit_amount)
#check balances after depositeing
current_balace = round((float)(account.balance),2)
withdraw_amount = float(input("Enter the amount that you want to withdraw: "))
account.bank_withdrawal(withdraw_amount)
account.balance_inquiry()