class A:
    def __private_function(self):
        print("Private function of A")


class B(A):
    def display_b(self):
        print("B class")


class C(B):
    def display_c(self):
        print("C class")


obj = C()

# Private function cannot be called directly
print("Private function cannot be accessed directly")
