from abc import abstractmethod
from models.Abstract_Classes.Animal import Animal

class NonFlyingAnimal(Animal):
    
    @abstractmethod
    def nofly(self):
        pass

