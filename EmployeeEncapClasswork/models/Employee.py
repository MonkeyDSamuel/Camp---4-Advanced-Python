'''
TASK:
Menu-driven employee management system that allows the user to:

Add Employee: validation name, salary
    Fields:
        employee_id(unique,integer)
        name(string)
        department(string)
        salary(float)
        should reject if employee_id already exists
Update Employee
    User can update name.department, or salary of an existing employee
    If the employee doesn't exist, show a message
Search employee
    Search by employee_id or name
    If found, print employee details
    Exit ends the program

'''

import random
class Employee:
    'The Employee class used to perform the above assigned functions'
    emp_ids = []
    def __init__(self, name = None, department = None, salary = None):
        while True:
            id = random.randint(1,1000)
            if id not in Employee.emp_ids:
                self.__emp_id = id
                Employee.emp_ids.append(id)
                break
        self.__name = name
        self.__dept = department
        self.__sal = salary
    
    @property
    def get_emp_id(self):
        return self.__emp_id
    
    @property
    def get_emp_name(self):
        return self.__name

    @get_emp_name.setter
    def set_emp_name(self,name):
        if not isinstance(name,str):
            raise ValueError("The name must be of string type")
        elif not name.strip():
            raise ValueError("The name is required")
        else:
            self.__name = name
    @property
    def get_dept_name(self):
        return self.__dept
    
    @get_dept_name.setter
    def set_dept_name(self,dept):
        if not dept.strip():
            raise ValueError("The department must not be empty")
        self.__dept = dept
    
    @property
    def get_sal(self):
        return self.__sal
    
    @get_sal.setter
    def set_sal(self,sal):
        if not isinstance(sal,float):
            raise ValueError("The salary must be of float type")
        elif not sal:
            raise ValueError("The salary must be present")
        else:
            self.__sal = sal
    
    def display_emp_details(self):
        print(f"""
                Employee ID: {self.__emp_id}
                Employee Name: {self.__name}
                Department: {self.__dept}
                Salary: {self.__sal}
                """)