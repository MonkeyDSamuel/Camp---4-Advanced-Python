'''
Question 5: University Hierarchy (Hybrid Inheritance)
    Create:
        • Class University with a static method get_university_name().
        • Class Department with department name and code.
        • Class Student (inherits from University and Department) that holds student details.
        • Class Result derived from Student that calculates grades.
    Demonstrate:
        • Hybrid inheritance (combining multiple and multilevel).
        • Accessing static, instance, local, and global variables.
        • Using super() for constructor chaining.
        • Method conflict resolution using MRO.

'''

class University:
    def __init__(self,uname):
        self.uname = uname
    @staticmethod
    def uni_name(univ_name):
        print("University Name: "+ univ_name)

class Department:
    def __init__(self,dname,code):
        self.dname = dname
        self.code = code
    
class Student(University,Department):
    def __init__(self, uname, name, age, class_no):
        super().__init__(uname)
        self.name = name
        self.age = age
        self.class_no = class_no

class Result(Student):
    def __init__(self, uname, name, age, class_no, mark):
        super().__init__(uname, name, age, class_no)
        self.mark = mark
        self.grade = ""
    def grade_check(self):
        if 90<= self.mark <=100:
            self.grade = "S"
        elif 80<= self.mark <90:
            self.grade = "A"
        elif 70<= self.mark <80:
            self.grade = "B"
        elif 60<= self.mark <70:
            self.grade = "C"
        elif 50<= self.mark <60:
            self.grade = "D"
        elif 40< self.mark <50:
            self.grade = "E"
        elif self.mark == 40:
            self.grade = "P"
        else:
            self.grade = "F"
        print("Grade: "+self.grade)

rt = Result("AJCE","Samuel",23,12,89)
rt.grade_check()

University.uni_name("KLJC")