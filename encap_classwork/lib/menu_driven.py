from models.customer import Customer
class MenuDriven:

    def __init__(self):
        self.customers = []

    def show_menu(self):
        print('''
                1. Create Customer
                2. List Customer
                3. Update Amount
                4. Exit
            ''')
    
    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                accno = int(input("Enter the Account Number: "))
                name = input("Enter the name of the customer: ")
                amount = float(input("Enter the amount: "))
                customer = Customer(accno,name,amount)
                self.customers.append(customer)
            elif choice == "2":
                for id,cust in enumerate(self.customers, start=1):
                    print(f"{id}")
                    cust.display_customer_details()
            elif choice == "3":
                accno = int(input("Enter the account number to which the amount is to be updated"))
                flag = False
                for cust in self.customers:
                    if cust.get_account == accno:
                        new_amount = float(input("Enter the new amount to be updated: "))
                        cust.set_amount = new_amount
                        print("Balance updated successfully")
                        flag = True
                        break
                if not flag:
                    print("Customer not found!!!")
            elif choice == "4":
                print("EXITING....")
                break
            else:
                print("Invalid choice...")