from abc import abstractmethod
from Abstract_Classes.Animal import Animal

class FlyingAnimal(Animal):

    @abstractmethod
    def fly(self):
        pass