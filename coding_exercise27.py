class BankAccount:
    def __init__(self, name, balance=0):
        self.account_holder_name = name
        self.account_balance = balance
    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited {amount}. New balance is {self.account_balance}")

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient balance")
        else:
            self.account_balance -= amount
    def __str__(self):
        return (f"Account holder name is: {self.account_holder_name}\nAccount balance is: {self.account_balance}")

obj=BankAccount("pradeeshna poluri", 1000)
print(obj) #prints the string representation of the object by calling the __str__ method

obj.deposit(500)
obj.withdraw(200)

print(obj) 
print()   

# print(obj.account_holder_name) #prints particular attribute of the class
# print(obj.account_balance)  #prints particular attribute of the class

obj.withdraw(1299) #attempt to withdraw more than the balance to test insufficient balance case

print() 
print(obj) 

#later checking the balance after the failed withdrawal attempt

obj.withdraw(300) #withdraw an amount to test the withdraw method
print(obj)