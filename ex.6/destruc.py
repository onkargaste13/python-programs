class Student:
    def __init__(self):
        self.name = "Onkar Gaste"
        print("Object Created")

    def __del__(self):
        print("Object Destroyed")
        print(self.name)

s1 = Student()

del s1