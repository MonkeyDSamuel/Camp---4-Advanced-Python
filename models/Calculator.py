class Calculator:
    'Class to perform arithmetic calculations'
    def __init__(self,num1,num2,op):
        self.num1 = num1
        self.num2 = num2
        self.op = op
    def add(self):
        print(f"Sum:{eval(f'{self.num1}{self.op}{self.num2}')}")
    def difference(self):
        print(f"Difference:{eval(f'{self.num1}{self.op}{self.num2}')}")
    def multiply(self):
        print(f"Product:{eval(f'{self.num1}{self.op}{self.num2}')}")
    def divide(self):
        if self.num2 == 0:
            print("----Division by zero not possible----")
        else:
            print(f"Quotient:{eval(f'{self.num1}{self.op}{self.num2}')}")


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
op = input("Enter the operator(+,-,*./): ")

result = Calculator(num1,num2,op)
if op=='+':
    result.add()
elif op == '-':
    result.difference()
elif op == '*':
    result.multiply()
elif op == '/':
    result.divide()
else:
    print("Operation not possible....Invalid operator")