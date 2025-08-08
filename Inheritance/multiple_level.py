class ParentA:
    'demo for multiple inheritance'
    def display(self):
        print("Inside ParentA class")

class ParentB:
    def display(self):
        print("Inside ParentB class")

class Child(ParentA, ParentB):
    def display(self):
        print("Inside child class")

cl = Child()

cl.display()