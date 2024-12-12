class Employee:
    def __init__(self):
        self.name = None
        self.id = None
        self.name = input("Enter your name: ")
        self.id = int(input("Enter your ID: "))
    def display_info(self):
        print(f"Your name is {self.name}.")
        print(f"Your ID is {self.id}.")
class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.team_size = None
        self.team_size = int(input("Enter the team size: "))
    def display_info(self):
        super().display_info()
        print(f"You have {self.team_size} members in your team.")
user1 = Manager()
user1.display_info() 