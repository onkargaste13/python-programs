class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):
        super().speak()   # Call parent class method
        print("Dog barks")


d = Dog()
d.speak()