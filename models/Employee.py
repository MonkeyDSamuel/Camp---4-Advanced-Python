class Employee:
    'common base class for all Employees'

    cname = 'FaithInfotech'
    
    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

#create employee object
emp1 = Employee('Tom', 54)
emp1.cname='Tensor'
print(emp1.cname)

print(f'{emp1.name}\n{emp1.age}')
# emp1 = Employee()
# emp1.name = 'TOM'
# emp1.age = 10

#Employee 2

# emp2 = Employee()
# print(emp2.name)
# print(Employee.__doc__)
# print(emp1.name)
# print(emp1.age)
# print(emp1)
# print(sys.getsizeof(emp1))