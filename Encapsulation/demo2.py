class Classdata:
    'demo to set getter and setter for private data members'
    def __init__(self, data):
        self.__data = data
        self.__age = 0
    
    @property
    def get_age(self):
        return self.__age

    @get_age.setter
    def set_age(self, new_age):
        self.__age = new_age

    @property
    def get_data(self):
        print("hello")
        return self.__data

    @get_data.setter
    def set_data(self, new_data):
        if new_data >= 0:
            self.__data = new_data
        else:
            raise ValueError("Value must be positive")

obj = Classdata(40)
obj2 = Classdata(40)
print("Accessing private variable with gettter", obj.get_data)
# modifying the private variable with setter
obj.set_data = 40   #calls the setter and sets value to 20
print("Changed the private variable with setter",obj.get_data)