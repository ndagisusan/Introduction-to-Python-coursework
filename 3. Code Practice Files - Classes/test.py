# Real world examle - Financial setting: Tracking different people's bank accounts 
class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

jane = BankAccount()
john = BankAccount()

print("Jane's balance: ", jane.deposit(100))
print("Jane's new balance: ",jane.withdraw(10))

print("John's balance: ", john.deposit(2500))
print("John's new balance: ", john.withdraw(1000))


#Test example - What is the expected output?
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print(a.f(), b.f())
print(a.g(), b.g())

# Checking data type
print(type(A))
print(type(a))