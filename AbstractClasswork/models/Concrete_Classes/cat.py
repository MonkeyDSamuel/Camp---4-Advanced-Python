from models.Abstract_Classes.NonFlying import NonFlyingAnimal

class Cat(NonFlyingAnimal):
    def __init__(self,name, legs, color):
        super().__init__(name, legs, color)
    def nofly(self):
        print("Cat doesn't fly")
        print(f"The cat, {self.name} has {self.legs} legs and is {self.color} in color")

cat1 = Cat("Breezy",4,"White")
cat1.nofly()