class A:
    def __init__(self):
        self.__private_var = 10
        self._protected_var = 20

    def __private_function(self):
        print("Private function of A")

    def _protected_function(self):
        print("Protected function of A")

    def show_private(self):
        print("Private variable:", self.__private_var)
        self.__private_function()


class B(A):
    def display_b(self):
        print("Protected variable:", self._protected_var)
        self._protected_function()


class C(B):
    def display_c(self):
        print("C class")


obj = C()

obj.show_private()
obj.display_b()
obj.display_c()
