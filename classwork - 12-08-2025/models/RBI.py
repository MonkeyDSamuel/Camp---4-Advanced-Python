class RBI:
    'demo for method overriding in which all banks follow RBI reulations'
    'child or sub classes are SBI, UPI, PNB,...goes on'
    def __init__(self):
        self.__rate_of_interest = 5.5   #private variable
    #getter method 
    def get_rate_of_interest(self):
        return self.__rate_of_interest
    #custom method
    def display_rate_of_interest(self):
        print("RBI rate interest is: ",self.__rate_of_interest)