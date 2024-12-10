continue_or_not=0
while continue_or_not==0:
        class Employee:
            def calculate_salary(self,salary):
                print(f"The salary of this employee is {salary}.")

        class Developer(Employee):
            salary=0
            projects = 4
            salary=100*projects + salary


            def calculate_salary(self,salary):
                print(f"""The salary of a Developer is ${salary}.
        Including a bonus of $400 for 4 completed projects.""")
        class Mananger(Employee):
            salary=0
            bonus=500
            salary = bonus + salary
            total_salary=salary+bonus
            def calculate_salary(self,salary):
                print(f"""The salary of a Manager ${salary}.
        Including a bonus of $500""")
        class Intern(Employee):
            salary=120
            def calculate_salary(self,salary):
                print(f"""The salary of this employee is ${salary}.
        With no bonus :( """)
        def salary_selection():
            try:
                    selection = int(input("""What would you like to select? 
        1) Manager 
        2) Developer 
        3) Intern 
        >>>  """))
                    if selection==1:
                     employee=Mananger()
                     salary=300
                     employee.calculate_salary(salary)
                    elif selection==2:
                        salary=1500
                        employee=Developer()
                        employee.calculate_salary(salary)
                    elif selection == 3:
                        salary = 1000
                        employee = Intern()
                        employee.calculate_salary(salary)
            except ValueError:
                    print("Please input numbers only.")
                    continue_or_not=input("Would you like to continue or not: ")
        if continue_or_not!="y":
         break


        salary_selection()