class Vehicle:
    def __init__(self):
        self.make = None
        self.model = None
        self.make = input("Enter the car name: ")
        self.model = input("Enter the car model: ")
    def display_info(self):
        print(f"You have a {self.make}")
        print(f"You have a model of {self.model}")
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.number_of_door = None
        self.number_of_door = int(input("Enter the number of doors: "))
    def display_info(self):
        super().display_info()
        print(f"There are {self.number_of_door} doors.")
user1 = Car()
user1.display_info()