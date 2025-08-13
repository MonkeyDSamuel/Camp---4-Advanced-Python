from abc import ABC, abstractmethod
class Animal(ABC):
    
    def __init__(self, name, legs, color):
        self.name = ""
        self.legs = 0
        self.color = ""
    @abstractmethod
    def walk(self,legs):
        pass
    
    @abstractmethod
    def cry(self,cry):
        pass