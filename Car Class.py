import time
class Car:
    def __init__(self):
        self.colour = input("Enter the colour of your car: ")
        self.model = input("Enter the model of your car: ")
        self.measurement = input("What do you want to measure in mph or km/h: ").lower()
        if self.measurement != "km/h" and self.measurement != "mph":
            print("Sorry, that option is not available.")
        self.speed = int(input(f"Enter the speed of your car({self.measurement}): "))
        self.list_of_speeds = []
        self.accelerated_speed = int(input("To what speed do you want to accelerate to?: "))
    
    def accelerate(self):
        print(f"Accelerating from {self.speed}km/h to {self.accelerated_speed}{self.measurement}...")
        time.sleep(2.8)
        if self.accelerated_speed < self.speed:
            print(f"Your accelerated speed has to be less than {self.speed}")
            quit()
        print(f"Your car has been accelerated by {self.accelerated_speed-self.speed}{self.measurement}")


    def brake(self):
        brake_or_not = input("Do you want to hit the brake?(y/n): ").lower()
        if brake_or_not == "y":
            print("Stopping the car...")
            time.sleep(2.5)
            print("Car has been stopped")
        elif brake_or_not == "n":
            print("Car is still driving...")
            time.sleep(2)
            Car.accelerate(self)
        else:
            print("Invalid Input")
    
    def slow_down(self):
        slow_or_no = input("Do you want to slow down or no(y/n): ").lower()
        if slow_or_no == "y":
            slow_amount = int(input("How much do you want to slow down by?: "))
            new_speed = self.accelerated_speed - slow_amount
            print("Slowing down...")
            time.sleep(3)
            print(new_speed)

Car1 = Car()
Car1.accelerate()
Car1.brake()
Car1.slow_down()
