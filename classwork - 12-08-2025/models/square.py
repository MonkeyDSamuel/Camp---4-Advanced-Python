from models.Shape import Shape
class Square(Shape):
    def __init__(self):
        self.__side = 0
    def area(self,len):
        self.__side = len
        return self.__side*self.__side