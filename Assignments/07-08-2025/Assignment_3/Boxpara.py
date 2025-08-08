'''
Assignment 3: Box Volume Calculation (with parameterized constructor)
    Scenario:
    Modify the previous Box class to include a parameterized constructor.
    Instructions:
        Use the constructor (__init__) to initialize the dimensions: width, height, depth.
        Create two different box objects with different dimensions.
        Call the get_volume() method to calculate and print the volume of each box.

'''

class Box:
    def __init__(self,width,height,depth):
        self.width = width
        self.height = height
        self.depth = depth
    def get_volume(self):
        return self.height*self.width*self.depth
    
box1 = Box(10,20,10)
box2 = Box(40,20,10)

print(box1.get_volume())
print(box2.get_volume())