'''
Assignment 5: Hospital Management System
    Scenario:
    You are a developer building a simple Hospital Management System. The system
    will manage patients' details, calculate bills, and maintain hospital-wide data.
        Task:Create a class called Patient.
            Requirements:
                1. Instance Variables (set inside the constructor):
                    • patient_id
                    • name
                    • age
                    • admitted_days
                    • daily_charge
                2. Class Variable:
                    • hospital_name (shared by all patients, e.g., "CityCare Hospital")
                3. Constructor (__init__):
                    • Initializes all instance variables with values passed at object creation.
                4. Instance Method:
                    • calculate_bill(): Returns total bill = admitted_days * daily_charge.
                5. Class Method:
                    • change_hospital_name(cls, new_name): Changes the hospital name for all
                    patients.
                6. Static Method:
                    • is_senior(age): Returns True if age >= 60, else False.
                7. __str__() Method:
                    • Returns a readable string showing patient details.

'''

class Patient:

    hospital_name = 'CityCare Hospital'
    def __init__(self,patient_id, name, age, admitted_days, daily_charge):
        self.patient_id = patient_id,
        self.name = name
        self.age = age
        self.admitted_days = admitted_days
        self.daily_charge = daily_charge
    def calculate_bill(self):
        total_bill = self.admitted_days*self.daily_charge
        return total_bill
    
    @classmethod
    def change_hospital_name(cls, new_name):
        cls.hospital_name = new_name
    
    @staticmethod
    def is_senior(age):
        if age>=60:
            print("Senior citizen")
        else:
            print("Not a Senior Citizen")
    
    def __str__(self):
        return f"Patient ID: {self.patient_id}\nPatient's Name: {self.name}\nAge: {self.age}\nAdmitted Days: {self.admitted_days}\nDaily Charge: {self.daily_charge}"

pat_id = input("Enter the patient ID: ")
pname = input("Enter the patient name: ")
age = int(input("Enter the age of the patient: "))
admit_days = int(input("Enter the number of days admitted: "))
daily_charge = float(input("Enter the daily charge of the patient: "))

pat1 = Patient(pat_id,pname,age,admit_days,daily_charge)

print(pat1.calculate_bill())
print('\n')
Patient.change_hospital_name("Freeman Hospital")
print('\n')
Patient.is_senior(age)
print('\n')
print(pat1)