class Super:
    'demo for multivel inheritance'
    def method_super(self):
        print("Super class method called...")

class SubClassA(Super):
    def method_SubClassA(self):
        print("SubClassA class method called...")

class SubClassB(SubClassA):
    def method_SubClassB(self):
        print("SubClassB method called...")

st = SubClassB()
#with st object, I can call the methods of all of it's parent methods

st.method_super()
st.method_SubClassA()
st.method_SubClassB()