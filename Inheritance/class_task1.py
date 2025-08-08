'''
TASK: MULTILEVEL INHERITANCE

    Design a Python program using multilevel 
    inheritance to manage an Employee Payroll System. 

    Create a base class SuperClass that stores the employee's ID and password. 

    Derive a class SubClassOne from SuperClass to store additional employee details 
    such as address, email ID, and mobile number. 

    Then, derive another class SubClassTwo 
    from SubClassOne to handle salary-related information 
    including salary, HRA, DA, deductions, and bonus. 

    Implement a method net_sal() in SubClassTwo 
    to calculate the net salary using 
    the formula: Net Salary = Salary + HRA + DA + Bonus - Deduction.

    Also, create a method show_details() in 
    SubClassTwo to display the employee’s ID, email ID, mobile number, and net salary. 

    Use the super() keyword appropriately to call constructors of parent classes. 
    Finally, create an object of SubClassTwo, 
    and call the methods to display the required outputs.

'''

class SuperClass:
    def __init__(self,emp_id,password):
        self.emp_id = emp_id
        self.password = password

class SubClassOne(SuperClass):
    def __init__(self, emp_id, password, address, email, phone):
        super().__init__(emp_id,password)
        self.address = address
        self.email = email
        self.phone = phone

class SubClassTwo(SubClassOne):
    def __init__(self,emp_id, password, address, email, phone,salary,HRA,DA,deductions,bonus):
        super().__init__(emp_id, password, address, email, phone)
        self.salary = salary
        self.HRA = HRA
        self.DA = DA
        self.deductions = deductions
        self.bonus = bonus
    def net_sal(self):
        self.net_salary = self.salary + self.HRA + self.DA + self.bonus - self.deductions
        print(self.net_salary)
    def __str__(self):
        return f'Employee ID: {self.emp_id}\nPassword: {self.password}\nAddress: {self.address}\nEmail: {self.email}\nPhone: {self.phone}\nSalary: {self.salary}\nHRA: {self.HRA}\nDA: {self.DA}\nDeductions: {self.deductions}\nBonus: {self.bonus}\nNet Salary: {self.net_salary}'

print('\n')
print("---------Employee Payroll System---------")
emp1 = SubClassTwo(1001,"hello@123","Kazhakootam, Trivandrum","samuelcsofficial@gmail.com",9089876789,150000,20000,10000,3000,50000)
print('\n')
emp1.net_sal()
print('\n')
print(emp1)