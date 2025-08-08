class ParentClass:
    'demo parentclass for checking single level inheritance'
    #class variable
    var_one = 679
    def method_parent(self,arg1,arg2):
        total = arg1 + arg2
        print("Sum is: ", total)

class ChildClass(ParentClass):
    def method_child(self,arg3, arg4):
        sum1 = arg3 + arg4
        print("sum is: ",sum1)

obj = ChildClass()
print(obj.var_one)      #to call the parent class' class variable

obj.method_child(10,20)     #to call the ChildClass method
obj.method_parent(30,40)    #to call the ParentClass method