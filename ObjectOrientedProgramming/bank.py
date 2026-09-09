class Bank:

    acc_number:int
    balance:float
    ac_type:str
    customer_name:str
    amount:float

    def __init__(self,acc_number,balance,ac_type,customer_name):

        self.acc_number=acc_number
        self.balance=balance
        self.ac_type=ac_type
        self.customer_name=customer_name
        

    def deposit(self,amount):

        self.balance = self.balance + amount
        print(f"your {self.acc_number} is credicted with {amount} ,available balance is {self.balance}")

    def withdraw(self,amount):

        if self.balance<amount:

            raise Exception(".........insufficient balance.........")

        else:

            self.balance = self.balance-amount

            print(f"your {self.acc_number} is debited with {amount} ,available balance is {self.balance}")


    def get_balance(self):

        print("Available Balance is ",self.balance)
        
action1=Bank(1234567,24000,"savings","Ajna")
action1.deposit(2000)
action1.withdraw(100)
action1.get_balance()

