# Shape Class
# While Loop
x = 1
while x == 1:
    # Continue or Not
    continue_or_not = input("Do you want to continue❓(y/n): ").lower()
    if continue_or_not == "y":
        # Try statement
        try:
            # Main Class/Base Class
            class Shape:
                # Method
                def area(self): # Not defining constructor just defining method.
                    raise NotImplementedError("Subclass must implement this method.")
            shape = int(input("""Choose a shape: 
1) Circle
2) Rectangle
3) Square
4) Triangle
Choose from 1-4:
>>> """))
            measurement = input("Enter the measurement you want?(cm or m): ").lower()
            # Subclass 1
            class Circle(Shape):
                def area(self):
                    radius = int(input(f"Enter the radius of the circle🔵({measurement}): "))
                    area_of_circle = 3.14 * radius**2
                    print(f"The area of the circle having radius {radius}{measurement} is {area_of_circle}{measurement}.")
            # Subclass 2
            class Rectangle(Shape):
                def area(self):
                    length = int(input("Enter the length of the rectangle: "))
                    breadth = int(input("Enter the breadth of the rectangle: "))
                    area_of_rectangle = length * breadth
                    print(f"The area of the rectangle having a length of {length}{measurement} and {breadth}{measurement} is {area_of_rectangle}{measurement}.")
            # Subclass 3
            class Square(Shape):
                def area(self):
                    length = int(input("Enter the length of the square: "))
                    area_of_square = length * length
                    print(f"The area of the square having a length of {length}{measurement} is {area_of_square}{measurement}.")
            # Subclass 4
            class Triangle(Shape):
                def area(self):
                    base = int(input("Enter the breadth of the triangle: "))
                    height = int(input("Enter the height of the triangle: "))
                    area_of_triangle = height * base * 1/2
                    print(f"The area of the triangle having a base of {base}{measurement} and height of {height}{measurement} is {area_of_triangle}{measurement}.")
            # Objects/Main Polymorphism
            if shape == 1:
                Shape = Circle()
                Shape.area()
            elif shape == 2:
                Shape = Rectangle()
                Shape.area()
            elif shape == 3:
                Shape = Square()
                Shape.area()
            elif shape == 4:
                Shape = Triangle()
                Shape.area()
            else:
                print("Sorry, there is no such option given❌")
        except ValueError:
            print("You have to enter a number from 1-4.☹")
    # Quit
    else:
        print("Okay, Bye Bye😊!")
        quit()
                