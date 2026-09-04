class A:
    def _show(self):
        print("Protected function of class A")


class B(A):
    def display(self):
        self._show()


obj = B()
obj.display()
