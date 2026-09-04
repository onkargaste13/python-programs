class A:
    def __init__(self):
        self._x = 20


class B(A):
    def display(self):
        print("Protected variable:", self._x)


obj = B()
obj.display()
