'''
Question 1: School Management System (Multilevel Inheritance)
    Design a system to manage a school.
    Create a Person class with instance variables like name, age, and a method to display
    them.

    From this, derive a class Teacher, adding employee ID, department, and a static
    variable for school name.

    Then, derive a class SubjectTeacher which stores subject and class assigned.
    Use the super() keyword to properly initialize parent classes.

    Add a class-level constant (e.g., MAX_SUBJECTS = 5) and show how local, global,
    and instance variables differ.

    Create objects and demonstrate the complete structure and method calls.
'''

class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    
    def display_employee(self):
        print(f"Employee name: {self.name}\nAge: {self.age}")

class Teacher(Person):
    school_name = "Faith Public School"
    def __init__(self, name, age, emp_ID, department):
        super().__init__(name, age)
        self.emp_ID = emp_ID
        self.department = department
    
class SubjectTeacher(Teacher):
    MAX_SUBJECTS = 5
    def __init__(self, name, age, emp_ID, department, subject, class_no):
        super().__init__(name, age, emp_ID, department)
        self.subject = subject
        self.class_no = class_no

teacher1 = SubjectTeacher("Samuel",23,"SCI001","Science","Physics",10)
teacher1.display_employee()