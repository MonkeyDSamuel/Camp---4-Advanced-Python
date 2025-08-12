from models.Interest import Interest
class MenuDriven:
    # def __init__(self):
    #     self.accounts = []
    # def show_menu():
    #     print(f'''
    #             1. Add account details
    #             2. 

    #             ''')
    def run(self):
        accounts = []
        while True:
            acc_type = input("Enter the account type(savings/fixed): ")
            principal = float(input("Enter the principal amount: "))
            duration = float(input("Enter the duration in (years): "))

            try :
                account = Interest(principal,duration, acc_type)
                accounts.append(account)
            except ValueError as e:
                print(e)
                continue
            choice = input("Do you want to add another account? (y/n)").lower()
            if choice  != "y":
                break
        print("\n------------Account--Details------------")
        for acc in accounts:
            print(acc)