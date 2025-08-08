'''
Question 4: Hospital Billing System (Single Inheritance)
    Create a base class Patient with attributes like patient ID and name.

    Create a derived class Billing that adds:
        • Room charges
        • Doctor fees
        • Medicine cost
    Add a constant for GST (e.g., GST_RATE = 0.18) and a method to calculate the total
    bill using local and instance variables.

    Use super() to initialize the parent class and static method to display hospital name.

'''
GST = 0.18

class Patient:
    def __init__(self, Patient_ID, name):
        self.Patient_ID = Patient_ID
        self.name = name
    
class Billing(Patient):
    def __init__(self, Patient_ID, name, room_charge, doc_fee, med_cost):
        super().__init__(Patient_ID, name)
        self.room_charge = room_charge
        self.doc_fee = doc_fee
        self.med_cost = med_cost
    def total_bill(self):
        global GST
        bill = (self.room_charge + self.doc_fee + self.med_cost)*GST + (self.room_charge + self.doc_fee + self.med_cost)
        print("TOTAL BILL: "+str(bill))
    
    @staticmethod
    def display_hospital_name(name):
        print("Hospital Name: "+name)

bl = Billing("PAT101", "Samuel", 100, 100, 300)
bl.total_bill()
Billing.display_hospital_name("Jeremy Dental Hospital")