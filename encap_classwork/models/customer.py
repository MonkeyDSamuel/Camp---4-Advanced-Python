class Customer:
    'customer class to add accountno, name, amount'
    def __init__(self, account_no = None, cust_name = None, amount = None):
        self.__account_no = account_no
        self.__cust_name = cust_name
        self.__amount = amount
    
    @property
    def get_account(self):
        return self.__account_no
    
    @get_account.setter
    def set_account_no(self,value):
        if not isinstance(value, int):
            raise ValueError("Account number must be of integer type")
        self.__account_no = value
    
    @property
    def get_name(self):
        return self.__cust_name
    
    @get_name.setter
    def set_name(self, name):
        if not isinstance(name,str):
            raise ValueError("Customer name must be of string type...")
        elif not name.strip():
            raise ValueError("The Customer name can't be empty")
        self.__cust_name = name
    
    @property
    def get_amount(self):
        return self.__amount
    
    @get_amount.setter
    def set_amount(self,amount):
        if not isinstance(amount,float):
            raise ValueError("The amount must be in float type")
        elif amount<0:
            raise ValueError("The amount can't be negative")
        self.__amount = amount
    
    def display_customer_details(self):
        print(f"""
                Account Number: {self.__account_no}
                Customer Name: {self.__cust_name}
                Amount: {self.__amount}
                """)

# name = "Samuel"
# age = 23
# Date = date.today()

# print(f"""Name: {name}
# Age: {age}
# Date: {Date}""")