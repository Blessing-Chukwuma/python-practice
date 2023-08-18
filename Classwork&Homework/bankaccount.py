currency = '$'
class Account:
    def __init__(self,owner=' ',balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
    def withdrawal(self,amount):
        if amount > self.balance:
            print('Insufficient Funds')
        #users account cant be below $20
        elif self.balance - amount < 20:
            print('Your account will be below limit, kindly withdraw less')
        else:
            self.balance-=amount
        return self.balance
        

acct1 = Account('Jose',100)

#this is to validate deposit input
while True:
    try:
        amount1 = int(input("How much do you want to deposit? "))
        break
    except ValueError:
        print("Please enter a valid integer.")

acct1.deposit(amount1)
print (f"{currency}{amount1} has been deposited, Your current Account balance is {currency}{acct1.balance}")

#this is to validate withdrawal input
while True:
    try:
        amount2 = int(input("How much do you want to withdraw? "))
        break
    except ValueError:
        print("Please enter a valid integer.")
acct1.withdrawal(amount2)

print (f"Current Account balance: {currency}{acct1.balance}")

