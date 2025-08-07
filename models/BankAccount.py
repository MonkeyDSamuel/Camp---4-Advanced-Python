class BankAccount:
    'class to handle deposit and withdraw'
    #class variable
    bank_name = 'SBI'

    #constructor
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    #instance method
    def deposit(self, amount):
        self.balance+=amount
        print(f'{amount}deposited. New balance: {self.balance}')
    
    #class method
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
    
    #static method
    @staticmethod
    def calculate_interest(balance, rate):
        return (balance*rate)/100
    
    #override the inbuilt str method to display the object
    def __str__(self):
        return f"Account holder: {self.account_holder} | Balance: {self.balance} | Bank: {self.bank_name}"

acc1 = BankAccount("Anu",1000)
print(acc1) #str method is invoked

#use static method
print(BankAccount.calculate_interest(200,5))

#use deposit method
acc1.deposit(1000)

#use class method to change the bank name permamnently after calling
BankAccount.change_bank_name('SIB')

