import time
class Car:
    def __init__(self):
        self.colour = input("Enter the colour of your car: ")
        self.model = input("Enter the model of your car: ")
        self.measurement = input("What do you want to measure in mph or km/h: ").lower()
        
        if self.measurement != "km/h" and self.measurement != "mph":
            print("Sorry, that option is not available.")
        
        while self.measurement != "km/h" and self.measurement != "mph":
            self.measurement = input("What do you want to measure in mph or km/h: ").lower()
        self.list_of_accelerations = []
        self.speed = int(input(f"Enter the speed of your car({self.measurement}): "))
        self.accelerated_speed = self.speed
    def accelerate(self):
        self.speed = self.accelerated_speed
        self.accelerated_speed = int(input("To what speed do you want to accelerate to?: "))
        if self.accelerated_speed > self.speed:    
            self.list_of_accelerations.append(self.accelerated_speed)
        print(f"Accelerating from {self.speed}{self.measurement} to {self.accelerated_speed}{self.measurement}...")
        time.sleep(2.8)
        if self.accelerated_speed < self.speed:
            print("ERROR IN ACCELERATING: FAILED TO ACCELERATE")
            print(f"Your accelerated speed has to be more than {self.speed}{self.measurement}")
            self.accelerated_speed = int(input("To what speed do you want to accelerate to?: "))
            while self.accelerated_speed < self.speed:
                self.accelerated_speed = int(input("To what speed do you want to accelerate to?: "))
        accelerated_amount = self.accelerated_speed - self.speed
        print(f"Your car has been accelerated by {abs(accelerated_amount)}{self.measurement}")
    def brake(self):
        brake_or_not = input("Do you want to hit the brake?(y/n): ").lower()
        if brake_or_not == "y":
            print("Stopping the car...")
            time.sleep(2.5)
            print("Car has been stopped")
            continue_or_no = input("Do you want to continue?(y/n): ").lower()
            while continue_or_no != "n":
                    to_continue = input("To continue you have to start your car(PRESS OK) otherwise type anything else to quit: ").lower()
                    if to_continue == "ok":
                        if continue_or_no == "y":
                            options = int(input("""What do you want to do: 
1) Accelerate
2) Slow Down
3) Hit the brakes
4) Quit(Q OR q)
Enter a number from 1-4
>>> """))
                            if options == 1:
                                Car.accelerate(self)
                            elif options == 2:
                                Car.slow_down(self)
                            elif options == 3:
                                Car.brake(self)
                            elif options == 4 or options == "q" or options == "Q":
                                print("Bye, bye!")
                                quit()
                            else:
                                print("Invalid Input.")
                    elif to_continue != "ok":
                        quit()
            else:
                print("Invalid Input")

        elif brake_or_not == "n":
            print("Car is still driving...")
            time.sleep(2)
            Car.accelerate(self)
            x = 1
            while x == 1:
                continue_or_no = input("Do you want to continue?(y/n): ").lower()
                if continue_or_no == "y":
                        options = int(input("""What do you want to do: 
1) Accelerate
2) Slow Down
3) Hit the brakes
4) Quit(Q OR q)
Enter a number from 1-4
>>> """))
                        if options == 1:
                            Car.accelerate(self)
                        elif options == 2:
                            Car.slow_down(self)
                        elif options == 3:
                            Car.brake(self)
                        elif options == 4 or options == "q" or options == "Q":
                            print("Bye, bye!")
                            print("Car is slowing down to stop.")
                            time.sleep(2.5)
                            quit()
                        else:
                            print("Invalid Input.")
                if continue_or_no != "y":
                    print("Bye, bye!")
                    print("Car is slowing down to stop.")
                    time.sleep(2.5)
                    quit()
        else:
            print("Invalid Input")
    
    def slow_down(self):
        slow_or_no = input("Do you want to slow down or no(y/n): ").lower()
        if slow_or_no == "y":
            slow_amount = int(input("How much do you want to slow down by?: "))
            new_speed = self.accelerated_speed - slow_amount
            print("Slowing down...")
            time.sleep(3)
            print(f"You have slowed down to {new_speed}{self.measurement}.")
            continue_or_no = input("Do you want to continue?(y/n): ").lower()
            while continue_or_no != "n":
                    if continue_or_no == "y":
                        options = int(input("""What do you want to do: 
1) Accelerate
2) Slow Down
3) Hit the brakes
4) Quit
Enter a number from 1-4
>>> """))
                        if options == 1:
                            Car.accelerate(self)
                        elif options == 2:
                            Car.slow_down(self)
                        elif options == 3:
                            Car.brake(self)
                        elif options == 4:
                            print("Bye, bye!")
                            print("Car is slowing down to stop.")
                            time.sleep(2.5)
                            quit()
                        else:
                            print("Invalid Input.")
        else:
            accelerate_or_not = input("Do you want to accelerate or not?(y/n): ").lower()
            if accelerate_or_not == "y":
                Car.accelerate(self)
                x = 1
                while x == 1:
                    continue_or_no = input("Do you want to continue?(y/n): ").lower()
                    if continue_or_no == "y":
                        options = int(input("""What do you want to do: 
1) Accelerate
2) Slow Down
3) Hit the brakes
4) Quit
Enter a number from 1-4
>>> """))
                        if options == 1:
                            Car.accelerate(self)
                        elif options == 2:
                            Car.slow_down(self)
                        elif options == 3:
                            Car.brake(self)
                        elif options == 4:
                            print("Bye, bye!")
                            quit()
                        else:
                            print("Invalid Input.")
                    elif continue_or_no != "y":
                        print("Car is slowing down to stop.")
                        time.sleep(2.5)
            else:
                    print("Bye, bye!")
                    print("Car is slowing down to stop.")
                    time.sleep(2.5)
                    quit()



Car1 = Car()
Car1.accelerate()
Car1.brake()
Car1.slow_down()
