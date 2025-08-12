from models.Employee import Employee

class MenuDriven:
    'The Menu driver to handle all Employee class\'s functions'
    def __init__(self):
        self.employees = []

    def show_menu(self):
        print('''
                1. Add Employee
                2. List Employees
                3. Update Employee details
                4. Search by Employee ID/ Employee Name
                5. EXIT
            ''')
    
    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                name = input("Enter the name of the Employee: ")
                dept = input("Enter the department name: ")
                sal = float(input("Enter the salary of the Employee: "))
                employee = Employee(name,dept,sal)
                self.employees.append(employee)
            elif choice == "2":
                for id,emp in enumerate(self.employees, start = 1):
                    print(f"S.No: {id}")
                    emp.display_emp_details()
            elif choice == "3":
                emp_id = int(input("Enter the Employee's ID whose details are to be updated: "))
                flag = False
                for emp in self.employees:
                    if emp.get_emp_id == emp_id:
                        name = input(f"Updated Employee Name: [{emp.get_emp_name}]") or emp.get_emp_name
                        dept = input(f"Update department name of the Employee: [{emp.get_dept_name}]") or emp.get_dept_name
                        sal = float(input(f"Update the salary of the Employee: [{emp.get_sal}]") or emp.get_sal)

                        emp.set_emp_name = name
                        emp.set_dept_name = dept
                        emp.set_sal = sal

                        print(f"""
                            The Employee ID:{emp_id}\'s Updated details are:
                            Employee Name: {name}
                            Department: {dept}
                            Salary: {sal}
                            """)
                        flag = True
                        break
                if not flag:
                    print(f"Employee not found!!!")
                
            elif choice == "4":
                print(f"""
                        Search methods:
                        1. Search by Employee ID
                        2. Search by Employee Name
                        """)
                ch = input("Enter the choice to search by:")
                flag = False
                if ch == "1":
                    id = int(input("Enter the Employee ID: "))
                    for emp in self.employees:
                        if emp.get_emp_id == id:
                            emp.display_emp_details()
                            flag = True
                    if not flag:
                        print("EMPLOYEE NOT FOUND!!!")
                elif ch == "2":
                    name = input("Enter the name of the Employee: ")
                    for emp in self.employees:
                        if emp.set_emp_name == name:
                            emp.display_emp_details()
                            flag = True
                    if not flag:
                        print("EMPLOYEE NOT FOUND!!!")
                else:
                    print("INAVLID CHOICE....EXITING....")

            elif choice == "5":
                print("EXITING...")
                break

            else:
                print("INVALID CHOICE...ENTER AGAIN")