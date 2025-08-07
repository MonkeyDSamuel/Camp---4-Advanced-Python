'''
Assignment 2: Box Volume Calculation (with method)
    Scenario:
        Create a class named Box that can calculate the volume of a box.
        Instructions:
            Create instance variables: width, height, and depth.
            Create a method get_volume() that calculates and returns the volume.
            In another class or in the main section, create two Box objects.
            Assign different values to their dimensions and print their volumes.

'''

class Box:
    def __init__(self):
        pass
    def volume(self,height,width,depth):
        return height*width*depth

box1 = Box()
box2 = Box()

# box1.width = 10
# box1.height = 20
# box1.depth = 10

# box2.width = 50
# box2.height = 20
# box2.depth = 10

print(box1.volume(10,20,10))
print(box2.volume(30,20,10))