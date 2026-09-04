class Student:
    # Constructor
    def __init__(self):
        print("Constructor called")
        self.name = "Rahul"

    # Destructor
    def __del__(self):
        print("Destructor called")


# Create object
obj = Student()

print("Student name:", obj.name)

# Delete object
del obj
