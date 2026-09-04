class A:
    def __init__(self):
        self.__x = 10

    def show(self):
        print("Private variable:", self.__x)


class B(A):
    def display(self):
        print("Private variable cannot be accessed directly in class B")


obj = B()

obj.show()
obj.display()
