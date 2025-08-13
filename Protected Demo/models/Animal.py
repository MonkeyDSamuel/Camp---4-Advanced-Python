class Animal:
    'demo for protected member inheritamce'
    '''
        If we declare variables and methdos protected,
        it is accessiblke inside the class
        its not accessible outisde the class in (JAVA/C++/C#)
        but in Python, its acessible and not really secures.
        its just a developer's signal that it's protected.
        Subclasses can easily access protected members.
        Direct access to protected members is possible in Python
        with object, but its not recommended!!!
    '''

    def __init__(self, name):
        self._name =name    #protected attribute

    def _make_sound(self):  #protected method
        print(f"{self._name} makes a sound")
    
    def show_name(self):
        print(f"Animal name: {self._name}")
    
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        #accessing the protected variable from parent
        print(f"The {self.breed}, {self._name} says woof!!!")
        #accessing protected method
        self._make_sound()

#create object
dog = Dog("Blackie","Bull Dog")
dog.bark()
dog.show_name()
#direct access to protected is possible but not recommended
print(dog._name)