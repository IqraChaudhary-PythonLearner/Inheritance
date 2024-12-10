class Parent:
    def func1(self):
        print("This is a parent class.")
class Child(Parent):
    def func2(self):
        print("This is a child class.")
object = Child()
object.func1()
object.func2()
