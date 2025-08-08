'''
Assignment 4: Billing System for International Customers
    Scenario:
    You're a programmer at Simple Solutions, a US-based software firm. You’re
    building billing software for EasyaPay Telecommunications to handle international
    customer billing.
    Instructions:
        Create a class BillingSystem.
        In the constructor, accept and initialize:
            country_name
            language
            customer_id
            billing_date
            amount_outstanding (use float)
        Create a method display_details() that prints all the billing info.
        Create two objects, one for a customer in the US and one for a customer in Japan.
        Call the display_details() method for both

'''

class BillingSystem:
    def __init__(self, country_name, language, customer_id, billing_date, amount_outstanding):
        self.country_name = country_name
        self.language = language
        self.customer_id = customer_id
        self.billing_date = billing_date
        self.amount_outstanding = amount_outstanding
    
    def __str__(self):
        return f"Country: {self.country_name}\nLanguage: {self.language}\nCustomer_ID: {self.customer_id}\nBillingDate: {self.billing_date}\nAmount_Outstanding: {float(self.amount_outstanding)}"

us_user = BillingSystem('USA','English','USA1','07/08/2025', 5000)
jp_user = BillingSystem('JAPAN','Japanese','JP1','07/07/2025',4000)

print(us_user)
print('\n\n')
print(jp_user)