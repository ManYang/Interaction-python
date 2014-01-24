
n = 1001
numbers=[]

results=[]
def num(n):
    for x in range(2,n):
        global numbers
        numbers.append(x)
    return numbers

def res():
    global results
    while len(numbers)!=0:
        x=numbers.pop(0)
        results.append(x)
        for y in numbers:
            if y%x==0:
                numbers.remove(y)

#num(1000)
#res()
#print len(results)


def year():
    slow=1000 
    fast=1
    n=0
    while True:
        slow*=2
        slow*=0.6
        fast*=2
        fast*=0.7
        if fast>slow:
            break
        n+=1
    print str(slow)+" " +str(fast) + " "+str(n)
    
#year()  

#quiz 6a
class OverLoad:
    def __init__(self,c):
        pass
    def __init__(self, another,d):
        pass

#a=OverLoad(1)
#b=OverLoad(1,1) 

class BankAccount:
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.balance= initial_balance
        self.penalty=0
        
    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.balance+=amount
    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        self.balance-=amount
        if self.balance<0:
            self.penalty+=5
            self.balance-=5
            
    def get_balance(self):
        """Returns the current balance in the account."""
        return self.balance
    
    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.penalty

account1 = BankAccount(20)
account1.deposit(10)
account2 = BankAccount(10)
account2.deposit(10)
account2.withdraw(50)
account1.withdraw(15)
account1.withdraw(10)
account2.deposit(30)
account2.withdraw(15)
account1.deposit(5)
account1.withdraw(10)
account2.withdraw(10)
account2.deposit(25)
account2.withdraw(15)
account1.deposit(10)
account1.withdraw(50)
account2.deposit(25)
account2.deposit(25)
account1.deposit(30)
account2.deposit(10)
account1.withdraw(15)
account2.withdraw(10)
account1.withdraw(10)
account2.deposit(15)
account2.deposit(10)
account2.withdraw(15)
account1.deposit(15)
account1.withdraw(20)
account2.withdraw(10)
account2.deposit(5)
account2.withdraw(10)
account1.deposit(10)
account1.deposit(20)
account2.withdraw(10)
account2.deposit(5)
account1.withdraw(15)
account1.withdraw(20)
account1.deposit(5)
account2.deposit(10)
account2.deposit(15)
account2.deposit(20)
account1.withdraw(15)
account2.deposit(10)
account1.deposit(25)
account1.deposit(15)
account1.deposit(10)
account1.withdraw(10)
account1.deposit(10)
account2.deposit(20)
account2.withdraw(15)
account1.withdraw(20)
account1.deposit(5)
account1.deposit(10)
account2.withdraw(20)
print account1.get_balance(), account1.get_fees(), account2.get_balance(), account2.get_fees()