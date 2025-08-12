'''
TASK:
    Create a Employee class for a company HR system.
        1. Store the employee name (public)
        2. Store the salary(private) and allow it to be accessed only via getters/ setters
        3. Validate the salary
            --must be positive
            --can only be increased upto 50% at a time
        4. Keep a read only property called annual_salary which is salary*12
'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__sal = salary
    
    @property
    def get_salary(self):
        return self.__sal
    
    @get_salary.setter
    def set_salary(self, new_sal):
        if (new_sal>=0) & (new_sal <= 1.5*self.__sal):
            self.__sal = new_sal + self.__sal
        else:
            print("Salary is invalid")
    
    @property
    def ann_sal(self):
        return self.__sal*12

emp1 = Employee("Samuel", 20000)

print("Current Salary:", emp1.get_salary)

emp1.set_salary = 10000

print("New Salary: ",emp1.get_salary)

print("Annual Salary: ",emp1.ann_sal)