'''
Question 2: Online Shopping System (Hierarchical Inheritance)
    Build an online shopping system.

    Create a base class User with instance variables: username, email.

    Derive two classes: Customer and Seller.
        • Customer should include cart and Wishlist features.
        • Seller should include product listings and ratings.
    Use:
        • Static variables for total users/customers.
        • Global variables to maintain platform-wide sales count.
        • Local variables inside methods to perform calculations.
        Demonstrate all types of variables clearly in a method.

'''
Sales = 0
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
class Customer(User):
    def __init__(self, username, email):
        super().__init__(username, email)
        self.cart_list=[]
    def wishlist(self,product_name):
        self.wish_product = product_name
    def cart(self,product_name):
        global Sales
        self.cart_list.append(product_name)
        Sales += 1
        print("Sale completed")

class Seller(User):
    def __init__(self, username, email):
        super().__init__(username, email)
        self.products={}
    def product_listing(self,product_name, rating):
        self.products[product_name] = rating

seller1 = Seller("Samuel","samuelcsofficial@gmail.com")
customer1 = Customer("Breesha","breeshajeno@gmail.com")

seller1.product_listing("Kelloggs Corn flakes",5)

customer1.wishlist("Kelloggs Corn flakes")

check = customer1.wish_product
if check in seller1.products:
    customer1.cart(check)
else:
    print("Product not available")

print(f"Total number of sales: {Sales}")