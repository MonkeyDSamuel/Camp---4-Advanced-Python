class ClassOne:
    'demo for private access specifier'
    #private class specifier
    __total = 500
    def __init__(self, a, b):
        self.__a = a   #private instance variable
        self.b = b
    
    def print_values(self):
        #can access the private variable inside the class
        print(f"Private class variable: {self.__a}")
        print(f"Public class variable: {self.b}")
        print(f"With object, try to access, {obj.__a}")


obj = ClassOne(111,222)
obj.print_values()
# print("not able to access the private the data member", obj.__a)