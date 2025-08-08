'''
passing value to the child class constructor at the time of object creation
parent class constructor also gets the values using single inheritance

'''

class ParentClass:
    var_parent = 100
    def __init__(self,emp_id,emp_pin):
        self.emp_id = emp_id
        self.emp_pin = emp_pin
    def method_parent(self):
        print('Inside parent class method')

class ChildClass(ParentClass):
    def __init__(self, emp_id, emp_pin, emp_email, emp_salary):
        super().__init__(emp_id, emp_pin)
        self.emp_email = emp_email
        self.emp_salary = emp_salary
    def method_child(self):
        self.method_parent()
        res = self.var_parent + 222
        print("The value of the result is: "+str(res))

    def method_print_data(self):
        print('Employee id is: ' + str(self.emp_id))
        print('Employee pin is: ' + str(self.emp_pin))
        print('Employee email is: ' + str(self.emp_email))
        print('Employee salary is: ' + str(self.emp_salary))

cc = ChildClass(101,1234,'test@gmail.com',20000)
cc.method_print_data()
cc.method_child()