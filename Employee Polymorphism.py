x = 1
while x == 1:
    try_again = input("Do you want to continue?(y/n): ").lower()
    if try_again == "y":
        class Employee:
            def calculate_salary(self):
                        raise NotImplementedError("Subclass must implement this method.")
        try:
            class Intern(Employee):
                    def calculate_salary(self):
                        salary = 150
                        print(f"Your salary as an Intern is ${salary}.")
            class Developer(Employee):
                    def calculate_salary(self):
                        salary = 1000
                        projects = 4
                        print(f"Your salary as a Developer is ${salary}.")
                        print(f"You have completed {projects} projects each for $500.")
                        print(f"Hence, your total salary is ${projects*150 + salary}")
            class Manager(Employee):
                    def calculate_salary(self):
                        salary = 1500
                        print(f"Your salary as a Manager is ${salary} plus a bonus of $150.")
                        print(f"Hence, your total salary is ${salary + 150}.")
            intern_devoloper_or_manager = int(input("""What are you:
1) Inter
2) Developer
3) Manager
Choose from 1-3:
>>> """))
            if intern_devoloper_or_manager == 1:
                Employee = Intern()    
                Employee.calculate_salary()   
            elif intern_devoloper_or_manager == 2:
                Employee = Developer()
                Employee.calculate_salary()
            elif intern_devoloper_or_manager == 3:
                Employee = Manager()
                Employee.calculate_salary()
            else:
                print("Invalid Input.")
        except ValueError:
            print("Input has to be an integer.")
    else:
         print("Okay, Bye Bye!")
         quit()
