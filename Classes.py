# Creating the class
class Student:
    def __init__(self): # Self is a constructor
        self.name = None
        self.age = None
        self.id = None
        self.marks = None
# Taking Input
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.id = int(input("Enter your ID: "))
        self.marks = int(input("Enter your marks: "))
# Printing the details
    def print_details(self):
        return f'''Student Name: {self.name}
Student Age: {self.age}
Student ID: {self.id}
Student Marks: {self.marks}'''
# Objects
student1 = Student()
print("----------------------------------")
print(student1.print_details())
