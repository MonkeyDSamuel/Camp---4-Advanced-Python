'''
Assignment 1: ATM PIN Verification
    Scenario:
        You are a software developer at XYZ Company. You're tasked with creating a
        program to verify a user's PIN code when they visit an ATM.
        Instructions:
            • Create a class named Verify.
            • In the constructor (__init__), accept the user's PIN input at runtime.
            • Initialize a class variable y with the correct PIN (e.g., 1234).
            • Compare the entered PIN with y using decisional statements (if/else).
            • Print "Access granted" if it matches, or "Access denied" otherwise.

'''

class Verify:
    y = 12345
    def __init__(self,pin):
        self.pin = pin
        if self.pin == Verify.y:
            print("Access Granted")
        else:
            print("Access Denied")

user_pin = int(input("Enter the pin of the user: "))
user = Verify(user_pin)