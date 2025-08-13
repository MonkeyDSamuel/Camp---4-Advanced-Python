from abc import ABC, abstractmethod

class Order:    #concrete class
    'demo for data abstraction'
    '''
    To create an abstract class:
            --from abc import ABC, abstractmethod
            --@abstractmethod
            --you can't create objects of an abstract class

    '''
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"
        
    def add_item(self,name:str,quantity:int,price:float)->None:
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

#create an Abstract class
#ABC: short for Abstract Based Class
#Classes that inherit from ABC can define abstract methods
#Abstract methods must be overriden in child classes

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self,order):
        pass

#create concrete class
class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self,security_code:str):
        self.security_code = security_code
    def pay(self,order):
        print("Processing debit payment type...")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self,security_code:str):
        self.security_code = security_code
    def pay(self,order):
        print("Processing credit payment type...")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

#create object
order = Order()
order.add_item("keyboard",1,5000.0)
order.add_item("SSD", 2,2500)
order.add_item("USB cable",3,200)

#create object of concrete subclass
payment = DebitPaymentProcessor("Samuel123")
payment.pay(order)
print(order.status)

#create object of abstract class...
# pay = PaymentProcessor()