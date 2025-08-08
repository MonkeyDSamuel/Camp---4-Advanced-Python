'''
Question 3: Vehicle Rental System (Multiple Inheritance)
    Design a vehicle rental system.

    Create two parent classes:
        • Owner with owner name and contact.
        • Vehicle with vehicle type, model, and registration number.

    Create a RentalInfo class that inherits from both and manages rental rates and
    duration.

    Demonstrate:
        • How super() works in multiple inheritance.
        • How Python resolves method conflicts using MRO (Method Resolution Order).

    Add a method with the same name in both base classes and show how to
    access each one explicitly.

'''

class Owner:
    def __init__(self, owner_name, contact):
        self.owner_name = owner_name
        self.contact = contact
    def display(self):
        print(f"Owner Name: {self.owner_name}\nContact: {self.contact}")

class Vehicle:
    def __init__(self, type, model, reg_no):
        self.type = type
        self.model = model
        self.reg_no = reg_no
    def display(self):
        print(f"Car Type: {self.type} | Car Model: {self.model} | Registration Number: {self.reg_no}")
    
class RentalInfo(Owner,Vehicle):
    def __init__(self, owner_name, contact, rent, duration):
        super().__init__(owner_name, contact)
        self.rent = rent
        self.duration = duration

rt = RentalInfo("Samuel",9078889056,2000,1)
rt.display()    #Only accesses diplay() method of first base class when there are methods of the same name in both base classes