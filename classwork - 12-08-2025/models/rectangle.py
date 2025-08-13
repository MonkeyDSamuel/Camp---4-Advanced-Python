from models.Shape import Shape
class Rectangle(Shape):
    def __init__(self):
        self.__length = 0
        self.__breadth = 0
    def area(self, len, bread):
        self.__length = len
        self.__breadth = bread
        return self.__length*self.__breadth