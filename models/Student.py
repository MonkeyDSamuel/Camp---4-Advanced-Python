'''
    TASK:   create a class Student
            create a class variable school_name and set it to "ABC school"
            create a constructor which receives name, grade
            add a display_info() method that prints name, grade and school_name
            change the school_name for one student using object and see whether the school_name is changed for all newly created students if not, how to change?


'''
class Student:
    'common class for all Students'
    school_name = 'ABC school'
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    
    def display_info(self):
        print(f'Name:{self.name}\nGrade:{self.grade}\nSchool Name:{self.school_name}')

stud1 = Student('Samuel','10th')
stud1.school_name = 'Faith High School'
stud1.display_info()

stud1 = Student('George','12th')
stud1.display_info()

#change the school name for all upcoming students
Student.school_name = 'Little Flower Public School'
stud3 = Student('Jerry','9th')
stud3.display_info()